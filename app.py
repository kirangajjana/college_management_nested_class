#building an college management system basic functionalities using nested classes and nested method concepts
class University:  #university Class
    def __init__(self):
        print("hello welcome to the university class")
        self.department=self.Department()
    class Department: #Department Class
        def __init__(self):
            print("hellop welcome to the department class")
            self.library=self.Library()
        class Library: #library Class
            def __init__(self):
                print("hello welcome to the library class")
college=University()