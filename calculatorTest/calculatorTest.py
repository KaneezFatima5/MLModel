from calculator import calculator

def testSum():
    assert calculator.add(2, 3)==5
    assert calculator.add(4, -5)==-1
    assert calculator.add(-10, -10)==-20

def testSubtract():
    assert calculator.subtract(2, 9)==-7
    assert calculator.subtract(30, 10)==20
    assert calculator.subtract(9, -20)==29
    assert calculator.subtract(-20, -20)==0

def testMultiply():
    assert calculator.multiply(2, 10)==20
    assert calculator.multiply(30, 0)==0
    assert calculator.multiply(2, -1)==-2

def testDivide():
    assert calculator.divide(20, 2)==10
    assert calculator.divide(10, 10)==1
    assert calculator.divide(9, 9)==1