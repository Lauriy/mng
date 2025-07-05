from pathlib import Path


def solve():
    rules = [
        "INIT | FIND | R",  # Start moving right to find +
        "FIND | FIND | R",  # Keep moving right through first number
        "FIND + MOVE | R",  # Found +, replace with |, move right
        "MOVE | MOVE | R",  # Move through second number to find end
        "MOVE _ BACK _ L",  # Found end, go back to remove last |
        "BACK | HALT _ L",  # Remove last | and halt
    ]

    project_root = Path(__file__).parent.parent
    machines_dir = project_root / "machines"
    with open(machines_dir / "1.txt", "w") as f:
        for rule in rules:
            f.write(rule + "\n")


if __name__ == "__main__":
    solve()
