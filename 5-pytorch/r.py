n=int(input("Enter your number: "))
remainder=0
final=0
while(n!=0):
    remainder=n%10
    final=final*10+remainder
    n=n/10

print(final)