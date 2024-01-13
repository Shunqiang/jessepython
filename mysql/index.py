from pymysql import connect

conn = connect(host='localhost', port=3306, user='root', passwd='123456', autocommit=True)

print (conn.get_server_info())
        
cursor = conn.cursor()
conn.select_db('sys')
# cursor.execute('create table userinfo(id int, name varchar(20))')       
# cursor.execute("insert into userinfo(id, name) values(2, 'john')") 

# result: tuple = cursor.fetchall()     

# for x in result:
#   print(x)   
conn.close()

