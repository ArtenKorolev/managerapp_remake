from exceptions.ObjectDoesNotExist import ObjectDoesNotExist
from use_cases.BaseHabitantUseCase import BaseHabitantUseCase
from use_cases.UseCaseResponse import UseCaseResponse


class GetHabitantByIdUseCase(BaseHabitantUseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

    def run(self, habitant_id) -> UseCaseResponse:
        try:
            habitant = self._gateway.get_by_id(habitant_id)
            return UseCaseResponse(habitant)
        except ObjectDoesNotExist as exc:
            return UseCaseResponse(exc.what())
    