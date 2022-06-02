
var = 'Rafael'

def func1():
    print(var)
    
func1()

def func2():
    var = 'Rafa'
    def func3():
        var = 'Days'
        print(var)
    func3()
    print(var)

func2()

def func4():
    var = 'Rafa'
    def func5():
        nonlocal var
        var = 'Days'
        print(var)
    func5()
    print(var)

func4()