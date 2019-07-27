import datetime
import sqlite3


class MyLogger:

    @staticmethod
    def get_connection(db_filename):
        sql_create_follows_table = "CREATE TABLE IF NOT EXISTS oc_logs(" \
                                   "id INTEGER PRIMARY KEY AUTOINCREMENT , " \
                                   "info TEXT NOT NULL ," \
                                   "log_time DATETIME DEFAULT current_timestamp);"
        try:
            connect = sqlite3.connect(db_filename)
            connect.cursor()
            connect.execute(sql_create_follows_table)
            return connect
        except sqlite3.Error as e:
            print(e)

    @staticmethod
    def write_to_db(db_name, info, log_time):
        try:
            with MyLogger.get_connection(db_name) as cursor:
                cursor.execute("INSERT INTO oc_logs("
                               "info, log_time) "
                               "VALUES (?, ?);", (info, log_time))
                cursor.commit()
        except sqlite3.Error as e:
            print(e)

    @staticmethod
    def get_datetime():
        time = datetime.datetime.now()
        result = "{} {}.{}.{}".format(time.date(), time.hour, time.minute, time.second)
        return result
