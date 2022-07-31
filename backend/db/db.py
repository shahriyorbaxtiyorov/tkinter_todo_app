import sqlite3


# Decorator commit for db
def commit(func):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('db.sqlite3')
        connection.cursor()

        result = func(*args, **kwargs)

        connection.commit()
        connection.close()

        return result

    return wrapper
