import random

from typing import List
from models.base_model import AbstractRecommendsModel


class RandomUserRecommendationsModel(AbstractRecommendsModel):
    """"""

    def __init__(self, id_to_recommend: List[int]) -> None:
        self.id_to_recommend = id_to_recommend

    def get_recommends(self, entity_id: int, k_recs: int = 1, *args, **kwargs) -> List[int]:
        return random.sample(self.id_to_recommend, k = k_recs)
    
    @staticmethod
    def get_reason():
        reasons = ["Он знает, где находится самое вкусное место для пиццы в параллельной вселенной.",
                   "Он может поделиться секретами о том, как обучить своего кота играть в шахматы.",
                   "Он имеет коллекцию самых необычных носков, которые вы когда-либо видели.",
                   "Он оказался родственником дальнего кузена дракона.",
                   "Он умеет читать мысли черепах и уток в парке.",
                   "Он знает, как использовать только три слова для убедительной речи о важности снаряжения пингвина.",
                   "Он имеет сверхъестественный талант делать самые весёлые фотографии с котятами.",
                   "Он владеет уникальным рецептом борща, в котором секрет крылышек ангелов.",
                   "Он может провести вас по лабиринтам безумных историй из детства енотов-героев.",
                   "Он знает, как заставить мух петь оперу и утверждает, что это - искусство.",
                   "Он может рассказать самые увлекательные истории о приключениях своего плюшевого медведя.",
                   "Он имеет диплом по общению с драконами и готов поделиться своими навыками.",
                   "Он умеет играть на банановой гитаре и показывать, как сделать это стильно.",
                   "Он изучал древний язык единорогов и может научить, как не обидеть их своими шутками.",
                   "Он знает, как разговаривать с облаками и узнавать их самые громкие тайны.",
                   "Он имеет карту сокровищ сокровищницы, где спрятаны сокровища из фейерверков.",
                   "Он может научить вас искусству печатать на клавишах пианино пальцами, покрытыми магией.",
                   "Он умеет уговаривать лисичек делиться своими сокровищами.",
                   "Он знает, как превратить самый обычный день в увлекательное приключение с карандашом и ниткой.",
                   "Он имеет сверхспособность различать аномальные смехи и дарит всем вокруг дозу веселья."
                   ]
        
        return random.sample(reasons, k=1)[0]