# coding: utf-8


class LazyProperty:

    def __init__(self, method):
        '''
        在实例化的时候，method是调用该装饰器的Test.resource方法，也就是调用装饰器的方法
        :param method:
        '''
        # <function Test.resource at 0x1032c9378>
        # 所以就是将方法付给了self.method属性
        self.method = method
        # resouce
        # 该属性是设置方法名
        self.method_name = method.__name__
        # print('function overriden: {}'.format(self.method))
        # print("function's name: {}".format(self.method_name))

    def __get__(self, obj, cls):
        '''
        obj:<__main__.Test object at 0x10c0a8748>
        cls:<class '__main__.Test'>
        :param obj:
        :param cls:
        :return:
        '''
        if not obj:
            return None
        # 此处没太看明白
        '''
        由于Test的def resource(self):需要传入一个self进来，也就是一个对象，所以此处需要传入一个obj（相当于self）
        '''
        value = self.method(obj)
        # print('value {}'.format(value))

        setattr(obj, self.method_name, value)
        return value


class Test:

    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))    # 代价大的
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # 做更多的事情。。。
    print(t.resource)
    print(t.resource)

if __name__ == '__main__':
    main()
