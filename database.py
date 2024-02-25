import sqlite3
import typing

class WorkspaceData:
    def __init__(self):
        
        self.conn = sqlite3.connect("database.db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS watchlist (symbol TEXT, exchange TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS strategies (strategy_type TEXT, contract TEXT,"
                            "timeframe TEXT, balance_pct REAL, take_profit REAL, stop_loss REAL, extra_params TEXT)")
        
        self.conn.commit()

    def save(self, table: str, data: typing.List[typing.Tuple]):

        self.cursor.execute(f"DELETE FROM {table}")

        "INSERT INTO watchlist (symbol, exchange) VALUE (?,?)"

        table_data = self.cursor.execute(f"SELECT * FROM {table}")

        columns = [description[0] for description in table_data.description]