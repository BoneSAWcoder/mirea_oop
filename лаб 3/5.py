X = 4
Y = 3
Z = 5  
triangle = [X,Y,Z]
triangle.sort()

print(f'треугольник со сторонами {X}, {Y}, {Z}:')

if triangle[0] + triangle[1] > triangle[2]: 
    print('-существует')

    if (triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2):
        print('-прямоугольный')

    else: print ('-не прямоугольный')
else: print('-не существует')
