from data_define import Record
from chardet import detect
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
    
for line in list1:
    print(line)