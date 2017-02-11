sub1=int(input("enter marks of 1st subject = "))
sub2=int(input("enter marks of 2nd subject = "))
sub3=int(input("enter marks of 3rd subject = "))
sub4=int(input("enter marks of 4th subject = "))
sub5=int(input("enter marks of 5th subject = "))
total=(sub1+sub2+sub3+sub4+sub5)
mean=(sub1+sub2+sub3+sub4+sub5)/5
perc=total*100/500
print total 
print "Mean = ",mean
print "percentage = ",perc
if perc<35:
    print "fail"
else :
    print "pass"

    

