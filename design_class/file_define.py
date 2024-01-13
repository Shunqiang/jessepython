from data_define import Record
from chardet import detect
from pymysql import connect
import json
class FileReader:
    def read_data(self) -> list[Record]:
     pass
 
class TextFileReader(FileReader):
    def __init__(self, path) -> None:
       self.path = path
       
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding='utf-8', errors='ignore')
       
        record_list = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(',')
            record = Record(data_list[0],data_list[1],data_list[2],data_list[3],)
            record_list.append(record)
        f.close()
        return record_list
    
# class JsonFileWriter(FileReader):
#     def read_data(self) -> list[Record]:
#         f = open(self.path, "r", encoding='gb18030',)
#         print(f)
#         record_list: list[Record] = []
#         for line in f.readlines():
#             line = line.strip()
#             data_list = line.split(',')
#             record = Record(data_list[0],data_list[1],data_list[2],data_list[3],)
#             record_list.append(record)
#         f.close()
#         return record_list
def get_encoding_type(file):
    files =  open(file, 'rb')
    rawdata = files.read()
    return detect(rawdata)['encoding']    
if __name__ == '__main__':
    c = get_encoding_type('C:/Users/admin/Desktop/data.txt')
    print(c)
    text_file_reader = TextFileReader('C:/Users/admin/Desktop/data.txt')
    list1 = text_file_reader.read_data()

# data_dict = {}
# for record in list1:
#     if record.date in data_dict.keys():
#         print(1,list(data_dict.keys()),data_dict)
#         data_dict[record.date] += record.money
#     else:
#         data_dict[record.date] = record.money
# print(data_dict)

# for line in list3:
#     print(line)

conn = connect(host='localhost', port=3306, user='root', autocommit=True, passwd='123456')

conn.select_db('sys')

cursor = conn.cursor()

# cursor.execute("create table orders(date date, order_id varchar(255), money int, provice varchar(255))")


# cursor.execute("insert into orders(date, order_id, money, provice) values('2020-01-01', '1', 100, '上海')") 

# for x in list1:
#     sql = f"insert into orders(date, order_id, money, provice) values('{x.date}', '{x.order_id}', '{x.money}', '{x.provice}')"
#     cursor.execute(sql)
cursor.execute('select * from orders')
result: tuple = cursor.fetchall()  
print(result)
for x in result:
    print(list(x))
    
conn.close()    




