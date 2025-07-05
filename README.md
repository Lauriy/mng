Transitions:
```
current_state1 current_symbol1 new_state1 new_symbol1 move_direction
current_state2 current_symbol2 new_state2 new_symbol2 move_direction
current_state3 current_symbol3 new_state3 new_symbol3 move_direction
```

Rules:
```
The Mill starts on the first non-blank cell of the input tape and is in the state INIT
The Mill halts when it's in the state HALT
Each cell can contain only one symbol
A cell without a symbol is a blank cell and is represented by _
```

Limitations:
```
The tape length is limited to 2^20 cells (1 048 576 cells)
The number of states is limited to 2^16 (65 536 states)
State might be any string of up to 32 chars
The Mill has one tape and one head
```

```shell
    uv sync --dev
```

```shell
    ruff check --fix .
    ruff format .
```

```shell
    python src/solution_1.py
```

```shell
    pytest
```

```shell
    pytest -k test_1
```