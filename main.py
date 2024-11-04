from db.sqlite_gateway import SqliteHabitantGateway
from use_cases.TransactionsWithTwoHabitantsUseCase import TransactionWithTwoHabitantsUseCase
from use_cases.CreateNewHabitantUseCase import CreateNewHabitantUseCase
from use_cases.GetAllHabitantsUseCase import GetAllHabitantsUseCase
from use_cases.GetHabitantByIdUseCase import GetHabitantByIdUseCase
from use_cases.GiveSalariesToAllHabitantsUseCase import GiveSalariesToAllHabitantsUseCase


if __name__ == '__main__':
    sqlite_gateway = SqliteHabitantGateway()

    create_new = CreateNewHabitantUseCase(sqlite_gateway)

    # name = input('Введите имя нового жителя: ')
    # job = input('Введите работу нового жителя: ')
    # salary = int(input('Введите зарплату нового жителя: '))

    # create_new.run(HabitantDTO(name, job, salary, 0))

    give_salaries = GiveSalariesToAllHabitantsUseCase(sqlite_gateway)

    # give_salaries.run()

    transaction = TransactionWithTwoHabitantsUseCase(sqlite_gateway)

    transaction.run(4, 1, 12000)

    get_all = GetAllHabitantsUseCase(sqlite_gateway)

    all = get_all.run()

    if all.is_success():
        for i in all.get_response():
            print(i)
    else:
        print(all.get_response())

    ident = int(input('Введите ID жителя, которого хотите получить: '))

    get_by_id = GetHabitantByIdUseCase(sqlite_gateway)

    by_id = get_by_id.run(ident)

    print(by_id.get_response())
