from data_structures.habitant_data import HabitantData


class HabitantDTO(HabitantData):
    def __init__(self, name, job, salary, balance):
        super().__init__(name, job, salary, balance)
