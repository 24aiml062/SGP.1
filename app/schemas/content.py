from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field


class ContentBrief(BaseModel):
    product_name: str
    description: str
    target_audience: str
    tone: Literal["professional", "casual", "witty", "urgent"]
    keywords: List[str] = Field(default_factory=list)
    cta: Optional[str] = None


class ContentRequest(BaseModel):
    content_type: Literal["social_media", "seo", "ad_copy"]
    platform: str
    brief: ContentBrief
    variants: int = Field(default=1, ge=1, le=5)


class ContentVariant(BaseModel):
    id: str
    body: str
    hashtags: Optional[List[str]] = None
    cta: Optional[str] = None
    character_count: int
    meta_description: Optional[str] = None
    title_tag: Optional[str] = None
    headline_1: Optional[str] = None
    headline_2: Optional[str] = None


class ContentResponse(BaseModel):
    content_type: str
    platform: str
    variants: List[ContentVariant]
    tokens_used: int
    generated_at: datetime
    plan_used: bool = False


# ── Growth Plan ────────────────────────────────────────────────────────────

class GrowthPlan(BaseModel):
    niche: Optional[str] = None
    growth_objective: Optional[str] = None
    target_audience: Optional[str] = None
    tone: Optional[str] = None
    platforms: List[str] = Field(default_factory=list)
