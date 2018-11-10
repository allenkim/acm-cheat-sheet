import math
import numbers

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
        self.y = other.y

    @staticmethod
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

