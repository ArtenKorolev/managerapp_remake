from exceptions.ObjectDoesNotExist import ObjectDoesNotExist
from use_cases.BaseHabitantUseCase import BaseHabitantUseCase
from use_cases.UseCaseResponse import UseCaseResponse


class DeleteHabitantUseCase(BaseHabitantUseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

    def run(self, habitant_id) -> UseCaseResponse:
        try:
            return UseCaseResponse(self._gateway.delete(habitant_id))
        except ObjectDoesNotExist as exc:
            return UseCaseResponse(exc.what())
