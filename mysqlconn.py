import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="")
csr=conn.cursor()
try:
    db="create database integral"
    csr.execute(db)
    print("db created")

except:
    print("db error")

# DATATYPES :-
# INT       - for integer length 11
# TINYINT   - for boolean length 3
# BIGINT    - for integer length 20
# VARCHAR   - for any datatype length 0 to 255
# TEXT      - for any datatype length 0 to 6000
# LONGTEXT  - for any datatype length 6000 n above
# YEAR      - YYYY
# DATE      - YYYY-MM-DD
# TIME      - HH-MM-SS
# DATETIME  - YYYY-MM-DD HH-MM-SS
# TIMESTAME - system current time