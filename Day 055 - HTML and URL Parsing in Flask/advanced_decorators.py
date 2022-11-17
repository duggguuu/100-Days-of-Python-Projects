def logging_dec(fn):
    def wrapper(*args,**kwargs):
        print(f"You called {fn.__name__}{args}")
        result=fn(args[0],args[1],args[2])
        print(f"It returned: {result}")
    return wrapper

@logging_dec
def a_func(a,b,c):
    return a*b*c

a_func(1,2,3)