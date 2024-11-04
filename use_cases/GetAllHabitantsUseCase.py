from use_cases.BaseHabitantUseCase import BaseHabitantUseCase
from use_cases.UseCaseResponse import UseCaseResponse


class GetAllHabitantsUseCase(BaseHabitantUseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

    def run(self) -> UseCaseResponse:
        return UseCaseResponse(self._gateway.get_all())
