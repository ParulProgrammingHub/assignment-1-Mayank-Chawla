def simple_interest(p,t,r) :
    s=float((p*r*t)/100)
    print("simple interest is ",s)

p=int(input("enter principal amount : "))
r=float(input("enter interest rate (in %) :"))
t=int(input("enter time : "))
simple_interest(p,t,r)
      
