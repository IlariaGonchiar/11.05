import math

def circle_intersection_area(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if distance >= r1 + r2:
        return 0.0
    elif distance <= abs(r1 - r2):
        if r1 < r2:
            return math.pi * r1**2
        else:
            return math.pi * r2**2
    
    angle1 = math.acos((r1**2 + distance**2 - r2**2) / (2 * r1 * distance))
    angle2 = math.acos((r2**2 + distance**2 - r1**2) / (2 * r2 * distance))
    
    sector_area1 = 0.5 * angle1 * r1**2
    sector_area2 = 0.5 * angle2 * r2**2
    
    triangle_area1 = 0.5 * r1**2 * math.sin(2 * angle1)
    triangle_area2 = 0.5 * r2**2 * math.sin(2 * angle2)
    
    intersection_area = sector_area1 + sector_area2 - triangle_area1 - triangle_area2
    
    return intersection_area

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

result = circle_intersection_area(x1, y1, r1, x2, y2, r2)
print(result)
