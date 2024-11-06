#building an college management system basic functionalities using nested classes and nested method concepts
class University:  #university Class
    def __init__(self,name,city,hostel): #instance method
        print("hello welcome to the university class")
        self.department=self.Department() #instance variables
        self.name=name #instance variable
        self.city=city #instance variable
        self.hostel=hostel
    def info(self):   #instance Method
        print("hello welcome to the university campus")
        print(f"your gud name is {self.name}") #printing instance variabl;e
        print(f"your city is {self.city}") #printing instance variable
        print(f"your hostel is {self.hostel}") #printing instance variable


    class Department: #Department Class
        def __init__(self): #instance method
            print("hellop welcome to the department class")
            self.library=self.Library() #instance variables
        def branch(self,branch,section): #instance method
            self.branch=branch #instance variable
            self.section=section #instance variable
        class Library: #library Class
            def __init__(self):
                print("hello welcome to the library class")
college=University()