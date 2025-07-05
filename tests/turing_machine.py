from pathlib import Path

STATE_INIT = "INIT"
STATE_HALT = "HALT"

MAX_STEPS = 1000000

DIRECTION_LEFT = "L"
DIRECTION_RIGHT = "R"


class TuringMachine:
    def __init__(self, rules, tape, start_state=STATE_INIT):
        self.rules = self._parse_rules(rules)
        self.tape = list(tape)
        self.head = 0
        self.state = start_state
        self.steps = 0
        self.max_steps = MAX_STEPS

        while self.head < len(self.tape) and self.tape[self.head] == "_":
            self.head += 1

        if self.head >= len(self.tape):
            self.tape.extend(["_"] * 10)

    @staticmethod
    def read_rules_from_file(filename: str):
        project_root = Path(__file__).parent.parent
        machines_dir = project_root / "machines"
        filename += ".txt"
        with open(machines_dir / filename, "r") as f:
            return [line.strip() for line in f if line.strip()]

    @staticmethod
    def _parse_rules(rules):
        parsed = {}
        for rule in rules:
            parts = rule.strip().split()
            if len(parts) == 5:
                current_state, current_symbol, new_state, new_symbol, direction = parts
                parsed[(current_state, current_symbol)] = (
                    new_state,
                    new_symbol,
                    direction,
                )

        return parsed

    def _get_current_symbol(self):
        if self.head < 0 or self.head >= len(self.tape):
            return "_"

        return self.tape[self.head] if self.tape[self.head] != "" else "_"

    def _write_symbol(self, symbol):
        while self.head < 0:
            self.tape.insert(0, "_")
            self.head += 1

        while self.head >= len(self.tape):
            self.tape.extend(["_"] * 10)

        self.tape[self.head] = symbol

    def _move_head(self, direction):
        if direction == DIRECTION_LEFT:
            self.head -= 1
        elif direction == DIRECTION_RIGHT:
            self.head += 1

        if self.head >= len(self.tape):
            self.tape.extend(["_"] * 10)

    def run(self):
        while self.state != STATE_HALT and self.steps < self.max_steps:
            current_symbol = self._get_current_symbol()

            if (self.state, current_symbol) not in self.rules:
                print(f"No rule found for ({self.state}, {current_symbol}), halting")
                break

            new_state, new_symbol, direction = self.rules[(self.state, current_symbol)]

            self._write_symbol(new_symbol)
            self._move_head(direction)
            self.state = new_state
            self.steps += 1

        result = self._get_result()

        return result

    def _get_result(self):
        result = "".join(self.tape).rstrip("_")

        return result if result else "_"
