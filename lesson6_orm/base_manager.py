# Model object handler
import sqlite3


class BaseManager():
    connection = None

    @classmethod
    def set_connection(cls, db_name):
        connection = sqlite3.connect(db_name)
        # connection.autocommit = True
        cls.connection = connection

    @classmethod
    def _get_cursor(cls):
        return cls.connection.cursor()


    @classmethod
    def _execute_query(cls, query, params=None):
        cursor = cls._get_cursor()
        cursor.execute(query, params)

    def __init__(self, model_class):
        self.model_class = model_class
    
    
    def select(self, *field_names, chunk_size=2000):
        fields_format = ', '.join(field_names)
        query = f"SELECT {fields_format} FROM {self.model_class.table_name}"

        # Execute query
        cursor = self._get_cursor()
        cursor.execute(query)

        # Fetch data obtained with the previous query execution
        # and transform it into `model_class` objects.
        # The fetching is done by batches of `chunk_size` to
        # avoid to run out of memory.
        model_objects = list()
        is_fetching_completed = False
        while not is_fetching_completed:
            result = cursor.fetchmany(size=chunk_size)
            for row_values in result:
                keys, values = field_names, row_values
                row_data = dict(zip(keys, values))
                model_objects.append(self.model_class(**row_data))
            is_fetching_completed = len(result) < chunk_size

        return model_objects
    
    
    def insert(self, rows:list):
        field_names = rows[0].keys() #заголовки таблиц/классов
        assert all(row.keys() == field_names for row in rows[1:]) #подтверждает соответсвие форматов в строках

        fields_format = ", ".join(field_names)
        
        values_placeholder_format = ", ".join([f'({", ".join(["?"] * len(field_names))})'] * len(rows))  # https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries

        # field_names_str = str(field_names)
        # values_placeholder_format = ", ".join([f'({", ".join(([field_names_str]) * len(field_names))})'] * len(rows))
        
        # values_placeholder_format = ", ".join((['%s' for _ in range(len(field_names))]) * len(rows))
        # values_placeholder_format = ', '.join([f"'{str(_)}'" for _ in rows])
        
        query = f"INSERT INTO {self.model_class.table_name} ({fields_format}) VALUES {values_placeholder_format}"

        params = list()
        for row in rows:
            row_values = [row[field_name] for field_name in field_names]
            params +=row_values

        self._execute_query(query, params)


    # def delete(self):
    #     query = f"DELETE FROM {self.model_class.table_name}"
    #     self._execute_query(query)

    def update(self, new_data:dict):
        field_names = new_data.keys()
        placeholder_format = ', '.join([f'{field_name} = ?' for field_name in field_names])
        query = f"UPDATE {self.model_class.table_name} SET {placeholder_format}"
        params = list(new_data.values())

        # Execute query
        self._execute_query(query, params)