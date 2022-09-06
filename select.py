import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="")
csr=conn.cursor()

try:
    print()
    print('Start')
    print()


    print('{:<10} {:<10} {:<10} {:<20}'.format('Id','Name','Class','Email'))
    data=csr.execute('select * from integral')
    for n in data:
        print('{:<10} {:<10} {:<10} {:<20}'.format(n[0], n[1], n[2], n[3]))

    print()
    print('Show All')

except:
    print('Error')