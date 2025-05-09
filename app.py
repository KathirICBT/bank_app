import os

def get_customer_info():
    name = input('Enter the customer name: ')
    address = input('Enter the customer address: ')
    username = input('Enter the customer username: ')
    password = input('Enter the customer password: ')
    return [name, address, username, password]

def create_next_customer_id():
    if not os.path.exists('customers.txt'):
        return 'C001'
    else:
        with open('customers.txt', 'r') as cus_file:
            return f"C{int(cus_file.readlines()[-1].split(',')[0][1:]) + 1:03d}"

def create_customer():
    customer = get_customer_info()
    next_id = create_next_customer_id()
    with open('customers.txt', 'a') as customer_file, open('users.txt', 'a') as user_file:
        customer_file.write(f"{next_id},{customer[0]},{customer[1]}\n")
        user_file.write(f"{customer[2]},{customer[3]}\n")

def view_all_customer():
    with open('customers.txt', 'r') as cus_file:
        print(cus_file.read())

def main():
    print("1. Create Customer")
    print("2. View all Customers")
    ch = int(input('Enter number: '))
    if ch == 1:
        create_customer()
    elif ch == 2:
        view_all_customer()
    else:
        print('Invalid Input!')

main()
