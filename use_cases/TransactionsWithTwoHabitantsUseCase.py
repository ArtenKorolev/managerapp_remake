from exceptions.ObjectDoesNotExist import ObjectDoesNotExist
from use_cases.BaseHabitantUseCase import BaseHabitantUseCase
from use_cases.UseCaseResponse import UseCaseResponse


class TransactionWithTwoHabitantsUseCase(BaseHabitantUseCase):
    def __init__(self, gateway):
        super().__init__(gateway)

    def run(self, first_id, second_id, value) -> UseCaseResponse:
        try:
            first_habitant = self._gateway.get_by_id(first_id)
            second_habitant = self._gateway.get_by_id(second_id)
        except ObjectDoesNotExist as exc:
            return UseCaseResponse(exc.what())

        first_habitant.write_off_money(value)
        second_habitant.add_money(value)

        self._gateway.update(first_id, first_habitant.get_ds())
        self._gateway.update(second_id, second_habitant.get_ds())
        
        updated_habitants = [first_habitant, second_habitant]

        return UseCaseResponse(updated_habitants)
    