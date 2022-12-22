import pyodbc
from config import *

class Db:
    def __init__(self):
        self.conn = pyodbc.connect(
            "DRIVER={MySQL ODBC 8.0 Unicode Driver}; "
            "SERVER="+DB_HOST+";DATABASE="+DB_NAME+"; "
            "UID="+DB_USER+"; PASSWORD="+DB_PASSWORD+";",
            autocommit=True
        )

        self.cursor = self.conn.cursor()

    def query(self, query, args=None):
        if args is None:
            args = []
        self.cursor.execute(query, args)

    def select(self, query: object, args: object = None, fetchAll: object = True) -> object:
        if args is None:
            args = []
        self.cursor.execute(query, args)

        raw = self.cursor.fetchall()

        if fetchAll:
            return raw
        else:
            if len(raw) > 0:
                return raw[0]
            else:
                return 0

    def close(self):
        self.conn.close()


