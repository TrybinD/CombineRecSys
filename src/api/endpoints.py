from typing import List

from fastapi import APIRouter, Depends
from service.hack_user_recommendation_service import HackUserRecommendationService, hack_user_recommendation_service
from service.team_user_recommendation_service import TeamUserRecommendationService, team_user_recommendation_service
from service.user_team_recommendation_service import UserTeamRecommendationService, user_team_recommendation_service

from service.utils.schemas import UserRecommendedResponse, HackRecommendedResponse, TeamRecommendedResponse
from service.user_user_recommendation_service import UserUserRecommendationService, user_user_recommendation_service


router = APIRouter(prefix="/api/reco", tags=["reco"])

@router.get("/u2u/{user_id}")
async def get_user_user_recs(user_id: int, 
                             k_recs: int = 1, 
                             service: UserUserRecommendationService = Depends(user_user_recommendation_service)
                             ) -> List[UserRecommendedResponse]:
    
    responce = await service.get_user_user_recommendation(user_id=user_id, k_recs=k_recs)

    return responce


@router.get("/h2u/{user_id}")
async def get_hack_user_recs(user_id: int, 
                             k_recs: int = 1,
                             service: HackUserRecommendationService = Depends(hack_user_recommendation_service)
                             ) -> List[HackRecommendedResponse]:
    
    responce = await service.get_user_user_recommendation(user_id=user_id, k_recs=k_recs)

    return responce

@router.get("/t2u/{user_id}")
async def get_team_user_recs(user_id: int, 
                             k_recs: int = 1, 
                             service: TeamUserRecommendationService = Depends(team_user_recommendation_service)
                             ) -> List[TeamRecommendedResponse]:
    
    responce = await service.get_user_user_recommendation(user_id=user_id, k_recs=k_recs)

    return responce

@router.get("/u2t/{team_id}")
async def get_user_team_recs(team_id: int, 
                             k_recs: int = 1,
                             service: UserTeamRecommendationService = Depends(user_team_recommendation_service)
                             ) -> List[UserRecommendedResponse]:

    responce = await service.get_user_user_recommendation(user_id=team_id, k_recs=k_recs)

    return responce
