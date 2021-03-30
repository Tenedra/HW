x, y = map(float, input().split())

if ( 25 <= x**2+y**2 <= 100 and x >= -3 and y <= 0) or (x**2+y**2 <= 25 and y >= 0 and -3 <= x <= 2):
    print("Yes")
else:
    print("No")