import json

input_file = "ex_3.json"
output_file = "ex_3_modified.json"

with open(input_file, "r") as f:
    data = json.load(f)

new_invoice = {
    "id": 3,
    "total": 150.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 1,
            "price": 100.00
        },
        {
            "name": "item 5",
            "quantity": 2,
            "price": 25.00
        }
    ]
}

data["invoices"].append(new_invoice)

with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

