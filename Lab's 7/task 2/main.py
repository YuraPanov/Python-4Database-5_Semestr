import json

input_file_path = 'ex_2.json'
formatted_file_path = 'ex_2_formatted.json'

# Приведение JSON к читаемому виду
with open(input_file_path, 'r') as file:
    raw_data = file.read()
    # Поправляем некорректный JSON, если данные записаны как массив объектов
    if not raw_data.strip().startswith('['):
        raw_data = '[' + raw_data + ']'
    data = json.loads(raw_data)  # Загружаем данные как JSON

# Сохраняем
with open(formatted_file_path, 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

# Извлечение имен пользователей и телефонов
user_dict = {user["name"]: user["phoneNumber"] for user in data}

print(formatted_file_path, user_dict)
