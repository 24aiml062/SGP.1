from __future__ import annotations

from app.schemas.content import ContentRequest


def build_prompt(request: ContentRequest, plan: dict = {}) -> str:
    b = request.brief

    # ── Plan context (only include lines where the value is set) ──────────
    plan_lines: list[str] = []
    if plan.get("niche"):
        plan_lines.append(f"- Business niche: {plan['niche']}")
    if plan.get("growth_objective"):
        plan_lines.append(f"- Growth objective: {plan['growth_objective']}")
    if plan.get("target_audience"):
        plan_lines.append(f"- Target audience (plan): {plan['target_audience']}")
    if plan.get("tone"):
        plan_lines.append(f"- Brand tone: {plan['tone']}")
    if plan.get("platforms"):
        platforms_str = (
            ", ".join(plan["platforms"])
            if isinstance(plan["platforms"], list)
            else plan["platforms"]
        )
        plan_lines.append(f"- Primary platforms: {platforms_str}")

    # ── Effective tone: brief wins, plan is fallback ──────────────────────
    effective_tone = b.tone or plan.get("tone", "professional")

    # ── Effective audience: brief is specific, plan adds context ─────────
    if b.target_audience and plan.get("target_audience"):
        effective_audience = f"{b.target_audience} (broader: {plan['target_audience']})"
    else:
        effective_audience = b.target_audience or plan.get("target_audience", "general audience")

    # ── Assemble prompt ───────────────────────────────────────────────────
    parts: list[str] = [
        "You are an expert digital marketing copywriter.",
    ]

    if plan_lines:
        parts.append("Brand strategy context:")
        parts.extend(plan_lines)
        parts.append(
            f"\nYour job is to create {request.content_type} content for "
            f"{request.platform} that directly serves the growth objective above."
        )

    parts.append("\nContent brief:")
    parts.append(f"- Product / offer: {b.product_name} — {b.description}")
    parts.append(f"- Audience: {effective_audience}")
    parts.append(f"- Tone: {effective_tone}")

    if b.keywords:
        parts.append(f"- Keywords: {', '.join(b.keywords)}")
    if b.cta:
        parts.append(f"- CTA: {b.cta}")

    # ── Type-specific instructions ────────────────────────────────────────
    parts.append("")
    if request.content_type == "social_media":
        parts.append(
            "Write a social media caption for the platform above. "
            "Include 5-8 relevant hashtags. "
            'Respond ONLY with valid JSON: {"body": "...", "hashtags": ["#tag1", ...]}'
        )
    elif request.content_type == "seo":
        parts.append(
            "Write SEO-optimised copy for the platform above. "
            "Always include a meta description (max 160 chars) and a title tag (max 60 chars). "
            'Respond ONLY with valid JSON: {"body": "...", "meta_description": "...", "title_tag": "..."}'
        )
    else:  # ad_copy
        parts.append(
            "Write ad copy: 2 headline variants (max 30 chars each) and 1 description (max 90 chars). "
            'Respond ONLY with valid JSON: {"body": "...", "headline_1": "...", "headline_2": "...", "description": "..."}'
        )

    parts.append("\nRespond ONLY with valid JSON. No preamble, no markdown.")
    return "\n".join(parts)
