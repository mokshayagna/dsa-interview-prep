i = 0
flowerbed = [0,0,0,0,0,1,0,0]
n = 2

while i < len(flowerbed):
    if (flowerbed[i] == 0 and
        (i == 0 or flowerbed[i-1] == 0) and
        (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):

        flowerbed[i] = 1
        n -= 1
        i += 2
    else:
        i += 1

    if n == 0:
        print(True)
        break

if n > 0:
    print(False)