'''
c=10
d=int("10")
print( c is d )
print( c == d )


def my_print(x):
    print(x)

print (type(my_print))

print(callable(my_print))


def demo1():
    """returns 10"""
    return 10
def demo2():
    return 20

print(demo1.__doc__)
print(demo2.__doc__)



def my_greet(greeting, name="world"):
    return "{0} {1}".format(greeting, name)


print(my_greet("Hello"))
print(my_greet("Hello", "john"))



def demo(first, second=2, third=3):
    return [first, second, third]

print(demo(10))
print(demo(10, 20))
print(demo(10, 20, 30))
#print(demo(second=20))
#print(demo(second=20, third=30))
#print(demo(first=10, third=30))
print( demo(10, third=30))





def demo_variable_args(first, *args):
    return args


def my_merge(separator, *args):
    return separator.join(args)

result=demo_variable_args("hello", "world")
print(type(result).__name__ )
print(result)
print(demo_variable_args("hello", 1, 2, 3))
print(my_merge(".", "one", "two", "three"))
print(my_merge(",", "one", "two", "three"))


def demo_with_keyword_args(name, *args, **kwargs):
    return kwargs

result = demo_with_keyword_args("jack", age=10, height=100)
print(type(result).__name__)
print(result)
print(demo_with_keyword_args("jack","address",age=10,height=100))
print(demo_with_keyword_args("jack", address="address", age=10, height=100))




def demo_sub(*args, **kwargs):
    return args, kwargs


def demo_unpacking(name, *args, **kwargs):
    return demo_sub(*args, **kwargs)


def demo_no_unpacking(name, *args, **kwargs):
    return demo_sub(args, kwargs)


result = demo_unpacking("jack", 1, 2, k1="v1", k2="v2")
print(result)
result = demo_no_unpacking("jack", 1, 2, k1="v1", k2="v2")
print(result)
result = demo_sub(1,2, k1="v1")
print(result)
result = demo_sub((1,2), {"k1" :"v1"})
print(result)
result = demo_sub(*(1,2), **{"k1": "v1"})
print(result)
result = demo_sub(*[1,2], **{"k1":"v1"})
print(result)



print(".".join(("hello", "there")))

'''

print(3//2)
    

