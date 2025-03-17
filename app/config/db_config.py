import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="b0we3stgfk88wu2zgcbr-mysql.services.clever-cloud.com",
        user="uoamr67ezryzjefx",
        password="7kVVJhhq1BVPNSe0h4ss",
        database="b0we3stgfk88wu2zgcbr"
    )