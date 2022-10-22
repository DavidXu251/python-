
data=input('乐谱：').split()
circle='C D E F G A B C'.split()
data=[circle.index(x) for x in data]
data=[circle[len(circle)-x-1] for x in data]

print(' '.join(data))
