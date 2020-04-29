n=int(input())

if n%2==0:
    if 1<n<6:
        print("Not Weird")
    elif 5<n<21:
        print("Weird")
    else:
        print("Not Weird")
    
else:
    print("Weird")
