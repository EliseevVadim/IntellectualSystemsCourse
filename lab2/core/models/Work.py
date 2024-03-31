from dataclasses import dataclass


@dataclass
class Work:
    work_number: int
    dc: int
    k: int
    executor: str
