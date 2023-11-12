import knight
from coordinates import Position
from scores import Score


class Item:
    def __init__(self, name: str, position: Position, score: Score, acquired_by=None):
        self.__name: str = name
        self.__position: Position = position
        self.__acquired_by: knight.Knight = acquired_by
        self.__score: Score = score

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @name.setter
    def name(self, value):
        self.__name = value

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def acquired_by(self):
        return self.__acquired_by

    @property
    def score(self):
        return self.__score

    @acquired_by.setter
    def acquired_by(self, value):
        self.__acquired_by = value

    @score.setter
    def score(self, value):
        self.__score = value

    def update_position_by_acquired_knight(self):
        if self.acquired_by:
            self.position = self.acquired_by.position

    def to_list(self):
        return [
            [self.position.x, self.position.y],
            self.acquired_by is not None
        ]
