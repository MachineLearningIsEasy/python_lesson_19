class Someclass:
    def __init__(self):
        self.my_attr = 1

class SomeclassWithSlots:
    __slots__ = ('my_attr', 'only_my_attr')
    def __init__(self):
        self.my_attr = 1


if __name__ == '__main__':
    # obj = Someclass()
    # obj.not_my_attr = -1
    # print(obj.my_attr, obj.not_my_attr)
    #
    # print(dir(obj))
    #
    # print(obj.__dict__['my_attr'], obj.__dict__['not_my_attr'])
    obj_slots = SomeclassWithSlots()
    obj_slots.only_my_attr = lambda x: x**2
    print(dir(obj_slots))
    #print(obj_slots.only_my_attr(3))