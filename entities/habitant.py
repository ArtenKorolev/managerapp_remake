from data_structures.habitant_data import HabitantData


class Habitant:
    def __init__(self, ident, data: HabitantData):
        self.__ident = ident
        self.__data = data

    def change_job(self, new_job):
        self.__data.job = new_job

    def charge_salary(self):
        self.__data.balance += self.__data.salary

    def add_money(self, money_to_add):
        if money_to_add > 0:
            self.__data.balance += money_to_add
        
    def write_off_money(self, money_to_write_off):
        if money_to_write_off > 0 and self.__data.balance - money_to_write_off >= 0:
            self.__data.balance -= money_to_write_off

    def change_name(self, new_name):
        self.__data.name = new_name

    def raise_salary(self, value_to_raise):
        if value_to_raise > 0:
            self.__data.salary += value_to_raise

    def downgrade_salary(self, value_to_downgrade):
        if value_to_downgrade > 0 and self.__data.salary - value_to_downgrade >= 0:
            self.__data.salary -= value_to_downgrade

    def get_info(self):
        return f'ID: {self.__ident}, Имя: {self.__data.name}, Работа: {self.__data.job}, Зарплата: {self.__data.salary}, Баланс: {self.__data.balance}'

    def get_ds(self):
        return self.__data
    
    def get_id(self):
        return self.__ident
