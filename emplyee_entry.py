class employee:
    def __init__(self,name,age,city,id):
        self.name=name
        self.age=age
        self.city=city
        self.id=id
        # number_of_employee = 0
    def detail(self):
        print(self.name,self.age,self.city,self.id)
        # Employee.number_of_employee += 1

emp1=employee('xyz',22,'knl',1234)
emp2=employee('abcd',23,"kml",12345)


# employee.detail(emp1)
# employee.detail(emp2)
emp1.detail()
emp2.detail()


emp2.detail()
