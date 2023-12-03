from .user_recommend_models.random_model import RandomUserRecommendationsModel
from .team_recommend_models.random_model import RandomTeamRecommendationsModel
from .hack_recommend_models.random_model import RandomHackRecommendationsModel


user_user_model = RandomUserRecommendationsModel([0,1,2,3,4])

hack_user_model = RandomHackRecommendationsModel([0,1,2])

team_user_model = RandomTeamRecommendationsModel([0,1,2,3])

user_team_model = RandomUserRecommendationsModel([0,1,2,3,4])