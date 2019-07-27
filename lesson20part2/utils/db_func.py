import pymysql


class DatabaseConnector:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def get_connection(self):
        try:
            connection = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                         db=self.database, charset="utf8mb4",
                                         cursorclass=pymysql.cursors.DictCursor)
            return connection.cursor()
        except pymysql.Error as e:
            print(e)

    def insert_coupon(self, name, code, coupon_type, discount, logged, shipping, total,
                      date_start, date_end, uses_total, uses_customer, status, date_added):
        try:
            with self.get_connection() as cursor:
                cursor.execute("""INSERT INTO oc_coupon(
                               name, code, type, discount, logged, shipping, total,
                               date_start, date_end, uses_total, uses_customer,
                               status, date_added)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                               (name, code, coupon_type, discount, logged, shipping, total,
                                date_start, date_end, uses_total, uses_customer, status, date_added))
                cursor.commit()
        except pymysql.Error as e:
            print(e)
