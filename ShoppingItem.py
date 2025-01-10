class ShoppingItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.purchased = False

    def mark_as_purchased(self):
        self.purchased = True

    def __str__(self):
        status = "Purchased" if self.purchased else "Not Purchased"
        return f"{self.name} (x{self.quantity}) - ${self.price} ({status})"


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        item = ShoppingItem(name, quantity, price)
        self.items.append(item)
        print(f"Added: {item}")

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"Removed: {item}")
                return
        print("Item not found.")

    def view_list(self):
        if not self.items:
            print("The shopping list is empty.")
        else:
            for item in self.items:
                print(item)

    def mark_item_as_purchased(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.mark_as_purchased()
                print(f"Marked as purchased: {item}")
                return
        print("Item not found.")

    def view_total_cost(self):
        total_cost = sum(item.price * item.quantity for item in self.items if not item.purchased)
        print(f"Total cost of remaining items: ${total_cost:.2f}")


def main():
    shopping_list = ShoppingList()

    while True:
        print("\n1. Add Item\n2. Remove Item\n3. View List\n4. Mark Item as Purchased\n5. View Total Cost\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: $"))
            shopping_list.add_item(name, quantity, price)
        elif choice == '2':
            name = input("Enter item name to remove: ")
            shopping_list.remove_item(name)
        elif choice == '3':
            shopping_list.view_list()
        elif choice == '4':
            name = input("Enter item name to mark as purchased: ")
            shopping_list.mark_item_as_purchased(name)
        elif choice == '5':
            shopping_list.view_total_cost()
        elif choice == '6':
            print("Exiting the shopping list manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
