# College Management System
 ### This project is a simple College Management System implemented in Python, using Object-Oriented Programming (OOP) principles, particularly focusing on nested classes and nested methods concepts.

## The system consists of three main components:

- University: The main class representing the college.
- Department: A nested class within University representing a college department.
- Library: A nested class within Department representing the department's library.


# Features
- Display basic details about the university.
- Handle department information within the university.
- Manage library operations (e.g., adding books) within each department.


## Class Definitions and Methods
- University Class
- Static Variables:
- college: 
### The name of the university (e.g., "National Institute of Technology Sikkim").

- branch: The branch location (e.g., "Ravangla").
Instance Variables:

- name: The name of the university representative (e.g., "Kiran Gajjana").

- city: The city of the representative (e.g., "Hyderabad").

- hostel: Hostel name of the representative.

- Methods:
__init__(self, name, city, hostel): Constructor that initializes the university details and creates an instance of Department.
- display(self): Displays the university's name, branch, representative, city, and hostel.
Department Class

-  A nested class within University that represents a department within the university.
Instance Variables:
library: Creates an instance of Library class.
Methods:
__init__(self): Constructor that initializes the department and creates an instance of Library.
branch(self, branch, section): Sets the department branch and section information.
Library Class

- A nested class within Department that represents a library in the department.

- Instance Variables:
- book: An example attribute for adding books to the library.
## Methods:
- __init__(self): Initializes the library.
- add_book(self, a): Calls the display() method of the University class, displaying university information.
- remove_book(self): Placeholder method for potential future implementation of book removal.
# User Interaction
- The program interacts with the user through a menu-based interface, offering the following options:


- University (U): Displays university details by calling display() on the University instance.

- Department (D): Placeholder for department-related functionalities.

- Library (L): Accesses the Library class's add_book() method, displaying university details through the library's nested structure.

- Exit (E): Exits the program.