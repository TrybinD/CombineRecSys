from typing import Optional

from pydantic import BaseModel


class UserRecommendedResponse(BaseModel):
    user_id: int
    model_id: int
    reason: Optional[str] = None


class HackRecommendedResponse(BaseModel):
    hack_id: int
    model_id: int
    reason: Optional[str] = None


class TeamRecommendedResponse(BaseModel):
    team_id: int
    model_id: int
    reason: Optional[str] = None