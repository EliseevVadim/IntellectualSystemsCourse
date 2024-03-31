from core.constants import *
from itertools import combinations

from core.models.WorksCombination import WorkCombination


class AStar(object):
    def __init__(self, works: list):
        self.__works = works

    def find_best_works_to_do(self):
        minimal_spending_by_companies = dict(sorted(MINIMAL_SPENDING_BY_COMPANIES.items(), key=lambda item: item[1],
                                                    reverse=True))
        companies = list(minimal_spending_by_companies.keys())
        best_sequence = []
        for company in companies:
            possible_works_combinations = self.__generate_works_combinations_for_company(company)
            candidate_works_combinations = possible_works_combinations.copy()
            for combination in possible_works_combinations:
                spending_cost = sum(work.k for work in combination.works)
                best_sequence_cost = sum(work.k for combination in best_sequence for work in combination.works)
                if (spending_cost < MINIMAL_SPENDING_BY_COMPANIES[company] or
                        spending_cost + best_sequence_cost > MAX_MONEY_TO_SPEND):
                    candidate_works_combinations.remove(combination)
                    continue
                combination_t, combination_k, combination_dc = self.__calculate_best_sequence_metrics_with_addition(
                    best_sequence.copy(), combination
                )
                combination.t = combination_t
            if len(candidate_works_combinations) == 0:
                continue
            best_candidate_combination = min(candidate_works_combinations)
            best_sequence.append(best_candidate_combination)
        best_works_to_do = [work for combination in best_sequence for work in combination.works]
        t, _, _ = self.__calculate_best_sequence_metrics(best_sequence)
        return best_works_to_do, t

    def __generate_works_combinations_for_company(self, company: str):
        company_works = [work for work in self.__works if work.executor == company]
        company_possible_works_combinations = []
        for length in range(1, len(company_works) + 1):
            for combo in combinations(company_works, length):
                company_possible_works_combinations.append(WorkCombination(works=combo, t=0))
        return company_possible_works_combinations

    def __calculate_best_sequence_metrics(self, best_sequence: list[WorkCombination]):
        works = [work for combination in best_sequence for work in combination.works]
        if len(best_sequence) == 0:
            return 0, 0, 0
        dc = sum(work.dc for work in works)
        k = sum(work.k for work in works)
        t = round(k / (DAYS_IN_YEAR * N_TRAINS * dc), 1)
        return t, k, dc

    def __calculate_best_sequence_metrics_with_addition(self, best_sequence: list[WorkCombination],
                                                        addition: WorkCombination):
        best_sequence.append(addition)
        return self.__calculate_best_sequence_metrics(best_sequence)
