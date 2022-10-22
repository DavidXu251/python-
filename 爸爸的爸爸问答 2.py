
def points(names):
    return [Point(name=x) for x in names]

class Point:
    all_obj=dict()
    def __init__(self,name='X'):
        if len(name)!=1:
            print('point name must be 1 character')
            print('but now it is:', name)
        
        self.name=name
        Point.all_obj[name]=self
        self.on_lines=set()
        
class Line:
    def __init__(self,names='AB'):
        self.have_points=set(
            points(names) )
    def add_point(points='A'):
        self.have_points.update(points(names))

'''
add:
    points ABCDEF
    line AB
    line CD
    line EACF

where:
    parallel AB CD
    angle AB EF 60

tell:
    angle ECD
'''
Line.add('AB')
Line.add('CD')
Line.add('EACF')

Line.get('AB').parallel(line.get('EF'))

Angle.value('EAB', 60)

print(Angle.all_obj['ACD'])
















