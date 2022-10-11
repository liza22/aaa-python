from typing import Callable

INPUT_CSV_PATH = 'Corp_Summary.csv'


def print_hierarchy(csv_path: str) -> None:
    """
    Принимает путь к файлу с данными.
    Печатает иерархию департаментов, т.е. департамент и все команды, которые входят в него.
    """
    hierarchy = {}
    with open(csv_path, encoding="utf8") as csvfile:
        next(csvfile)
        for row in csvfile:
            row = row.split(';')
            if row[1] in hierarchy:
                hierarchy[row[1]].add(row[2])
            else:
                hierarchy[row[1]] = set()

    for department, teams in hierarchy.items():
        print(department + ':')
        for team in teams:
            print('---', team)


def compute_statistics(input_csv: str) -> list[list[str]]:
    """Вспомогательная функция подсчета сводного отчета"""
    dep_salaries = {}
    with open(input_csv, encoding="utf8") as csvfile:
        next(csvfile)
        for row in csvfile:
            row = row.split(';')
            if row[1] in dep_salaries:
                dep_salaries[row[1]].append(int(row[-1]))
            else:
                dep_salaries[row[1]] = [int(row[-1])]

    header = ['Департамент', 'Численность', 'Вилка', 'Средняя зарплата']
    return [header] + \
           [[str(department), str(len(salaries)), f"{min(salaries)} - {max(salaries)}",
             str(sum(salaries) / float(len(salaries)))] for department, salaries in dep_salaries.items()]


def print_statistics(input_csv: str) -> None:
    """
        Принимает путь к файлу с данными.
        Печатает сводный отчёт по департаментам:
        название, численность, "вилка" зарплат в виде мин – макс, средняя зарплата.
    """
    stat = compute_statistics(input_csv)
    for row in stat:
        print("{:>12} {:>12} {:>20} {:>20}".format(*row))


def save_statistics(input_csv: str) -> None:
    """
        Принимает путь к файлу с данными.
        Сохраняет сводный отчёт по департаментам в файл statistics.csv:
        название, численность, "вилка" зарплат в виде мин – макс, средняя зарплата.
    """
    stat = compute_statistics(input_csv)
    with open('statistics.csv', encoding="utf8", mode='w') as csvfile:
        for row in stat:
            csvfile.write(';'.join(row) + '\n')


def print_menu() -> Callable[[str], None]:
    """Печатает меню выбора функций. Возвращает выбранную функцию."""
    command = ''
    commands = {'1': 'Вывести иерархию команд', '2': 'Вывести сводный отчёт', '3': 'Сохранить сводный отчёт'}
    functions = {'1': print_hierarchy, '2': print_statistics, '3': save_statistics}
    while command not in commands:
        print('Выберите команду из списка:')
        commands_list = list(map(lambda x: f"{x[0]}. {x[1]}", commands.items()))
        print('\n'.join(commands_list))
        command = input()
    return functions[command]


if __name__ == '__main__':
    func_to_execute = print_menu()
    func_to_execute(INPUT_CSV_PATH)
