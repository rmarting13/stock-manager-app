from db_context.db_connection import Connection
from log.logger_base import log


class Cursor:
    def __int__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Excecuting __enter__ method')
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Excecuting __exit__ method')
        if exc_val:
            self._connection.rollback()
            log.error(f'An exception occurred during query transaction: {exc_type}: {exc_val}: {exc_tb}')
        else:
            self._connection.commit()
            log.debug('Transaction committed')
        self._cursor.close()
        Connection.putConnection(self._connection)


if __name__ == '__main__':
    with Cursor() as cursor:
        pass