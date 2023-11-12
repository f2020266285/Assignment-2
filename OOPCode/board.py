import json
from knight import Knight
from item import Item
from coordinates import Position
from scores import Score


class Board:
    def __init__(self):
        self.__knights = {}
        self.__items = {}
        self.initialize_knights()
        self.initialize_items()

    @property
    def knights(self):
        return self.__knights

    @knights.setter
    def knights(self, value: Knight):
        self.__knights[value.name] = value

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value: Item):
        self.__items[value.name] = value

    def initialize_knights(self):
        self.knights = Knight("R", Position(0, 0))
        self.knights = Knight("B", Position(7, 0))
        self.knights = Knight("G", Position(7, 7))
        self.knights = Knight("Y", Position(0, 7))

    def initialize_items(self):
        self.items = Item("A", Position(2, 2))
        self.items = Item("D", Position(2, 5))
        self.items = Item("M", Position(5, 2))
        self.items = Item("H", Position(5, 5))

    def has_any_item(self, name):
        knight = self.knights.get(name)
        return knight.item is not None

    def validate_fight_and_item(self, name):
        knight = self.knights.get(name)
        if not knight:
            return False

        # Implement the logic to validate the fight and item acquisition
        return True

    def update_acquired_items_location(self):
        for knight in self.knights.values():
            if knight.item and not knight.is_dead:
                item = self.items.get(knight.item)
                if item:
                    item.position = knight.position

    def main(self, name, direction):
        knight = self.knights.get(name)
        if not knight:
            return

        knight.move(direction)
        self.update_acquired_items_location()
        self.validate_fight_and_item(name)

    def read_input(self, knight, direction):
        self.main(knight, direction)

    def output(self):
        return {
            "red": self.knights["R"].to_list(),
            "blue": self.knights["B"].to_list(),
            "green": self.knights["G"].to_list(),
            "yellow": self.knights["Y"].to_list(),
            "magic_staff": self.items["M"].to_list(),
            "helmet": self.items["H"].to_list(),
            "dagger": self.items["D"].to_list(),
            "axe": self.items["A"].to_list()
        }


if __name__ == '__main__':
    board = Board()
    print(json.dumps(board.output(), indent=2))
