import openpyxl


def calculate_average(values):
    total = sum(values)
    return round(total / len(values), 2)


def get_worker_data(sheet, rows):
    return [sheet[f'A{row}:I{row}'][0] for row in rows]


def print_salary_info(workers):
    max_salary_worker = max(workers, key=lambda x: x[8].value)
    print(f"Наибольшая зп: {max_salary_worker[8].value} - {max_salary_worker[1].value}")

    min_salary_worker = min(workers, key=lambda x: x[8].value)
    print(f"Наименьшая зп: {min_salary_worker[8].value} - {min_salary_worker[1].value}")


wb = openpyxl.load_workbook("table.xlsx")

sheet = wb.active

# Получение данных работников по строкам

worker_rows = [2, 3, 5, 6, 7, 8, 10]
workers = get_worker_data(sheet, worker_rows)

print_salary_info(workers)

print(f"Средняя зп в бухгалтерии: {calculate_average([workers[0][8].value, workers[1][8].value])}")
print(
    f"Средняя зп в отделе кадров: {calculate_average([workers[2][8].value, workers[3][8].value, workers[4][8].value, workers[5][8].value])}")
print(f"Средняя зп в бухгалтерии: {calculate_average([workers[6][8].value])}")
