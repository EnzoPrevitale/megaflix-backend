def table(table_name: str, user: bool = False):
    def wrapper(cls):
        cls._table = table_name
        cls._user = user
        return cls
    return wrapper

@table(table_name="model")
class Model:
    def __init__(self):
        try:
            self._table
        except Exception as e:
            print(f"[Model] {self.__class__.__name__} has no table name defined at @table()")

