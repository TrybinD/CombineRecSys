import random

from typing import List
from models.base_model import AbstractRecommendsModel


class RandomTeamRecommendationsModel(AbstractRecommendsModel):
    """"""

    def __init__(self, id_to_recommend: List[int]) -> None:
        self.id_to_recommend = id_to_recommend

    def get_recommends(self, user_id: int, k_recs: int = 1, *args, **kwargs) -> List[int]:
        return random.sample(self.id_to_recommend, k = k_recs)
    
    @staticmethod
    def get_reason():
        reasons = [
                    "У нас есть тайный рецепт пиццы, который вдохновляет на кодинг.",
                    "Мы используем бессмертных единорогов в качестве технической поддержки.",
                    "У нас есть кот-хакер, который программирует на Python и кофеине.",
                    "В команде есть танцующий робот, который дарит идеи на каждом шагу.",
                    "Мы используем язык программирования, который создан специально для хакатонов.",
                    "У нас в команде специалист по переводу кода на человеческий язык.",
                    "Мы знаем, как использовать кибернетических попугаев для тестирования безопасности.",
                    "В нашей команде есть маг-дизайнер, который создаёт интерфейсы из будущего.",
                    "Мы работаем в симбиозе с AI, который предсказывает будущее кода.",
                    "У нас есть рабочий хакерский чайник, который готовит лучший кодинг-чай.",
                    "Мы проводим совещания на космической станции внутри виртуальной реальности.",
                    "В команде есть профессиональный чародей, превращающий баги в фокусы.",
                    "Мы используем роботов-поваров, чтобы поддерживать уровень энергии во время хакатона.",
                    "У нас есть специалист по фен-шую кода, чтобы каждая строчка приносила гармонию.",
                    "Мы разработали секретный язык программирования на основе мемов.",
                    "У нас в команде робот-джедай, который использует Силу для улучшения кода.",
                    "Мы устраиваем космические квесты по поиску утерянных точек с запятой.",
                    "У нас есть член команды, который может писать код, пользуясь только мысленной силой.",
                    "Мы используем симбиоз квантовых компьютеров и пушистых котиков для решения сложных задач.",
                    "У нас в команде робот-мотиватор, который поддерживает дух коллектива на высоте."
                ]
        return random.sample(reasons, k=1)[0]