import json

# Загрузка данных из файла
with open("sample-data.json") as file:
    data = json.load(file)

# Вывод заголовка
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 80)

# Обработка и вывод данных
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")
    print(f"{dn:<50} {description:<20} {speed:<6} {mtu:<6}")
