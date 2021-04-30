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


def inBox(p1,p2,x,y):
    """check if point in box with opposite corners p1 and p2"""
    return (p1[0]<=x<=p2[0] or p1[0]>=x>=p2[0]) and (p1[1]<=y<=p2[1] or p1[1]>=y>=p2[1])

def squarePointDis(p1,p2):
    """return square of distance between points"""
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])

def pointDis(p1,p2):
    """return distance between points"""
    return sqrt(squarePointDis(p1,p2))

def crossPoint(A,B,C,p1,p2,po):
    """return crossing point between line and section or (None,None) if point not exist or closest to origin pint if line overlapping"""
    A2,B2,C2=twoPointToLine(p1,p2)
    y=(A*C2-A2*C)/(A2*B-A*B2)
    x=(B*y+C)/(-A)
    if A2*B==A*B2:
        if A*C2==A2*C:
            if squarePointDis(p1,po)<squarePointDis(p2,po):
                return p1
            else:
                return p2
        else:
            return None,None
    if inBox(p1,p2,x,y):
        return x,y
    return None,None




