'''
DIST=150
SPEED=50
BREAK=30
TIME BR=10M
TRAFFICDELAY = 30
'''

a=input("Enter Name of destination: ")
b=int(input("Enter distance to destination: "))
c=int(input("Enter Speed per kilometer: "))
d=int(input("Enter No. of breaks in Journey: "))
e=int(input("Enter time per brak: "))

time=((b/c)+(d*e))
t=time//60
tm=time%60
print(t,"hrs",tm,"min")





