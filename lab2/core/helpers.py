from core.models.Node import Node


def print_tree(node: Node, depth=0):
    if node is None:
        return
    print("  " * depth + f"- Work {node.work.work_number}, Executed: {node.executed}, T: {node.t}, fails: "
                         f"{node.fails_count}")
    for child in node.children:
        print_tree(child, depth + 1)


def find_candidates_nodes(node: Node, result: list):
    if node is None:
        return
    if node.fails_count == 0 and node.executed:
        result.append(node)
    for child in node.children:
        find_candidates_nodes(child, result)


def find_ancestors(node: Node):
    ancestors = [node]
    parent = node.parent
    while parent is not None:
        ancestors.append(parent)
        parent = parent.parent
    return ancestors
