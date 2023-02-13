import csv


def read_log(path):
    try:
        with open(path, 'r') as file:
            read = csv.reader(file)
            return list(read)
    except FileNotFoundError:
        if not path.endswith('.csv'):
            raise FileNotFoundError(f"Extensão inválida: '{path}'")

        raise FileNotFoundError(f"Arquivo inexistente: '{path}'")


def write_campaign(path, data):
    with open(path, 'w') as file:
        file.write(data)


def analyze_log(path_to_file):
    log_rows = read_log(path_to_file)

    client_data = {}
    food_counts = {}
    day_counts = {}

    for row in log_rows:
        client = row[0]
        food = row[1]
        day = row[2]

        client_data.setdefault(client, {'orders': {}, 'days': set()})
        client_orders = client_data[client]

        food_count = client_orders['orders'].get(food, 0)
        food_count += 1
        client_orders['orders'][food] = food_count

        client_orders['days'].add(day)

        food_counts[food] = food_counts.get(food, 0) + 1
        day_counts[day] = day_counts.get(day, 0) + 1

    orders = client_data['maria']['orders']
    max_food_for_maria = max(orders, key=orders.get)

    arnaldo_orders = client_data['arnaldo']['orders']
    arnaldo_hamburguer_orders = arnaldo_orders.get('hamburguer', 0)

    joao_orders = set(client_data['joao']['orders'].keys())
    foods_not_ordered_by_joao = set(food_counts.keys()) - joao_orders

    joao_days = set(client_data['joao']['days'])
    days_not_ordered_by_joao = set(day_counts.keys()) - joao_days

    output = (
        f"{max_food_for_maria}\n"
        f"{arnaldo_hamburguer_orders}\n"
        f"{foods_not_ordered_by_joao}\n"
        f"{days_not_ordered_by_joao}\n"
    )

    write_campaign('data/mkt_campaign.txt', output)
