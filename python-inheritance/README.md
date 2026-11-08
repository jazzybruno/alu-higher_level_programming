# Python - Inheritance

Inheritance in Python: subclasses, `isinstance`/`issubclass`/`type`, `super()`, and a small geometry hierarchy (`BaseGeometry` → `Rectangle` → `Square`).

| File | Description |
|------|-------------|
| `0-lookup.py` | `lookup(obj)` returns the list of an object's attributes and methods |
| `1-my_list.py` | `MyList(list)` with `print_sorted()` (tests in `tests/1-my_list.txt`) |
| `2-is_same_class.py` | True if an object is exactly an instance of a class |
| `3-is_kind_of_class.py` | True if an object is an instance of a class or one of its subclasses |
| `4-inherits_from.py` | True only if the object's class is a strict subclass |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry.area()` raises `Exception` |
| `7-base_geometry.py` | Adds `integer_validator()` (tests in `tests/7-base_geometry.txt`) |
| `8-rectangle.py` | `Rectangle(BaseGeometry)` with validated private width and height |
| `9-rectangle.py` | Adds `area()` and `[Rectangle] w/h` string form |
| `10-square.py` | `Square(Rectangle)` with a validated private size |
| `11-square.py` | `Square` with its own `[Square] w/h` string form |
