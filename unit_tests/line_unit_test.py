from line import Line
from line import Point

print 'testing line'

print 'testing line is set...'
l = Line()
print 'test not set'
assert not l.line_is_set()
l.set_line_by_coord(0, 0, 1, 1)
print 'test set'
assert l.line_is_set()
l = Line()
p1 = Point()
p2 = Point()
l.set_line_by_point(p1, p2)
print 'test setting by point not set'
assert not l.line_is_set()
p1.set_coord(0, 0)
p2.set_coord(1, 1)
assert l.line_is_set()
print 'test line with same start and end'
p2.set_coord(0, 0)
assert not l.line_is_set()

print 'testing get line...'
l = Line()
p1 = Point()
p1.set_coord(0, 0)
p2 = Point()
p2.set_coord(1, 1)
l.set_line_by_point(p1, p2)
print 'test points are same'
assert l.get_line() == (p1.get_coord(), p2.get_coord())
print 'test points are not same'
p3 = Point()
p3.set_coord(2, 2)
assert not l.get_line() == (p1.get_coord(), p3.get_coord())

print 'testing slope...'
l = Line()
p1 = Point()
p1.set_coord(0, 0)
p2 = Point()
p2.set_coord(1, 1)
l.set_line_by_point(p1, p2)
print 'test (0,0), (1,1) = 1'
assert l.slope() == 1
print 'test (-1,-1), (1,1) = 1'
p1.set_coord(-1, -1)
assert l.slope() == 1
print 'test (0,1), (1,0) = -1'
p1.set_coord(0, 1)
p2.set_coord(1, 0)
assert l.slope() == -1
print 'test (0,0), (1,0) = 0'
p1.set_coord(0, 0)
p2.set_coord(1, 0)
assert l.slope() == 0
print 'test (1.5, 1.5),(1.5,2.5) = inf'
p1.set_coord(1.5, 1.5)
p2.set_coord(1.5, 2.5)
assert l.slope() == float('inf')
print 'test (1.23456, 1.23456),(1.73456, 1.48456) = .5'
p1.set_coord(1.23456, 1.23456)
p2.set_coord(1.73456, 1.48456)
assert l.slope() == float(.5)

print 'testing do lines intersect...'


def line_inter_test(p1x, p1y,
                    p2x, p2y,
                    p3x, p3y,
                    p4x, p4y):
    print 'test if line ((' + str(p1x) + ', ' + str(p1y) + '), (' +\
          str(p2x) + ', ' + str(p2y) + ')), ((' + str(p3x) + ', ' + str(p3y) + '), (' + \
          str(p4x) + ', ' + str(p4y) + ')) intersects'
    pa = Point()
    pb = Point()
    pc = Point()
    pd = Point()
    l1 = Line()
    l2 = Line()
    pa.set_coord(p1x, p1y)
    pb.set_coord(p2x, p2y)
    pc.set_coord(p3x, p3y)
    pd.set_coord(p4x, p4y)
    l1.set_line_by_point(pa, pb)
    l2.set_line_by_point(pc,pd)
    return l1.do_lines_intersect(l2)

print 'test lines that do not intersect'
assert not line_inter_test(0, 0, 1, 0, 0, 1, 1, 1)
assert line_inter_test(0, 0, 1, 1, 1, 0, 0, 1)
