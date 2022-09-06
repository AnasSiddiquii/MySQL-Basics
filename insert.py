import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="",database="integral")
csr=conn.cursor()

try:
    ins="INSERT INTO members (Name,Class,Email) values (%s,%s,%s)"
    d=('Anas','MCA','scd8055@gmail.com')
    csr.execute(ins)
    conn.commit()
    print('inserted')

except:
    print('error')

