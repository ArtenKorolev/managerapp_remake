from abc import ABC

from gateways.habitant_gateway import HabitantGateway


class BaseHabitantUseCase(ABC):
    def __init__(self, gateway: HabitantGateway):
        self._gateway = gateway