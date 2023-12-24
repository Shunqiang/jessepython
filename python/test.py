def logger(func):
    def wrapper():
        print('haha')
        func()
        print('done')
    return wrapper


@logger
def sample():
    print('inside sample function')
    
sample()

