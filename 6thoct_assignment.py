

def print_mtable(number,c=1):
    result = number * c
    #print(number*c)
    print(f'{number} x {c} = {result}')
    if c < 10 :
        print_mtable(number,c+1)

number = int(input("Enter the number for multiplication table :"))
print_mtable(number)
