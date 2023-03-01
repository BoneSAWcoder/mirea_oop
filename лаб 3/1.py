# 1. Можно ли из бревна, имеющего диаметр поперечного сечения D, 
# выпилить квадратный брус шириной A?

import math

D = 20
a = 10  
flag = True
if D * math.sqrt(2) < a :
    flag = False
print(flag)