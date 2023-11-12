from coordinates import Position
from scores import Score
from Item import Item
from state import State


class Knight:
    def __init__(self, name: str, position: Position, score: Score, item: Item = None, state: State = State.Live):
        self.__name = name
        self.__position = position
        self.__score = score
        self.__item = item
        self.__state = state

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @property
    def score(self):
        return self.__score

    @property
    def item(self):
        return self.__item

    @name.setter
    def name(self, value):
        self.__name = value

    @position.setter
    def position(self, value):
        self.__position = value

    @score.setter
    def score(self, value):
        self.__score = value

    @item.setter
    def item(self, value):
        self.__item = value

    @property
    def state(self) -> State:
        return self.__state

    @state.setter
    def state(self, value: State):
        self.__state = value

    def is_live(self) -> bool:
        return self.state == State.Live

    def does_not_has_item(self):
        return self.item is None

    def drop_item(self, state: State):
        self.item = None
        self.state = state

    def declare_dead(self):
        self.drop_item(State.Dead)

    def declare_drowned(self):
        self.drop_item(State.DROWNED)

    def acquire_item(self, item: Item):
        if self.is_live() and self.found_item(item):
            self.item = item
            self.score.attack += item.score.attack
            self.score.defence += item.score.defence

    def is_winner(self, defender) -> bool:
        if self.is_live() and defender.is_live():
            return self.score.total_score() > defender.score.total_score()
        return False

    def found_item(self, item: Item):
        return self.is_live() and item.position == self.position and item.acquired_by is None

    def __eq__(self, other):
        return other is not None and self.position.x == other.position.x and self.position.y == other.position.y

    def move_north(self):
        if self.is_live():
            self.position = Position(self.position.x - 1, self.position.y)

    def move_south(self):
        if self.is_live():
            self.position = Position(self.position.x + 1, self.position.y)

    def move_west(self):
        if self.is_live():
            self.position = Position(self.position.x, self.position.y - 1)

    def move_east(self):
        if self.is_live():
            self.position = Position(self.position.x, self.position.y + 1)

    def state_to_str(self):
        if self.state == State.Live:
            return "LIVE"
        elif self.state == State.Dead:
            return "DEAD"
        else:
            return "DROWNED"

    def has_any_fight(self, knights: dict):
        if self.is_live():
            for other_knight in knights.values():
                if other_knight != self and other_knight.position == self.position:
                    return True
        return False

    def to_list(self):
        return [
            [self.position.x, self.position.y] if self.state != State.DROWNED else None,
            self.state_to_str(),
            self.item.name if self.item is not None else None,
            self.score.attack,
            self.score.defence
        ]

   
   
    
