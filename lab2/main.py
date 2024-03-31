from core.models.Work import Work
from core.solvers.AStar import AStar
from core.solvers.PartialTraversal import PartialTraversal

work1 = Work(work_number=6, dc=400, k=3942000, executor="ПМС-219")
work2 = Work(work_number=1, dc=150, k=3832500, executor="ПМС-219")
work3 = Work(work_number=2, dc=200, k=4453000, executor="МСО-9")
work4 = Work(work_number=5, dc=350, k=4215750, executor="МСО-9")
work5 = Work(work_number=3, dc=250, k=1368750, executor="ПМС-219")
work6 = Work(work_number=4, dc=300, k=3285000, executor="МСО-9")

works = [work1, work2, work3, work4, work5, work6]

partial_traversal = PartialTraversal(works)
partial_traversal.show_tree()
best_sequence, t = partial_traversal.find_best_sequence()
works_to_do = [node.work for node in best_sequence if node.executed]
print(works_to_do, t)

a_star = AStar(works)
works_to_do, t = a_star.find_best_works_to_do()
print(works_to_do, t)
