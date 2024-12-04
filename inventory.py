# Online Store Simulation

# Sample product inventory
inventory = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 599.99},
    {"id": 3, "name": "Headphones", "price": 89.99},
]

# Shopping cart
cart = []

# Function to display available products
def display_products():
    print("\nAvailable Products:")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f}")
    print()

# Function to add items to the cart
def add_to_cart():
    try:
        product_id = int(input("Enter the Product ID to add to cart: "))
        quantity = int(input("Enter the quantity: "))
        
        if quantity <= 0:
            print("Quantity must be a positive number.")
            return
        
        for product in inventory:
            if product["id"] == product_id:
                for item in cart:
                    if item["id"] == product_id:
                        item["quantity"] += quantity
                        print(f"Updated {product['name']} quantity to {item['quantity']}.")
                        return
                cart.append({"id": product_id, "name": product["name"], "price": product["price"], "quantity": quantity})
                print(f"Added {quantity} {product['name']}(s) to the cart.")
                return
        
        print("Invalid Product ID.")
    except ValueError:
        print("Please enter valid numeric values for Product ID and Quantity.")

# Function to view the cart
def view_cart():
    if not cart:
        print("\nYour cart is empty.\n")
        return
    
    print("\nYour Cart:")
    total = 0
    for item in cart:
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"{item['name']} | Quantity: {item['quantity']} | Total: ${item_total:.2f}")
    print(f"Cart Total: ${total:.2f}\n")

# Function to remove items from the cart
def remove_from_cart():
    try:
        product_id = int(input("Enter the Product ID to remove from cart: "))
        
        for item in cart:
            if item["id"] == product_id:
                cart.remove(item)
                print(f"Removed {item['name']} from the cart.")
                return
        
        print("Product not found in the cart.")
    except ValueError:
        print("Please enter a valid numeric Product ID.")

# Function to complete the purchase
def complete_purchase():
    if not cart:
        print("\nYour cart is empty. Add items before checking out.\n")
        return
    
    total = sum(item["price"] * item["quantity"] for item in cart)
    print(f"\nTotal Amount: ${total:.2f}")
    confirm = input("Do you want to proceed with the purchase? (yes/no): ").lower()
    if confirm == "yes":
        print("Purchase successful! Thank you for shopping with us.\n")
        cart.clear()
    else:
        print("Purchase canceled.\n")

# Function for user authentication 
def authenticate_user():
    username = "user"
    password = "pass"
    print("\nLogin to Access the Store")
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")
    
    if entered_username == username and entered_password == password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

# Menu system
def menu():
    print("\nWelcome to the Online Store!")
    while True:
        print("\nMenu:")
        print("1. View Available Products")
        print("2. Add Items to Cart")
        print("3. View Cart")
        print("4. Remove Items from Cart")
        print("5. Complete Purchase")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                display_products()
            elif choice == 2:
                add_to_cart()
            elif choice == 3:
                view_cart()
            elif choice == 4:
                remove_from_cart()
            elif choice == 5:
                complete_purchase()
            elif choice == 6:
                print("Thank you for visiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a numeric option.")

# Main program
if __name__ == "__main__":
    if authenticate_user():
        menu()
