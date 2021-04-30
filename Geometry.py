epsilon = 1e-10
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
    side = orient(polygon[-1], polygon[0], p, eps)
    if side == 0:
        return False
    for i in range(1, len(polygon)):
        if side != orient(polygon[i-1], polygon[i], p, eps):
            return False
    return True


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





