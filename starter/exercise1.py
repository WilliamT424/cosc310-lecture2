"""Exercise 1: Menu filtering.

Load data/menu.json and print every AVAILABLE item under $10.00,
sorted by price, cheapest first.

Expected output shape:
    Green Tea            $3.25
    Iced Coffee          $4.25
    ...

Requirements:
  - use an f-string for the output
  - type-hint every function you write
"""

import json
from pathlib import Path

MENU_PATH = Path(__file__).parent / "data" / "menu.json"


def load_menu() -> list[dict]:
    """Read the menu file and return it as a list of dictionaries."""
    with MENU_PATH.open() as f:
        return json.load(f)

def available_under(menu: list[dict], limit: float) -> list[dict]:
    """Return available items priced below `limit`, sorted cheapest first."""
    # TODO: filter items priced under $10, then sort by price.
    result = []
    for item in menu:
        if item["available"] == True and item["price"] < limit:
            result.append(item)

    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j]["price"] > result[j + 1]["price"]:
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp

    return result


def main() -> None:
    menu = load_menu()
    for item in available_under(menu, 10.00):
        # TODO: print name and price using an f-string.
        # Hint: f"{item['name']:<20} ${item['price']:.2f}"
        print(f"{item['name']:<20} ${item['price']:.2f}")


if __name__ == "__main__":
    main()
