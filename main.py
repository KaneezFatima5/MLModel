from calculator import calculator;

a=float(input("Enter frist number "));
b=float(input("Enter second number "));

sum=calculator.add(a, b);
difference=calculator.subtract(a, b);
multiplication=calculator.multiply(a, b);
division=calculator.divide(a, b);

print("The sum of "+str(a)+", "+str(b)+" is "+str(sum));
print("The difference of "+str(a)+", "+str(b)+" is "+str(difference));
print("The multiplication of "+str(a)+", "+str(b)+" is "+str(multiplication));
print("The division of "+str(a)+", "+str(b)+" is "+str(division));