# Python - Object-relational mapping

Querying MySQL from Python, first with raw SQL through `MySQLdb`, then through
the SQLAlchemy ORM.

| File | Description |
| --- | --- |
| `0-select_states.py` | List all states |
| `1-filter_states.py` | States whose name starts with `N` |
| `2-my_filter_states.py` | States matching an argument (query built with `format`) |
| `3-my_safe_filter_states.py` | Same, safe from SQL injection |
| `4-cities_by_state.py` | All cities with their state name |
| `5-filter_cities.py` | Cities of a given state, comma separated |
| `model_state.py` | `State` model and declarative `Base` |
| `7-model_state_fetch_all.py` | All `State` objects |
| `8-model_state_fetch_first.py` | First `State`, or `Nothing` |
| `9-model_state_filter_a.py` | States containing `a` |
| `10-model_state_my_get.py` | Id of a state by name, or `Not found` |
| `11-model_state_insert.py` | Add `Louisiana` |
| `12-model_state_update_id_2.py` | Rename state 2 to `New Mexico` |
| `13-model_state_delete_a.py` | Delete states containing `a` |
| `model_city.py` | `City` model linked to `states.id` |
| `14-model_city_fetch_by_state.py` | All cities with their state |
