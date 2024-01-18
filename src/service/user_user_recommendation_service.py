from pathlib import Path
from typing import List

from models import AbstractRecommendsModel
from service.utils.schemas import UserRecommendedResponse

class UserUserRecommendationService:
    def __init__(self, model: AbstractRecommendsModel) -> None:
        self.model = model

    async def get_user_user_recommendation(self, user_id: int, k_recs: int = 1) -> List[UserRecommendedResponse]:

        recos_id = self.model.get_recommends(user_id, k_recs=k_recs)

        res = []

        for rec_id in recos_id:
            res.append(UserRecommendedResponse(user_id=rec_id,
                                               model_id=0,
                                               reason=self.model.get_reason()))
        
        return res

user_model = AbstractRecommendsModel.load(Path("models/random_user_model.pkl")) # Hardcode

def user_user_recommendation_service():
    return UserUserRecommendationService(user_model)