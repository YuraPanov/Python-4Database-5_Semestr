import openpyxl
from openpyxl import Workbook


# Функция для расчета итогов
def calculate_totals(data):
    totals = {
        "grand_total1": 0,
        "grand_total2": 0,
        "grand_total3": 0,
        "grand_total4": 0,
        "grand_total5": 0
    }

    for occupation in data:
        occupation_name = ""
        occupation_totals = {"total1": 0, "total2": 0, "total3": 0, "total4": 0, "total5": 0}

        for entry in occupation:
            occupation_name = entry['Отдел']

            # Округляем данные
            entry['Сумма по окладу, руб.'] = round(entry['Сумма по окладу, руб.'], 2)
            entry['Сумма по надбавкам, руб.'] = round(entry['Сумма по надбавкам, руб.'], 2)

            # Расчеты
            entry['Сумма зарплаты, руб.'] = round(entry['Сумма по окладу, руб.'] + entry['Сумма по надбавкам, руб.'], 2)
            entry['НДФЛ, %'] = 13
            entry['Сумма НДФЛ, %'] = round(entry['Сумма зарплаты, руб.'] * entry['НДФЛ, %'] / 100, 2)
            entry['Сумма к выдаче, руб.'] = round(entry['Сумма зарплаты, руб.'] - entry['Сумма НДФЛ, %'], 2)

            # Обновляем текущие итоги отдела
            occupation_totals["total1"] += entry['Сумма по окладу, руб.']
            occupation_totals["total2"] += entry['Сумма по надбавкам, руб.']
            occupation_totals["total3"] += entry['Сумма зарплаты, руб.']
            occupation_totals["total4"] += entry['Сумма НДФЛ, %']
            occupation_totals["total5"] += entry['Сумма к выдаче, руб.']

            # Записываем данные в лист
            sheet.append(list(entry.values()))

        # Добавляем итоги отдела
        sheet.append(["", "", f"{occupation_name} Итог",
                      round(occupation_totals["total1"], 2),
                      round(occupation_totals["total2"], 2),
                      round(occupation_totals["total3"], 2),
                      "",
                      round(occupation_totals["total4"], 2),
                      round(occupation_totals["total5"], 2)])

        # Обновляем общие итоги
        for key in totals.keys():
            occupation_key = key.replace("grand_", "")  # Преобразуем ключ к виду "total1", "total2" и т.д.
            totals[key] += occupation_totals[occupation_key]  # Правильный доступ к значению

    return totals


# Исходные данные
data = [
    [
        {"Таб. номер": "0002", "ФИО": "Петров П.П.", "Отдел": "Бухгалтерия", "Сумма по окладу, руб.": 3913.04, "Сумма по надбавкам, руб.": 2608.7},
        {"Таб. номер": "0005", "ФИО": "Васин В.В.", "Отдел": "Бухгалтерия", "Сумма по окладу, руб.": 5934.78, "Сумма по надбавкам, руб.": 913.04}
    ],
    [
        {"Таб. номер": "0001", "ФИО": "Иванов И.И.", "Отдел": "Отдел кадров", "Сумма по окладу, руб.": 6000.0, "Сумма по надбавкам, руб.": 4000.0},
        {"Таб. номер": "0003", "ФИО": "Сидоров С.С.", "Отдел": "Отдел кадров", "Сумма по окладу, руб.": 5000.0, "Сумма по надбавкам, руб.": 4500.0},
        {"Таб. номер": "0006", "ФИО": "Львов Л.Л.", "Отдел": "Отдел кадров", "Сумма по окладу, руб.": 4074.07, "Сумма по надбавкам, руб.": 2444.44},
        {"Таб. номер": "0007", "ФИО": "Волков В.В.", "Отдел": "Отдел кадров", "Сумма по окладу, руб.": 1434.78, "Сумма по надбавкам, руб.": 1434.78}
    ],
    [
        {"Таб. номер": "0004", "ФИО": "Мишин М.М.", "Отдел": "Столовая", "Сумма по окладу, руб.": 5500.0, "Сумма по надбавкам, руб.": 3500.0}
    ]
]

# Создаем книгу и лист
wb = Workbook()
sheet = wb.active
sheet.title = "Зарплаты"

# Заголовки
columns = [
    "Таб. номер", "ФИО", "Отдел", "Сумма по окладу, руб.",
    "Сумма по надбавкам, руб.", "Сумма зарплаты, руб.",
    "НДФЛ, %", "Сумма НДФЛ, %", "Сумма к выдаче, руб."
]
sheet.append(columns)

# Вычисление данных и итогов
totals = calculate_totals(data)

# Добавляем общий итог
sheet.append(["", "", "Общий итог",
              round(totals["grand_total1"], 2),
              round(totals["grand_total2"], 2),
              round(totals["grand_total3"], 2),
              "",
              round(totals["grand_total4"], 2),
              round(totals["grand_total5"], 2)])

# Сохраняем файл
wb.save("table.xlsx")
print("Таблица успешно сохранена в 'salaries.xlsx'")
