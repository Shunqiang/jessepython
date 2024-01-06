# class Student:
#     name = None
#     def say(self, msg):
#         print(f'HELLO, I AM {self.name} {msg}')

# person = Student()
# person.name = '阿三'

# person.say('见到你很高兴！')

class Phone: 
    __vaoltage = 10.5
    def __keep_sigle(self):
        print('rangcdd')
    
    def call_by_5g(self): 
        if self.__vaoltage >= 1:
            print('5gtonghuayikaiqi')
        else:
            self.__keep_sigle()
            
phone = Phone()
# phone.__keep_sigle()
phone.call_by_5g()