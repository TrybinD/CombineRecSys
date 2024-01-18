from pathlib import Path
from typing import List

from models import AbstractRecommendsModel
from service.utils.schemas import TeamRecommendedResponse

class TeamUserRecommendationService:
    def __init__(self, model: AbstractRecommendsModel) -> None:
        self.model = model

    async def get_team_user_recommendation(self, user_id: int, k_recs: int = 1) -> List[TeamRecommendedResponse]:

        recos_id = self.model.get_recommends(user_id, k_recs=k_recs)

        res = []

        for rec_id in recos_id:
            res.append(TeamRecommendedResponse(user_id=rec_id,
                                               model_id=0,
                                               reason=self.model.get_reason()))
        
        return res

user_model = AbstractRecommendsModel.load(Path("models/random_team_model.pkl")) # Hardcode

def team_user_recommendation_service():
    return TeamUserRecommendationService(user_model)