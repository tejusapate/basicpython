def multiplication(z):
    i=1;
    while(i<11):
        f=int(i*z)
        print(i,"*",z,"=",i*z)
        i=i+1
print("Enter the number whose muktiplication table you will like to see")
x=input()
multiplication(int(x))
