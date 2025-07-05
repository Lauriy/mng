from pathlib import Path


def solve():
    rules = [
        "INIT | ODD | R",  # First | makes the count odd, move right
        "ODD | EVEN | R",  # Next | makes the count even, move right
        "EVEN | ODD | R",  # Next | makes the count odd, move right
        "ODD _ BACK_ODD _ L",  # End reached in odd state, go back
        "EVEN _ BACK_EVEN _ L",  # End reached in even state, go back
        "BACK_ODD | BACK_ODD _ L",  # Clear tape while going back (odd case)
        "BACK_EVEN | BACK_EVEN _ L",  # Clear tape while going back (even case)
        "BACK_ODD _ HALT O R",  # Reached start, write O for odd
        "BACK_EVEN _ HALT E R",  # Reached start, write E for even
    ]

    project_root = Path(__file__).parent.parent
    machines_dir = project_root / "machines"
    with open(machines_dir / "2.txt", "w") as f:
        for rule in rules:
            f.write(rule + "\n")


if __name__ == "__main__":
    solve()
