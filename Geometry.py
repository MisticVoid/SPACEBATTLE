epsilon = 1e-10

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