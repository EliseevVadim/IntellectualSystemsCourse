from core.constants import *
from core.models import Work


class Node(object):
    def __init__(self, work: Work, executed: bool):
        self.__work = work
        self.__executed = executed
        self.__children = []
        self.__T = self.work.k / (N_TRAINS * DAYS_IN_YEAR * self.work.dc) if self.executed else None
        self.__spending = {}
        self.__fails_count = 0
        self.__parent = None

    def __str__(self):
        return f"Work {self.work.work_number}, Executed: {self.executed}, T: {self.t}, fails: {self.fails_count}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.t == other.t
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Node):
            return self.t != other.t
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.t < other.t
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Node):
            return self.t <= other.t
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.t > other.t
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Node):
            return self.t >= other.t
        return NotImplemented

    def has_parent(self):
        return self.__parent is not None

    @property
    def spending(self):
        return self.__spending

    @property
    def fails_count(self):
        return self.__fails_count

    @fails_count.setter
    def fails_count(self, count):
        self.__fails_count = count

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @property
    def work(self):
        return self.__work

    @property
    def executed(self):
        return self.__executed

    @property
    def t(self):
        return self.__T

    @t.setter
    def t(self, t):
        self.__T = t

    def add_child(self, child: 'Node', minimal_remaining_price=0):
        spending_by_companies = MINIMAL_SPENDING_BY_COMPANIES.fromkeys(MINIMAL_SPENDING_BY_COMPANIES, 0)
        parent = self
        child.parent = parent
        total_k = child.work.k if child.executed else 0
        total_dc = child.work.dc if child.executed else 1
        if child.executed:
            spending_by_companies[child.work.executor] = child.work.k
        while parent is not None:
            if parent.executed:
                total_k += parent.work.k
                total_dc += parent.work.dc
                for key in spending_by_companies.keys():
                    if parent.work.executor == key:
                        spending_by_companies[key] += parent.work.k
            parent = parent.parent
        child.fails_count = sum(1 for key in spending_by_companies if spending_by_companies[key] <
                                MINIMAL_SPENDING_BY_COMPANIES[key])
        child.t = round(total_k / (DAYS_IN_YEAR * N_TRAINS * total_dc), 1)
        if child.t == 0:
            child.t = None
        child.__spending = spending_by_companies
        if total_k - child.work.k + minimal_remaining_price <= MAX_MONEY_TO_SPEND:
            self.__children.append(child)
