n = 1

x = int(input("Input an integer"))
print("The factors of ", x, "are: ")
while n <= x:
    if x % n == 0:
        print(n)
        n=n+1
    #endif
#endwhile



