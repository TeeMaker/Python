x = 0
y = 0

while 3 * x + 4 * y != 52:
    x += 1
    y = 0
    while 3 * x + 4 * y != 52 and y < 100:
        y += 1
#    x += 1
print(x, y)
