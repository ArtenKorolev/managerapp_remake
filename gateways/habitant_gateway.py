from abc import ABC, abstractmethod
from entities.habitant import Habitant


class HabitantGateway(ABC):
    @abstractmethod
    def create(self, habitant_dto) -> Habitant:
        pass

    @abstractmethod
    def delete(self, habitant_id) -> Habitant:
        pass
 
    @abstractmethod
    def get_all(self) -> list[Habitant]:
        pass

    @abstractmethod
    def get_by_id(self, habitant_id) -> Habitant:
        pass

    @abstractmethod
    def update(self, habitant_id, habitant_dto) -> Habitant:
        pass
