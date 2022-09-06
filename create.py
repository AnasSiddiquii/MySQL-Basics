import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="",database="integral")
csr=conn.cursor()

try:
    tb='''
            CREATE TABLE kids (
                Id int PRIMARY KEY AUTO_INCREMENT,
                Name varchar(50),
                Class varchar(10),
                Email varchar(30)
            )
        '''
    csr.execute(tb)

    print('Saved')

except:
    print('Already Exists')
