epsilon = 1e-12
from math import sin,cos,sqrt

def det(A, B, C):
    return (A[0]*B[1] + B[0]*C[1] + C[0]*A[1] - A[0]*C[1] - A[1]*B[0] - B[1]*C[0])


def orient(A, B, C, eps = epsilon):
    x = det(A, B, C)
    if (x > eps):
        return 1
    elif (x > -eps):
        return 0
    else:
        return -1


def inPolygon(p, polygon, eps = epsilon):           #convex polygons only
    """ returns True if point is inside polygon """
    side = orient(polygon[-1], polygon[0], p, eps)
    if side == 0:
        return True
    for i in range(1, len(polygon)):
        if side != orient(polygon[i-1], polygon[i], p, eps):
            return False
    return True


def polygonsCollide(p1, p2):
    """ returns True if polygons collide
        use points"""
    for point in p1:
        if inPolygon(point, p2):
            return True, point, p2

    for point in p2:
        if inPolygon(point, p1):
            return True, point, p1

    return False, None, None

def polygonsCollide2(p1, p2):
    """ returns True if polygons collide
        use segments """
    for i in range (len(p1)):
        for j in range (len(p2)):
            if(intersect(p1[i-1],p1[i],p2[j-1],p2[j])):
                return True
    return False



def rotatePoint(pointX,pointY,angle)->tuple[float,float]:
    """return coordinates of point (pointX,pointY) around point (0,0) by angle(in radians) clockwise"""
    s = -sin(angle)
    c = cos(angle)
    x = pointX * c - pointY * s
    y = pointX * s + pointY * c
    return x,y

def twoPointToLine(p1,p2):
    """return parameters for line"""
    if p2[0]==p1[0]:
        a=0
    else:
        a = (p2[1]-p1[1])/(p1[0]-p2[0])
    c = p1[1]+a*p1[0]
    return a,1,-c

def distPointFromLine(A,B,C,x,y):
    """return distans of a point from line with parameters A,B,C"""
    return abs(A*x+B*y+C)/sqrt(A**2+B**2)


def dist(p1, p2 ,p3):
    """ (p1, p2) - line   p3 - point"""
    if p2[0]==p1[0]:
        return abs(p3[0]-p2[0])
    if p2[1]==p1[1]:
        return abs(p3[1]-p2[1])

    return distPointFromLine( *twoPointToLine(p1,p2), p3[0], p3[1] )

def intersect(A,B,C,D) -> bool:
    """check if segment AB intersects with CD"""
    return orient(A,B,D) != orient(A,B,C) and orient(C,D,A) != orient(C,D,B)

