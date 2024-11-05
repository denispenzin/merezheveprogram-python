import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://127.0.0.1:8000/items'
USERNAME = 'admin'  
PASSWORD = 'admin_pass'  

def get_items():
    response = requests.get(BASE_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        print("Items:", response.json())
    else:
        print("Error:", response.status_code, response.json())

def add_item(name, price, quantity):
    item_data = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    response = requests.post(BASE_URL, json=item_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 201:
        print("Item added:", response.json())
    else:
        print("Error:", response.status_code, response.json())

def update_item(item_id, name, price, quantity):
    item_data = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    response = requests.put(f"{BASE_URL}/{item_id}", json=item_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        print("Item updated:", response.json())
    else:
        print("Error:", response.status_code, response.json())

def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/{item_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        print("Item deleted:", response.json())
    else:
        print("Error:", response.status_code, response.json())

if __name__ == '__main__':
    get_items()  
    add_item("New Product", 100.0, 10)  
    update_item(1, "Updated Product", 120.0, 5)  
    delete_item(1)  
