from dataclasses import dataclass


@dataclass
class WorkCombination:
    works: tuple
    t: float

    def __eq__(self, other):
        if isinstance(other, WorkCombination):
            return self.t == other.t
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, WorkCombination):
            return self.t != other.t
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, WorkCombination):
            return self.t < other.t
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, WorkCombination):
            return self.t <= other.t
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, WorkCombination):
            return self.t > other.t
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, WorkCombination):
            return self.t >= other.t
        return NotImplemented
