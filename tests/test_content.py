"""Tests for POST /api/content/generate — OpenAI is fully mocked."""
from __future__ import annotations

import json
import sys
import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

# Root is one level up from tests/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from main import app  # noqa: E402

client = TestClient(app)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _mock_response(body: str, extra: dict | None = None):
    payload = {"body": body}
    if extra:
        payload.update(extra)

    choice = MagicMock()
    choice.message.content = json.dumps(payload)

    usage = MagicMock()
    usage.total_tokens = 120

    resp = MagicMock()
    resp.choices = [choice]
    resp.usage = usage
    return resp


# ---------------------------------------------------------------------------
# Fixtures / payloads
# ---------------------------------------------------------------------------

SOCIAL = {
    "content_type": "social_media",
    "platform": "Instagram",
    "brief": {
        "product_name": "Sunrise Bakery",
        "description": "Artisan sourdough baked fresh daily.",
        "target_audience": "Foodies and local families",
        "tone": "casual",
        "keywords": ["sourdough", "fresh", "local"],
        "cta": "Visit us today!",
    },
    "variants": 1,
}

SEO = {
    "content_type": "seo",
    "platform": "Blog",
    "brief": {
        "product_name": "Sunrise Bakery",
        "description": "Artisan sourdough baked fresh daily.",
        "target_audience": "Health-conscious readers",
        "tone": "professional",
        "keywords": ["sourdough", "artisan bread"],
    },
    "variants": 1,
}

AD_COPY = {
    "content_type": "ad_copy",
    "platform": "Google Ads",
    "brief": {
        "product_name": "Sunrise Bakery",
        "description": "Artisan sourdough baked fresh daily.",
        "target_audience": "Local customers",
        "tone": "urgent",
        "cta": "Order now",
    },
    "variants": 1,
}


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@patch("app.services.content_service.AsyncOpenAI")
def test_social_media_generate(mock_cls):
    mock_client = MagicMock()
    mock_cls.return_value = mock_client
    mock_client.chat.completions.create = AsyncMock(
        return_value=_mock_response(
            "Fresh sourdough every morning! 🍞",
            {"hashtags": ["#sourdough", "#fresh", "#local", "#bakery", "#artisan"]},
        )
    )

    res = client.post("/api/content/generate", json=SOCIAL)
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["content_type"] == "social_media"
    assert data["platform"] == "Instagram"
    assert len(data["variants"]) == 1
    v = data["variants"][0]
    assert v["body"] != ""
    assert v["character_count"] == len(v["body"])
    assert v["id"].startswith("gen_")
    assert isinstance(data["tokens_used"], int)
    assert "generated_at" in data


@patch("app.services.content_service.AsyncOpenAI")
def test_seo_generate(mock_cls):
    mock_client = MagicMock()
    mock_cls.return_value = mock_client
    mock_client.chat.completions.create = AsyncMock(
        return_value=_mock_response(
            "Discover the art of sourdough baking.",
            {"meta_description": "Artisan sourdough baked fresh.", "title_tag": "Sunrise Bakery"},
        )
    )

    res = client.post("/api/content/generate", json=SEO)
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["content_type"] == "seo"
    assert len(data["variants"]) == 1
    assert data["variants"][0]["body"] != ""


@patch("app.services.content_service.AsyncOpenAI")
def test_ad_copy_generate(mock_cls):
    mock_client = MagicMock()
    mock_cls.return_value = mock_client
    mock_client.chat.completions.create = AsyncMock(
        return_value=_mock_response(
            "Order fresh bread now!",
            {"headline_1": "Fresh Daily", "headline_2": "Order Now", "description": "Artisan sourdough."},
        )
    )

    res = client.post("/api/content/generate", json=AD_COPY)
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["content_type"] == "ad_copy"
    assert len(data["variants"]) == 1


def test_missing_required_brief_fields():
    """Pydantic should reject a brief missing required fields → 422."""
    res = client.post("/api/content/generate", json={
        "content_type": "social_media",
        "platform": "Instagram",
        "brief": {},   # missing product_name, description, target_audience, tone
    })
    assert res.status_code == 422


def test_invalid_content_type():
    """Unknown content_type should fail Pydantic validation → 422."""
    res = client.post("/api/content/generate", json={
        "content_type": "invalid_type",
        "platform": "Instagram",
        "brief": {
            "product_name": "Test",
            "description": "Test desc",
            "target_audience": "Everyone",
            "tone": "casual",
        },
    })
    assert res.status_code == 422
