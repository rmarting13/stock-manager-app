import sys

from log.logger_base import log
import psycopg2 as db
from psycopg2 import pool
class Connection:
    _DATABASE = 'postgres'
    _USERNAME = 'postgres'
    _PASSWORD = 'postgres'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Connection pool opening successful: {cls._pool}')
            except Exception as e:
                log.error(f'An exception occurred during getting the pool: {e}')
                sys.exit()
        return cls._pool

    @classmethod
    def getConnection(cls):
        try:
            connection = cls.getPool().getconn()
            log.debug(f'Connection fetched from pool: {connection}')
            return connection
        except Exception as e:
            log.error(f'An exception occurred while fetching the connection from pool: {e}')

    @classmethod
    def putConnection(cls, conn):
        try:
            cls.getPool().putconn(conn)
            log.debug(f'Connection returned: {conn}')
        except Exception as e:
            log.error(f'An exception occurred while returning connection to pool: {e}')

    @classmethod
    def closeAllConnections(cls):
        try:
            cls.getPool().closeall()
            log.debug('All connections have been returned to the pool which is closed now.')
        except Exception as e:
            log.error(f'An exception occurred during connection pool shutdown: {e}')
    @classmethod
    def getCursor(cls):
        pass

if __name__ == '__main__':
    c1 = Connection.getConnection()
    Connection.putConnection(c1)
    c2 = Connection.getConnection()
    #c3 = Connection.getConnection()
    #c4 = Connection.getConnection()
    #c5 = Connection.getConnection()
    #c6 = Connection.getConnection()
