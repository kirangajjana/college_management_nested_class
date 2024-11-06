#building an college management system basic functionalities using nested classes and nested method concepts
class University:  #university Class
    def __init__(self,name,city,hostel):
        print("hello welcome to the university class")
        self.department=self.Department()
        self.name=name
        self.city=city
        self.hostel=hostel
    def info(self):
        print("hello welcome to the university campus")
        print(f"your gud name is {self.name}")
        print(f"your city is {self.city}")
        print(f"your hostel is {self.hostel}")


    class Department: #Department Class
        def __init__(self):
            print("hellop welcome to the department class")
            self.library=self.Library()
        def branch(self,branch,section):
            self.branch=branch
            self.section=section   
        class Library: #library Class
            def __init__(self):
                print("hello welcome to the library class")
college=University()