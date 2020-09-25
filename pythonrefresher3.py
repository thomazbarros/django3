age = 31

name = 'Thomaz'

todayIsCold = True

def hello (name='Alice', age=34):
    return "Hello {} you are {} years old.".format(name, age)

sentence = hello()

print(sentence)

sentence = hello(name, age)

print(sentence)

