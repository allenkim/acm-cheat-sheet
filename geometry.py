import math
import numbers

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

EPS=1e-6
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if abs(self.x - other.x) > EPS:
            return self.x < other.x

        return self.y < other.y

    def __eq__(self, other):
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS

    def set(self, other):
        self.x = other.x
        self.y = other.y @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

    @staticmethod
    def rotate(p, theta): # theta is in radians, rotate w.r.t origin
        return Point(p.x * math.cos(theta)  - p.y * math.sin(theta),
                p.x * math.sin(theta) + p.y * math.cos(theta))

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __repr__(self):
        return str(self)

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "Line({}, {}, {})".format(self.a, self.b, self.c)

    def __repr__(self):
        return str(self)

    @staticmethod 
    def from_points(p1, p2):
        if abs(p1.x - p2.x) < EPS:
            return Line(1, 0, -p1.x)
        else:
            a = -(p1.y - p2.y)/(p1.x - p2.x)
            b = 1
            c = -(a * p1.x) - p1.y
            return Line(a, b, c)

    @staticmethod
    def are_parallel(l1, l2):
        return abs(l1.a - l2.a) < EPS and abs(l1.b - l2.b) < EPS

    def __eq__(self, other):
        return Line.are_parallel(self, other) and self.c == other.c

    @staticmethod
    def intersection(l1, l2):
        if (Line.are_parallel(l1, l2)):
            return None

        x = (l2.b * l1.c - l1.b * l2.c) / (l2.a * l1.b - l1.a * l2.b)
        y = -(l1.a * x + l1.c) if (abs(l1.b) > EPS) else (l2.a * x + l2.c)
            
        return Point(x, y)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __repr__(self):
        return str(self)

    @staticmethod
    def from_points(a, b): # vector from a-> b
        return Vector(b.x - a.x, b.y - a.y)

    def __mul__(self, k):
        if isinstance(k, numbers.Number):
            return Vector.scale(self, k)
        
        return Vector.dot_product(self, k)

    def __mod__(self, v): # cross product: % kind of looks like an 'x' if you squint hard enough
        return Vector.cross_product(self, v)


    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def magnitude(self):
        return math.sqrt(self * self)

    @staticmethod
    def scale(v, k):
        return Vector(v.x * k, v.y * k)

    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    @staticmethod
    def cross_product(a, b):
        return a.x * b.y - a.y * b.x

    @staticmethod
    def translate_point(p, v):
        return Point(p.x + v.x, p.y + v.y)


def distance_to_line(p, a, b, c=Point(0, 0)): # distance. closest point returned by ref in c
    ap = Vector.from_points(a, p)
    ab = Vector.from_points(a, b)
    u = (ap * ab)/(ab * ab)
    c.set(Vector.translate_point(a, ab * u))
    return Point.distance(p, c), c

def distance_to_line_segment(p, a, b, c=Point(0, 0)):
    ap = Vector.from_points(a, p)
    ab = Vector.from_points(a, b)
    u = (ap * ab) / (ab * ab)
    if u < 0:
        c.set(a)
        return Point.distance(p, a)
    elif u > 1:
        c.set(b)
        return Point.distance(p, b)

    return distance_to_line(p, a, b, c)

def angle(a, o, b): # returns angle aob in radians
    oa = Vector.from_points(o, a)
    ob = Vector.from_points(o, b)

    if (oa * oa) == 0 or (ob * ob) == 0:
        raise ValueError("Duplicate point in ({}, {}, {})".format(a, o, b))

    return math.acos((oa * ob) / math.sqrt((oa * oa) * (ob * ob)))

def is_counter_clockwise(p, q, r): # returns true if r is on the left side of the line pq
    return Vector.from_points(p, q) % Vector.from_points(p, r) > 0

def is_collinear(p, q, r): # returns true if r is on the same line as the line pq
    return abs(Vector.from_points(p, q) % Vector.from_points(p, r)) < EPS

def inside_circle(p, c, r): # returns 0 if inside circle, 1 if on border, 2 if outside
    dx = p.x - c.x
    dy = p.y - c.y
    euc = dx**2 + dy**2
    rs = r**2
    return 0 if euc < rs else (1 if euc == rs else 2)

# returns the centers of the circle that goes through p1 and p2 with radius r
def circle_from_points(p1, p2, r): 
    def center_finder(p1, p2, r):
        d2 = (p1.x - p2.x)**2 + (p1.y - p2.y)**2
        det = r**2/d2 - 0.25
        if det < 0:
            return None

        h = math.sqrt(det)
        return Point((p1.x + p2.x) * 0.5 + (p1.y - p2.y) * h,
                (p1.y + p2.y) * 0.5 + (p2.x - p1.x) * h)

    return center_finder(p1, p2, r), center_finder(p2, p1, r)

class Triangle:
    @staticmethod
    def perimeter(ab, bc, ca):
        return ab + bc + ca

    @staticmethod
    def area(ab, bc, ca):
        s = .5 * Triangle.perimeter(ab, bc, ca)
        return math.sqrt(s * (s - ab) * (s - bc) * (s - ca))

    @staticmethod
    def radius_inscribed_circle(ab, bc, ca):  # returns the rabdius of the inscaribced caircale
        return Triangle.area(ab, bc, ca) / (0.5 * Triangle.perimeter(ab, bc, ca))

    @staticmethod
    def get_inscribed_circle(p1, p2, p3):
        ab = Point.distance(p1, p2)
        bc = Point.distance(p2, p3)
        ca = Point.distance(p3, p1)
        r = Triangle.radius_inscribed_circle(ab, bc, ca)
        if abs(r) < EPS:
            return None

        ratio = Point.distance(p1, p2) / Point.distance(p1, p3)
        p = Vector.translate_point(p2, Vector.from_points(p2, p3) * (ratio / (1 + ratio)))
        l1 = Line.from_points(p1, p)

        ratio = Point.distance(p2, p1) / Point.distance(p2, p3)
        p = Vector.translate_point(p1, Vector.from_points(p1, p3) * (ratio / (1 + ratio)))
        l2 = Line.from_points(p2, p)

        c = Line.intersection(l1, l2)
        return c, r

    @staticmethod
    def radius_circumscribed_circle(ab, bc, ca):
        return (ab * bc * ca)/ (4 * Triangle.area(ab, bc, ca)) 

# center point of circumscribed circle is meeting point of triangle's perpendicular bisectors
# perpendicular bisectors cut the angle of a triangle in such a way that any line drawn from
# the bisector to the side is pi/2 radians

class Polygon:
    # p is a list of points in clockwise or counterclockwise order
    # p[0] must be equal to p[-1]
    @staticmethod
    def perimeter(p):
        r = 0
        for i in range(len(p) - 1):
            r += Point.distance(p[i], p[i + 1])

        return r

    # area is half the determinant of the matrix:
    # [[x0, y0], [x1, y1], [x2, y2]...[xn, yn]]
    # p is a list of points in clockwise or counterclockwise order
    # p[0] must be equal to p[-1]
    @staticmethod
    def area(p):
        r = 0
        for i in range(len(p) - 1):
            x1, x2 = p[i].x, p[i + 1].x
            y1, y2 = p[i].y, p[i + 1].y
            r += (x1 * y2 - x2 * y1)

        return abs(r) / 2

    @staticmethod
    def is_convex(p):
        sz = len(p)
        if sz <= 3:
            return False

        is_left = is_counter_clockwise(p[0], p[1], p[2])
        for i in range(1, sz - 1):
            if is_counter_clockwise(p[i], p[i + 1], p[1 if i + 2 == sz else i + 2]) != is_left:
                return False

        return True

    # checks if point pt is in the polygon p
    @staticmethod
    def in_polygon(pt, p):
        if len(p) == 0:
            return False

        s = 0
        for i in range(len(p) - 1):
            if is_counter_clockwise(pt, p[i], p[i + 1]):
                s += angle(p[i], pt, p[i + 1])
            else:
                s -= angle(p[i], pt, p[i + 1])

        return abs(abs(s) - 2*math.pi) < EPS

    # cut polygon q using line segment a-b
    @staticmethod
    def cut_polygon(a, b, Q):
        # line segment p-q intersects with lien A-B
        def line_intersect_segment(p, q, A, B):
            a = B.y - A.y
            b = A.x - B.x
            c = B.x * A.y - A.x * B.y
            u = abs(a * p.x + b * p.y + c)
            v = abs(a * q.x + b * q.y + c)
            return Point((p.x * v + q.x * u)/(u + v), (p.y * v + q.y * u) /(u + v))
        P = []
        for i in range(len(Q)):
            left1 = Vector.from_points(a, b) % Vector.from_points(a, Q[i])
            left2 = 0
            if i != len(Q) - 1:
                left2 = Vector.from_points(a, b) % Vector.from_points(a, Q[i + 1])
            if left1 > -EPS:
                P.append(Q[i]) # Q[i] is on the left of ab
            if left1 * left2 < -EPS:
                P.append(line_intersect_segment(Q[i], Q[i + 1], a, b))

        if len(P) != 0 and not (P[0] == P[-1]):
            P.append(P[0])

        return P

    @staticmethod
    def convex_hull(P):
        def angle_cmp_generator(pivot):
            def angle_cmp(a, b):
                if is_collinear(pivot, a, b):
                    da = Point.distance(pivot, a)
                    db = Point.distance(pivot, b)
                    return -1 if da < db else (0 if da == db else 1)

                d1x, d1y = a.x - pivot.x, a.y - pivot.y
                d2x, d2y = b.x - pivot.x, b.y - pivot.y

                theta1 = math.atan2(d1y, d1x)
                theta2 = math.atan2(d2y, d2x)
                return -1 if theta1 < theta2 else (0 if theta1 == theta2 else 1)

            return angle_cmp

        n = len(P)
        if n <= 3:
            if not (P[0] == P[-1]):
                P.append(P[0])
            return P

        P0 = 0
        for i in range(n):
            if P[i].y < P[P0].y or (P[i].y == P[P0].y and P[i].x > P[P0].x):
                P0 = i

        P[0], P[P0] = P[P0], P[0]
        P = sorted(P, key=cmp_to_key(angle_cmp_generator(P[0])))
        S = []
        S.append(P[-1])
        S.append(P[0])
        S.append(P[1])
        i = 2
        while i < n:
            j = len(S) - 1
            if is_counter_clockwise(S[j - 1], S[j], P[i]):
                S.append(P[i])
                i += 1
            else:
                S.pop()

        return S


# Art Gallery Problem
# Given: 
# polygon P to describe the art gallery
# a set of pointsS to describe the guards where each guard is represented by a point in P
# a rule that a point A in S can guard another point B in P iff (A in S), (B in P), and
# a line segment AB is contained in P
# a question whether all points in P are guarded by S
# 4 Variants:
# 1) Determine the upper bound of the smallest size of set S
# 2) Determine if there exists a critical point C in polygon P and there exists another point D
# in P such that if the guard is not at position C, the guard cannot protect point D
# 3) Determine if the polygon P can be guarded with just one guard
# 4) Determine the smallest size of set S if the guards can only be placed at the vertices
# of polygon P and only the verticies need to be guarded
# Solutions:
# 1) floor(n/3) are always sufficient and sometimes necessary to guard a simple polygon with n vertices
# 2) The solution for variant 2 involves testing if polygon P is concave (and thus has a critical point). 
# We can use the negation of isConvex
# The solution for variant 3 can be hard if one has not seen the solution before. We can use the
# cutPolygon function. We cut polygon P with all lines formed by the edges in P in counterclockwise
# fashion and retain the left side at all times. If we simply have a non-empty polygon at the end
# one guard can be placed in the non-empty polygon which can protect the entire polygon P
# The solution for variant 4 involves the computation of the minimum vertex cover of of the
# "visibility" graph of polygon P. In general this is another NP-hard problem

# Great Circle
# The Great Circle Distance between any two points is the shortest distance along a path on the
# surface of the sphere. This path is an arc of the Great-Circle of that sphere that pass 
# through the two points. The Great circle cuts the sphere into two equal hemispheres
# to find the great-circle distance, we find the central angle AOB
# of the great-circle where O is the center of the great-circle. We can then determine
# the length of the arc A-B, which is the required Great-Circle distance
def great_circle_distance(plat, plong, qlat, qlong, radius):
    plat *= math.pi / 180
    plong *= math.pi/ 180
    qlat *= math.pi / 180
    qlong *= math.pi / 180
    acos = math.acos
    cos = math.cos
    sin = math.sin
    return radius * acos(cos(plat)*cos(plong)*cos(qlat)*cos(qlong) +
            cos(plat)*sin(plong)*cos(qlat)*sin(qlong)+
            sin(plat)*sin(qlat))
