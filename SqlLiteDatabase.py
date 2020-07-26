import sqlite3


class SQLighter:
    def __init__(self, database, tables):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.tables = tables

    def add_new(self, id_chat, name, first_name):
        a = self.cursor.execute('SELECT * FROM {} WHERE id_chat=?'.format(self.tables), ( id_chat,)).fetchall()
        if a:
            pass
        else:
            self.cursor.execute("insert into {} values (?, ?, ?)".format(self.tables), ( id_chat, name, first_name,))
            self.connection.commit()

    def select_all(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM {}'.format(self.tables)).fetchall()

    def count_id_chat(self):
        with self.connection:
            return self.cursor.execute('SELECT id_chat FROM {}'.format(self.tables)).fetchall()

    def count_id_chat_name(self):
        with self.connection:
            return self.cursor.execute('SELECT id_chat,first_name FROM {}'.format(self.tables)).fetchall()

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()