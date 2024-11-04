from sqlite3 import connect
from entities.habitant import Habitant
from exceptions.ObjectDoesNotExist import ObjectDoesNotExist
from gateways.habitant_gateway import HabitantGateway
from dtos.habitant_dto import HabitantDTO
from settings import settings


class SqliteHabitantGateway(HabitantGateway):
    def __init__(self):
        self.__connection = connect(settings.db_name)

    def create(self, dto):
        cursor = self.__connection.cursor()

        cursor.execute(f"""
        insert into habitant(name, job, salary, balance)
        values({self.__add_quotes_if_string(dto.name)}, 
        {self.__add_quotes_if_string(dto.job)}, 
        {dto.salary},
        {dto.balance})
        """)

        self.__connection.commit()

    def __add_quotes_if_string(self, value):
        if type(value) == str:
            return f"'{value}'"
        return str(value)

    def delete(self, habitant_id):
        try:
            habitant = self._get_by_id(habitant_id)
            self.__try_to_delete(habitant_id)
            return habitant
        except Exception:
            raise ObjectDoesNotExist(f'Habitant with id: {habitant_id} does not exist.')

    def __try_to_delete(self, habitant_id):
        cursor = self.__connection.cursor()

        cursor.execute(f"""
        delete from habitant
        where id = {habitant_id}
        """)

        self.__connection.commit()

    def get_by_id(self, habitant_id):
        try:
            return self.__try_to_get_by_id(habitant_id)
        except Exception:
            raise ObjectDoesNotExist(f'Habitant with id: {habitant_id} does not exist.')
    
    def __try_to_get_by_id(self, habitant_id):
        cursor = self.__connection.cursor()

        cursor.execute(f"""
        select * 
        from habitant
        where id = {habitant_id}
        """)

        habitant = cursor.fetchone()

        self.__connection.commit()

        return self.__get_habitant_entity_by_tuple(habitant)

    def __get_habitant_entity_by_tuple(self, habitant_tuple):
        habitant_id = habitant_tuple[0]
        habitant_data = HabitantDTO(habitant_tuple[1], habitant_tuple[2], habitant_tuple[3], habitant_tuple[4])
        
        return Habitant(habitant_id, habitant_data)

    def update(self, habitant_id, dto):
        cursor = self.__connection.cursor()

        cursor.execute(f"""
        update habitant
        set name = {self.__add_quotes_if_string(dto.name)},
        job = {self.__add_quotes_if_string(dto.job)},
        salary = {dto.salary},
        balance = {dto.balance}
        where id = {habitant_id}
        """)

        self.__connection.commit()

    def get_all(self):
        cursor = self.__connection.cursor()

        cursor.execute(f"""
        select * 
        from habitant
        """)

        habitants = cursor.fetchall()

        self.__connection.commit()

        return [self.__get_habitant_entity_by_tuple(i) for i in habitants]
