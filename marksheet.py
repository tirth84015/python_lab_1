print("marksheet")
a=int(input("enter sub1 marks: "))
b=int(input("enter sub2 marks: "))
c=int(input("enter sub3 marks: "))
d=int(input("enter sub4 marks: "))
e=int(input("enter sub5 marks: "))

f=a+b+c+d+e
print("total of marks: ",f)

g=f*100/500
print("average is: ",g)

print("grade")
if(g>=80 and g<=90):
    print("distingtion")
elif(g>=70 and g<=80):
    print("A grade")
elif(g>=60 and g<=70):
    print("B grade")
elif(g>=50 and g<=60):
    print("C grade")
elif(g>=40 and g<=60):
    print("d grade")
else:
    print("sorry you are fail")
