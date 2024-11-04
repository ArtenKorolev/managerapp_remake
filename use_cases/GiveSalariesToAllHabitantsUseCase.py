from use_cases.BaseHabitantUseCase import BaseHabitantUseCase
from use_cases.UseCaseResponse import UseCaseResponse


class GiveSalariesToAllHabitantsUseCase(BaseHabitantUseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

    def run(self) -> UseCaseResponse:
        all_habitants = self._gateway.get_all()

        updated_habitants = []

        for i in all_habitants:
            i.charge_salary()
            updated_habitants.append(self._gateway.update(i.get_id(), i.get_ds()))

        return UseCaseResponse(updated_habitants)
