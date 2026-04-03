from __future__ import annotations

import json
import os
import re
import secrets
from datetime import datetime, timezone

from huggingface_hub import InferenceClient

from app.prompts.content_prompts import build_prompt
from app.schemas.content import ContentRequest, ContentResponse, ContentVariant

HF_MODEL = "Qwen/Qwen2.5-7B-Instruct"


def _make_id() -> str:
    return "gen_" + secrets.token_hex(4)


class ContentService:
    def __init__(self) -> None:
        api_key = os.getenv("HF_API_KEY", "")
        self._enabled = bool(api_key and not api_key.startswith("hf_your"))
        self._client = InferenceClient(api_key=api_key) if self._enabled else None

    async def generate(self, request: ContentRequest, plan: dict = {}) -> ContentResponse:
        if not self._enabled:
            raise ValueError(
                "HF_API_KEY is not configured. "
                "Add your Hugging Face token to the .env file."
            )

        variants: list[ContentVariant] = []
        total_tokens = 0

        for _ in range(request.variants):
            response = self._client.chat.completions.create(
                model=HF_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert marketing copywriter. "
                            "Always respond with valid JSON only. No markdown, no explanation."
                        ),
                    },
                    {"role": "user", "content": build_prompt(request, plan)},
                ],
                max_tokens=600,
                temperature=0.8,
            )

            text = response.choices[0].message.content or ""
            total_tokens += len(text.split()) * 2  # rough estimate

            data = self._extract_json(text)

            body     = data.get("body", "")
            hashtags = data.get("hashtags") or None
            cta      = data.get("cta") or request.brief.cta or None

            variants.append(
                ContentVariant(
                    id=_make_id(),
                    body=body,
                    hashtags=hashtags,
                    cta=cta,
                    character_count=len(body),
                    meta_description=data.get("meta_description") or None,
                    title_tag=data.get("title_tag") or None,
                    headline_1=data.get("headline_1") or None,
                    headline_2=data.get("headline_2") or None,
                )
            )

        return ContentResponse(
            content_type=request.content_type,
            platform=request.platform,
            variants=variants,
            tokens_used=total_tokens,
            generated_at=datetime.now(timezone.utc),
            plan_used=bool(plan),
        )

    @staticmethod
    def _extract_json(text: str) -> dict:
        """Extract the first valid JSON object from model response."""
        # Strip markdown fences
        text = re.sub(r"```(?:json)?", "", text).strip()

        # Find the first { and match its closing }
        start = text.find("{")
        if start == -1:
            raise ValueError(f"No JSON object found in model response: {text[:200]}")

        depth = 0
        for i, ch in enumerate(text[start:], start):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:i + 1])
                    except json.JSONDecodeError as exc:
                        raise ValueError(f"Invalid JSON from model: {exc}") from exc

        raise ValueError(f"Unmatched braces in model response: {text[:200]}")
