class Event:
    '''
    描述一个事件
    '''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    '''
    所有操作的基类，所有操作都要继承自该类
    '''

    def __init__(self, parent=None):
        '''
        默认的构造函数parent可以为None
        :param parent:
        '''
        self.parent = parent

    def handle(self, event):
        '''
        所有的子类，都继承自父类，都可能调用父类的handle方法
        handle方法会处理传入的事件
        :param event:
        :return:
        '''
        handler = 'handle_{}'.format(event)
        # 判断传入的事件，当前对象是否存在指定方法
        if hasattr(self, handler):
            # 取到当前类的指定方法
            method = getattr(self, handler)
            # 执行该方法
            # 对传入的event事件进行处理
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):

    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):

    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):

    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    '''
        由于实例化是通过名字来创建具体的事件
    '''
    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)

if __name__ == '__main__':
    main()
