# Python - Test-driven development

Writing documentation and tests first: doctest files in `tests/*.txt` and a `unittest` suite for `max_integer`.

| File | Description |
|------|-------------|
| `0-add_integer.py` | Adds two ints/floats as integers (tests: `tests/0-add_integer.txt`) |
| `2-matrix_divided.py` | Divides every matrix element, rounded to 2 decimals (tests: `tests/2-matrix_divided.txt`) |
| `3-say_my_name.py` | Prints `My name is <first> <last>` (tests: `tests/3-say_my_name.txt`) |
| `4-print_square.py` | Prints a square of `#` (tests: `tests/4-print_square.txt`) |
| `5-text_indentation.py` | Adds two new lines after `.`, `?` and `:` (tests: `tests/5-text_indentation.txt`) |
| `6-max_integer.py` | Given `max_integer` function under test |
| `tests/6-max_integer_test.py` | `unittest` suite for `max_integer` |

Run the tests with `python3 -m doctest ./tests/*.txt` and `python3 -m unittest tests.6-max_integer_test`.
