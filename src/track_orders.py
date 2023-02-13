from collections import defaultdict


class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.days = defaultdict(set)

    def __len__(self):
        return sum(len(v) for v in self.orders.values())

    def add_new_order(self, customer, order, day):
        if customer not in self.orders:
            self.orders[customer] = defaultdict(int)
        self.orders[customer][order] += 1
        self.days[customer].add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        if customer not in self.orders:
            return None
        return max(self.orders[customer], key=self.orders[customer].get)

    def get_never_ordered_per_customer(self, customer):
        orders = []
        for customer_orders in self.orders.values():
            for order in customer_orders:
                orders.append(order)
        all_orders_list = orders
        all_orders = set(all_orders_list)

        customer_orders = set(self.orders.get(customer, []))
        return all_orders - customer_orders

    def get_days_never_visited_per_customer(self, customer):
        days = []
        for customer_days in self.days.values():
            for day in customer_days:
                days.append(day)
        all_days = set(days)
        customer_days = set(self.days.get(customer, []))
        return all_days - customer_days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
