# Q2 Implement a B-Method specification for a basic e-commerce checkout system and verify consistency in python

class ECommerceCheckout:
    def __init__(self, all_items, prices):
        # B-Method: SETS + CONSTANTS
        self.all_items = set(all_items)
        self.prices = dict(prices)
        assert self.all_items == set(self.prices.keys()), "Prices must cover all items"

        # B-Method: VARIABLES + INITIALISATION
        self.cart = {item: 0 for item in self.all_items}
        self.inventory = {item: 10 for item in self.all_items}  # assume 10 units of each item

    def check_invariant(self):
        # B-Method: INVARIANT - cart(i) ≤ original_inventory(i)
        for item in self.all_items:
            assert self.cart[item] >= 0, f"Invariant violated: cart has negative quantity of {item}"
            assert self.inventory[item] >= 0, f"Invariant violated: inventory has negative quantity of {item}"
            total_available = self.cart[item] + self.inventory[item]
            assert total_available <= 10, f"Invariant violated: total for {item} exceeds initial stock (10)"

    # B-Method: OPERATION AddItem
    def add_item(self, item):
        if item in self.all_items and self.inventory[item] > 0:
            self.cart[item] += 1
            self.inventory[item] -= 1
        else:
            raise ValueError(f"Cannot add item '{item}': invalid or out of stock")
        self.check_invariant()

    # B-Method: OPERATION RemoveItem
    def remove_item(self, item):
        if item in self.all_items and self.cart[item] > 0:
            self.cart[item] -= 1
            self.inventory[item] += 1
        else:
            raise ValueError(f"Cannot remove item '{item}': not in cart")
        self.check_invariant()

    # B-Method: OPERATION Checkout
    def checkout(self):
        total = sum(self.cart[item] * self.prices[item] for item in self.cart)
        print(f"\n Checkout complete. Total price: ${total}")
        self.cart = {item: 0 for item in self.all_items}
        self.check_invariant()

    def print_state(self):
        print("\n Cart State:", self.cart)
        print(" Inventory State:", self.inventory)


# 🔽 Example usage
if __name__ == "__main__":
    items = ['apple', 'banana', 'carrot']
    prices = {'apple': 2, 'banana': 1, 'carrot': 3}

    checkout_system = ECommerceCheckout(items, prices)

    print(" Performing operations...")
    checkout_system.add_item('apple')
    checkout_system.add_item('banana')
    checkout_system.add_item('carrot')
    checkout_system.remove_item('banana')
    checkout_system.print_state()
    checkout_system.checkout()
    checkout_system.print_state()
