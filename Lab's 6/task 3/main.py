import xml.etree.ElementTree as ET

file_path = 'ex_3.xml'
tree = ET.parse(file_path)
root = tree.getroot()

goods_data = []
for item in root.findall(".//ТаблСчФакт/СведТов"):
    name = item.get("НаимТов")  # Название товара
    quantity = item.get("КолТов")  # Количество товара
    price = item.get("ЦенаТов")  # Цена товара
    goods_data.append({"Товар": name, "Количество": quantity, "Цена": price})

print("Товары, их количество и цена:")
for good in goods_data:
    print(f"Товар: {good['Товар']}, Количество: {good['Количество']}, Цена: {good['Цена']}")