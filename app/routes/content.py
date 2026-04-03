from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.schemas.content import ContentRequest, ContentResponse, GrowthPlan
from app.services.content_service import ContentService
from app.services.plan_service import get_plan, save_plan

router = APIRouter(prefix="/api/content", tags=["content"])
_service = ContentService()


# ── Growth plan endpoints ──────────────────────────────────────────────────

@router.get("/plan", response_model=dict)
def get_growth_plan() -> dict:
    return get_plan()


@router.post("/plan", response_model=dict)
def update_growth_plan(plan: GrowthPlan) -> dict:
    return save_plan(plan.model_dump(exclude_none=True))


# ── Content generation ─────────────────────────────────────────────────────

@router.post("/generate", response_model=ContentResponse)
async def generate_content(request: ContentRequest) -> ContentResponse:
    # Fetch saved growth plan — empty dict if none saved yet
    plan = get_plan()

    try:
        return await _service.generate(request, plan=plan)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(exc)) from exc
