from typing import List

from fastapi import FastAPI

from service.utils.schemas import UserRecommendedResponse, HackRecommendedResponse, TeamRecommendedResponse
from models import user_user_model, user_team_model, hack_user_model, team_user_model


app = FastAPI()

@app.get("/api/reco/u2u/{user_id}")
def get_user_user_recs(user_id: int, k_recs: int = 1) -> List[UserRecommendedResponse]:

    recos_id = user_user_model.get_recommends(user_id, k_recs=k_recs)

    res = []

    for rec_id in recos_id:
        res.append(UserRecommendedResponse(user_id=rec_id,
                                           model_id=0,
                                           reason=user_user_model.get_reason()))
        
    return res

@app.get("/api/reco/h2u/{user_id}")
def get_hack_user_recs(user_id: int, k_recs: int = 1) -> List[HackRecommendedResponse]:
    
    recos_id = hack_user_model.get_recommends(user_id, k_recs=k_recs)

    res = []

    for rec_id in recos_id:
        res.append(HackRecommendedResponse(hack_id=rec_id,
                                           model_id=0,
                                           reason=hack_user_model.get_reason()))
        
    return res

@app.get("/api/reco/t2u/{user_id}")
def get_team_user_recs(user_id: int, k_recs: int = 1) -> List[TeamRecommendedResponse]:
    
    recos_id = team_user_model.get_recommends(user_id, k_recs=k_recs)

    res = []

    for rec_id in recos_id:
        res.append(TeamRecommendedResponse(team_id=rec_id,
                                           model_id=0,
                                           reason=team_user_model.get_reason()))
        
    return res

@app.get("/api/reco/u2t/{team_id}")
def get_user_team_recs(team_id: int, k_recs: int = 1) -> List[UserRecommendedResponse]:

    recos_id = user_team_model.get_recommends(team_id, k_recs=k_recs)

    res = []

    for rec_id in recos_id:
        res.append(UserRecommendedResponse(user_id=rec_id,
                                           model_id=0,
                                           reason=user_team_model.get_reason()))
        
    return res
