def solve():
    rules = [
        "INIT | FIND | R",  # Start moving right to find +
        "FIND | FIND | R",  # Keep moving right through first number
        "FIND + MOVE | R",  # Found +, replace with |, move right
        "MOVE | MOVE | R",  # Move through second number to find end
        "MOVE _ BACK _ L",  # Found end, go back to remove last |
        "BACK | HALT _ L",  # Remove last | and halt
    ]

    with open("output/1.txt", "w") as f:
        for rule in rules:
            f.write(rule + "\n")


if __name__ == "__main__":
    solve()
