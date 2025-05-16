#TAREA 1 BASICO
print("TAREA 1-BASICO")
for i in range(101):
    print(i) 

#TAREA 2 MULTIPLES DE 2
print("\nTAREA 2-MULTIPLES DE 2")
for i in range(2,501,2):
    print(i) 

#TAREA 3 ICE ICE BABY
print("\nTAREA 3-ICE ICE BABY")
for i in range(1,101):
    if i%10==0:
        print("baby")
    elif i%5==0:
        print("ice ice")
    else:
        print(i)
