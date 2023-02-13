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
        
        client_orders = client_data.setdefault(client, {'orders': {}, 'days': set()})
        client_orders['orders'][food] = client_orders['orders'].get(food, 0) + 1
        client_orders['days'].add(day)
        
        food_counts[food] = food_counts.get(food, 0) + 1
        day_counts[day] = day_counts.get(day, 0) + 1
        
    max_food_for_maria = max(client_data['maria']['orders'], key=client_data['maria']['orders'].get)
    arnaldo_hamburguer_orders = client_data['arnaldo']['orders'].get('hamburguer', 0)
    foods_not_ordered_by_joao = set(food_counts.keys()) - set(client_data['joao']['orders'].keys())
    days_not_ordered_by_joao = set(day_counts.keys()) - set(client_data['joao']['days'])
    
    output = (
        f"{max_food_for_maria}\n"
        f"{arnaldo_hamburguer_orders}\n"
        f"{foods_not_ordered_by_joao}\n"
        f"{days_not_ordered_by_joao}\n"
    )
    
    write_campaign('data/mkt_campaign.txt', output)
