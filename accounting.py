MELON_COST = 1.00

def print_accounting(payments):
    orders = open(payments)

    for line in orders:
        line = line.rstrip()
        words = line.split("|")
        customer_number = words[0]
        customer_name = words[1]
        melon_quantity = float(words[2])
        price_paid = float(words[3])
        customer_expected = melon_quantity * MELON_COST

        print(f"{customer_name} paid {price_paid}, expected {customer_expected}.")

        if price_paid < customer_expected:
            print(f"{customer_name} underpaid for their melons.")
        elif price_paid > customer_expected:
            print(f"{customer_name} overpaid for their melons.")

    orders.close()            
print_accounting("customer-orders.txt")
