"""Exercise 2: A Cart class.

Implement Cart so the example at the bottom of this file behaves correctly.

  add_item(item, qty=1)  add an item; if it is already in the cart,
                         increase the quantity instead of adding a second line
  remove_item(item_id)   remove that item entirely
  clear()                empty the cart
  total()                sum of price * qty across all lines, rounded to 2dp
  __repr__()             something readable, e.g. <Cart 3 items, $27.75>

Store each line as a dictionary:
    {"item_id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "qty": 2}
"""

from exercise1 import load_menu # what are we importing here? Food for thought.


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # TODO
        found = False
        for line in self.lines:
            if line["item_id"] == item["id"]:
                line["qty"] = line["qty"] + qty
                found = True
                break

        if found == False:
            new_line = {
                "item_id": item["id"],
                "name": item["name"],
                "price": item["price"],
                "qty": qty,
            }
            self.lines.append(new_line)

    def remove_item(self, item_id: int) -> None:
        # TODO
        index_to_remove = -1
        for i in range(len(self.lines)):
            if self.lines[i]["item_id"] == item_id:
                index_to_remove = i
                break

        if index_to_remove != -1:
            del self.lines[index_to_remove]

    def clear(self) -> None:
        # TODO
        self.lines = []

    def total(self) -> float:
        # TODO - round ONCE, at the end
        sum_total = 0
        for line in self.lines:
            sum_total = sum_total + (line["price"] * line["qty"])
        return round(sum_total, 2)

    def __repr__(self) -> str:
        # TODO
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]
    ramen = menu[0]

    cart = Cart()
    cart.add_item(gyoza, 2)
    cart.add_item(gyoza, 1)      # should become qty 3, NOT a second line
    cart.add_item(ramen, 1)

    print(cart)                  # <Cart 2 items, $40.50>
    print(len(cart.lines))       # 2
    print(cart.total())          # 40.5
