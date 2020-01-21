import time
def time_show(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(time.time() - start)
        return result
    return wrapper

@time_show
def one(n):
    list = []
    for i in range(n):
         list.append(i)
    return list
one(10**6)
print('время создания списка')
print()

@time_show
def two(n):
    list = [i for i in range(1,n+1)]
    return list
two(10**6)
print('время создания с помощью генератора')




