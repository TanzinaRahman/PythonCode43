

def add(*numbers) :
    sum = 0
    for num in numbers:
        sum = sum + num
        print(sum)
        add(10, 20)
        add(10, 20, 30)
        add(10, 20, 30, 40)



def student(**details):
    print(details)
    student(id=101,name="Anis")
