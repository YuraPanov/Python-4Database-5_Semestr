import xml.etree.ElementTree as ET


tree = ET.parse('ex_2.xml')
root = tree.getroot()


new_item = ET.Element("Item")
ET.SubElement(new_item, "ArtName").text = "Сыр Камамбер"
ET.SubElement(new_item, "Barcode").text = "2000000000151"
ET.SubElement(new_item, "QNT").text = "300"
ET.SubElement(new_item, "QNTPack").text = "300"
ET.SubElement(new_item, "Unit").text = "шт"
ET.SubElement(new_item, "SN1").text = "00000015"
ET.SubElement(new_item, "SN2").text = "22.11.2024"
ET.SubElement(new_item, "QNTRows").text = "20"

root.find("Detail").append(new_item)
ET.indent(tree, '    ')

total_qnt = sum(float(item.find("QNT").text.replace(",", ".")) for item in root.find("Detail").findall("Item"))
total_rows = sum(int(item.find("QNTRows").text) for item in root.find("Detail").findall("Item"))

summary = root.find("Summary")
summary.find("Summ").text = f"{total_qnt:.2f}".replace(".", ",")
summary.find("SummRows").text = str(total_rows)


tree.write('ex_2_update.xml', encoding="UTF-8", xml_declaration=True)

