# Python - Almost a circle

A small shape hierarchy that reviews classes, properties, `*args`/`**kwargs`,
JSON serialization and unit testing.

| File | Description |
| --- | --- |
| `models/base.py` | `Base`: id management, JSON helpers, `save_to_file`, `create`, `load_from_file`, `draw` |
| `models/rectangle.py` | `Rectangle(Base)`: validated width, height, x, y; `area`, `display`, `update`, `to_dictionary` |
| `models/square.py` | `Square(Rectangle)`: `size` property, `update`, `to_dictionary` |
| `tests/test_models/` | Unit tests for every class: `python3 -m unittest discover tests` |
