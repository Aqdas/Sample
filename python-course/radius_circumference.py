import math
radius = float (input ('Type the radius of a Circle: '))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print ('The area of a circle is ',round(area, 2))
print ('The circumference of a circle is ', round (circumference, 2))