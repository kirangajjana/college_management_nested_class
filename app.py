#building an college management system basic functionalities using nested classes and nested method concepts
class University:  #university Class
    college="National Institute of Technology Sikkim" #static variable
    branch="Ravangla" # static variable
    def __init__(self,name,city,hostel): #instance method
        print("hello welcome to the university class")
        self.department=self.Department() #instance variables
        self.name=name #instance variable
        self.city=city #instance variable
        self.hostel=hostel
    def display(self):
        print(f"college {University.college}")
        print(f"branch {University.branch}")
        print(f"hello mr {self.name}")
        print(f"City {self.city}")
        print(f"hostel {self.hostel}")    


    class Department: #Department Class
        def __init__(self): #instance method
            print("hellop welcome to the department class")
            self.library=self.Library() #instance variables
        def branch(self,branch,section): #instance method
            self.branch=branch #instance variable
            self.section=section #instance variable
        class Library: #library Class
            def __init__(self): #instance method
                print("hello welcome to the library class")
                self.book="new"
            def add_book(self,a): #instance method
                a.display()
                
            def remove_book(self): #instance method
                pass    
college=University("kiran gajjana","hyderabad","nit1")
d=college.Department()
e=d.Library()
e.add_book(college)
