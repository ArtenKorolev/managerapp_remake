from use_cases.BaseHabitantUseCase import BaseHabitantUseCase
from use_cases.UseCaseResponse import UseCaseResponse


class CreateNewHabitantUseCase(BaseHabitantUseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

    def run(self, habitant_dto) -> UseCaseResponse:
        response = UseCaseResponse(self._gateway.create(habitant_dto))
        return response
