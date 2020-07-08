x = 1
y = 2

def my_function(x):
    y = 3
    print(x, y)


my_function(10)
print(x, y)


def my_function():
    global x
    x = 100

my_function()
print(x)