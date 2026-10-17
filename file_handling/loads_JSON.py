import json

data = '{"Laptop": "HP", "Price": "45000", "In_stock": "True"}'

company = json.loads(data)
print(company)
print(f"લેપટોપ નામ {company['Laptop']} અને પ્રાઇસ {company['Price']}")