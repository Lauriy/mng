from pathlib import Path


def solve():
    rules = [
        # Find the end of the binary number
        "INIT 0 FIND_END 0 R",  # Move right through 0s
        "INIT 1 FIND_END 1 R",  # Move right through 1s
        "FIND_END 0 FIND_END 0 R",  # Continue moving right through 0s
        "FIND_END 1 FIND_END 1 R",  # Continue moving right through 1s
        "FIND_END _ BACK_TO_LAST _ L",  # Found end, go back to last bit
        # Process increment from rightmost bit
        "BACK_TO_LAST 0 HALT 1 L",  # If last bit is 0, change to 1 and halt
        "BACK_TO_LAST 1 CARRY 0 L",  # If last bit is 1, change to 0 and carry
        # Handle carry propagation
        "CARRY 0 HALT 1 L",  # Found 0, change to 1 and halt
        "CARRY 1 CARRY 0 L",  # Found 1, change to 0 and continue carry
        "CARRY _ ADD_ONE 1 R",  # Reached beginning, add 1 at start
        # After adding 1 at beginning, position correctly
        "ADD_ONE 0 HALT 0 R",  # Move right to position after new bit
        "ADD_ONE 1 HALT 1 R",  # Move right to position after new bit
    ]

    project_root = Path(__file__).parent.parent
    machines_dir = project_root / "machines"
    with open(machines_dir / "3.txt", "w") as f:
        for rule in rules:
            f.write(rule + "\n")


if __name__ == "__main__":
    solve()
