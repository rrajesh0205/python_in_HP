f = open('berry.png', 'rb')
f1 = open('berrynew.png', 'wb')
for i in f:
    f1.write(i)
