from core.helpers import *
from core.models.Node import Node
from core.models.Work import Work


class PartialTraversal(object):
    def __init__(self, works: list):
        self.__works = works.copy()
        self.__initialize_tree()

    def __initialize_tree(self):
        self.__tree = Node(Work(0, 1, 0, "0"), False)
        nodes = [self.__tree]
        step_nodes = []
        while len(self.__works) > 0:
            work = self.__works.pop(0)
            minimal_remaining_price = min([work.k for work in self.__works]) if len(self.__works) > 0 else work.k
            for node in nodes:
                first_node = Node(work, True)
                second_node = Node(work, False)
                node.add_child(first_node, minimal_remaining_price)
                node.add_child(second_node, minimal_remaining_price)
                step_nodes.append(first_node)
                step_nodes.append(second_node)
            nodes = step_nodes.copy()
            step_nodes.clear()

    def __find_candidates_nodes(self):
        result = []
        find_candidates_nodes(self.__tree, result)
        return result

    def find_best_sequence(self):
        candidates = self.__find_candidates_nodes()
        best_end_node = min(candidates)
        nodes_sequence = find_ancestors(best_end_node)
        return nodes_sequence, best_end_node.t

    def show_tree(self):
        print_tree(self.__tree)
