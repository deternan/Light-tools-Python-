# coding=utf8



def service(y):
    print('method output :', y)

service(123)


class Some:
    def __init__(self, x):
        self.x = x
    
    def service(self, y):
        print('class output :', self.x + y)


s1 = Some(10)
Some.service(s1, 2)

s2 = Some(20)
Some.service(s2, 2)
   