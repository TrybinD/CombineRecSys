import random

from typing import List
from models.base_model import AbstractRecommendsModel


class RandomHackRecommendationsModel(AbstractRecommendsModel):
    """"""

    def __init__(self, id_to_recommend: List[int]) -> None:
        self.id_to_recommend = id_to_recommend

    def get_recommends(self, hack_id: int, k_recs: int = 1, *args, **kwargs) -> List[int]:
        return random.sample(self.id_to_recommend, k = k_recs)
    
    @staticmethod
    def get_reason():
        reasons = [
                    "Научить своего робота готовить завтраки для всех участников.",
                    "Разработать космический интерфейс, управляемый пальцами ног.",
                    "Создать алгоритм, который предсказывает, кто первым закончит чашку кофе.",
                    "Программировать с помощью магии, извлеченной из плюшевых игрушек.",
                    "Изобрести язык программирования, использующий только эмодзи.",
                    "Обучить робота переводить код на язык котят и щенят.",
                    "Разработать приложение, которое оценивает уровень счастья по стилю написания кода.",
                    "Создать программу, которая автоматически добавляет котиков во все комментарии в коде.",
                    "Изучить, как программировать на языке, который понимают только панды.",
                    "Разработать робота-барабанщика, который сопровождает каждый успешный билд.",
                    "Создать приложение, предсказывающее, когда забытая запятая приведет к катастрофе.",
                    "Обучить искусственный интеллект различать кодовые шутки от обычных.",
                    "Разработать робота-художника, который создает абстрактные шедевры из багов.",
                    "Программировать с помощью танцев на столе, чтобы улучшить концентрацию.",
                    "Изобрести устройство, которое превращает сон в рабочий код.",
                    "Разработать алгоритм, который автоматически добавляет случайные котятки в презентации.",
                    "Создать приложение для обмена энергией, генерируемой от бессмысленных кодовых блоков.",
                    "Обучить робота-комика шутить о багах без обид для разработчиков.",
                    "Разработать технологию, позволяющую программировать силой мысли о кофе.",
                    "Создать робота-диджея, который подбирает музыку под фазу разработки кода."
                    ]
        return "На этом хакатоне вы сможите" + random.sample(reasons, k=1)[0].lower()