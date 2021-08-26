import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect(user="AGE7", password="123456",
                               dsn="localhost/orclpdb1")

cursor = connection.cursor()
cursor.execute("""
        SELECT ID_EMPENHO FROM DM_EMPENHO_DESP
        WHERE ID_EMPENHO = 999""")
for table_id in cursor:
    print("ID:", table_id)
