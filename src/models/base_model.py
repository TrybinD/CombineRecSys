from abc import ABC, abstractmethod
from typing import List
from pathlib import Path
import pickle


class AbstractRecommendsModel(ABC):
    __instances_dict = {}
    
    @abstractmethod
    def get_recommends(self, *args, **kwargs) -> List[int]:
        raise NotImplementedError
    
    def save(self, filename: Path) -> None:
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, filename: Path) -> 'AbstractRecommendsModel':
        if filename not in cls.__instances_dict:
            with open(filename, "rb") as file:
                cls.__instances_dict[filename] = pickle.load(file)

        return cls.__instances_dict[filename]
    
    @staticmethod
    def get_reason():
        return "Мы сделали эту рекомендацию на основе магии ИИ ✨"

