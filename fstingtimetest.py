import timeit

format = """
def format(name, age):
    return f'He said his name is {name} and he is {age} years old.'
""", """
def format(name, age):
    return 'He said his name is %s and he is %s years old.' % (name, age)
""", """
def format(name, age):
    return 'He said his name is ' + name + ' and he is ' + str(
        age) + ' years old.'
""",  """
def format(name, age):
    return 'He said his name is {} and he is {} years old.'.format(name, age)
""", """
from string import Template

template = Template('He said his name is $name and he is $age years old.')

def format(name, age):
    return template.substitute(name=name, age=age)
"""

test = """
def test():
    for name in ('Fred', 'Barney', 'Gary', 'Rock', 'Perry', 'Jackie'):
        for age in range (20, 200):
            format(name, age)
"""

for fmt in format:
    print(timeit.timeit('test()', fmt + test, number=10000))