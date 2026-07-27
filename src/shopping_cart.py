"""
Shopping cart module.
BUG #1: apply_discount uses wrong operator — subtracts discount amount directly instead of percentage
BUG #2: get_total does NOT account for quantity of each item (always counts 1)
BUG #3: remove_item removes by name but doesn't handle case where item doesn't exist
"""


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, quantity: int = 1):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name: str):
        # BUG: If item not found, this crashes with StopIteration — should handle gracefully
        item = next(i for i in self.items if i["name"] == name)
        self.items.remove(item)

    def get_total(self) -> float:
        # BUG: Ignores quantity! Should be price * quantity for each item
        return sum(item["price"] for item in self.items)

    def apply_discount(self, discount_percent: float) -> float:
        total = self.get_total()
        # BUG: Subtracts raw percent number instead of applying percentage
        # e.g. 10% off $100 → gives $90 but code does $100 - 10 = $90 (accidentally correct)
        # but 10% off $200 → should give $180, code gives $200 - 10 = $190 (WRONG)
        return total - discount_percent

    def item_count(self) -> int:
        return len(self.items)

    def clear(self):
        self.items = []
