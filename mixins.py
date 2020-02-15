class mixin_DS:
    def departament_ds(self):
        return 'Open DS department!'

class mixin_Dev:
    def department_dev(self):
        return 'Open development department!'

class mixin_Test:
    def department_test(self):
        return 'Open testing department!'


class Base_company:
    pass


class Company_dev(Base_company, mixin_Dev, mixin_Test):
    pass

class Company_ds(Base_company, mixin_DS, mixin_Test):
    pass