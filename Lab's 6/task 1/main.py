from xmlschema import XMLSchema



 # Укажите пути к файлам XML и XSD
xsd_file = "schema.xsd"
xml_file = "ex_1.xml"

try:
    schema = XMLSchema(xsd_file)
    if schema.is_valid(xml_file):
        print("This XML file is valid.")
    else:
        print("This XML file is not valid.")
except Exception as e:
    print(f"An error occurred: {e}")