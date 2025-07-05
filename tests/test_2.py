from pathlib import Path

from src import solution_2
from tests.turing_machine import TuringMachine


def test_2():
    solution_2.solve()

    rules = TuringMachine.read_rules_from_file("2")

    project_root = Path(__file__).parent.parent
    input_file = project_root / "input" / "2.txt"
    with open(input_file, "r") as f:
        tape = f.read().strip()
    tm = TuringMachine(rules, tape)
    result = tm.run()

    output_file = project_root / "output" / "2.txt"
    with open(output_file, "r") as f:
        expected = f.read().strip()

    assert result == expected, f"Expected {expected}, got {result}"
