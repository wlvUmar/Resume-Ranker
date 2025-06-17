from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.ranker import ResumeRanker

router = APIRouter()
ranker = ResumeRanker()

class RankingRequest(BaseModel):
    job_description: str
    resumes: List[str]

class RankingResponse(BaseModel):
    ranked_results: List[dict]

@router.post("/rank", response_model=RankingResponse)
async def rank_resumes(request: RankingRequest):
    try:
        ranked_results = await ranker.rank_resumes(
            request.job_description,
            request.resumes
        )
        return RankingResponse(ranked_results=ranked_results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 