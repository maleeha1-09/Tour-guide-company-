class TourCompany:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact      
    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Contact: {self.contact}")     
class Tour:
    def __init__(self, name, description, price, duration, guide):
        self.name = name
        self.description = description
        self.price = price
        self.duration = duration
        self.guide = guide       
    def display(self):
        print(f"Tour Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price}")
        print(f"Duration: {self.duration}")
        print(f"Guide: {self.guide}")
class MonthlyCourses:
    def __init__(self, name, description, price, duration):
        self.name = name
        self.description = description
        self.price = price
        self.duration = duration      
    def display(self):
        print(f"Course Name: {self.name}")
        print(f"You will learn: {self.description}")
        print(f"Price: {self.price}")
        print(f"Duration: {self.duration}")    
class Guide:
    def __init__(self, name, experience, rating):
        self.name = name
        self.experience = experience
        self.rating = rating   
    def display(self):
        print(f"Name: {self.name}")
        print(f"Experience: {self.experience} years")
class Ride:
    def __init__(self, type, price):
        self.type = type
        self.price = price     
    def display(self):
        print(f"Type: {self.type}")
        print(f"Price: {self.price}")       
class Booking:
    def __init__(self, customer_name, tour, ride, date):
        self.customer_name = customer_name
        self.tour = tour
        self.ride = ride
        self.date = date
    def display(self):
        print(f"Customer Name: {self.customer_name}")
        self.tour.display()
        self.ride.display()
        print(f"Date: {self.date}")
class Customer:
    def __init__(self, name, email, phone,bookedtour):
        self.name = name
        self.email = email
        self.phone = phone
        self.bookedtour = bookedtour
    def display(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Booked tour:{self.bookedtour}")
class BookingCourses:
    def __init__(self, customer_name, course, date):
        self.customer_name = customer_name
        self.course = course
        self.date = date
    def display(self):
        print(f"Customer Name: {self.customer_name}")
        self.course.display()
        print(f"Which date do you want to start: {self.date}")
while True:
    print("PK GUIDES AND tours")
    print("1.About us")  
    print("2.Information about tours")
    print("3.Information about monthly courses")
    print("4.Information about guides")
    print("5.Information about rides")
    print("6.Book your tour") 
    print("7.book a course")
    print("8.Your information") 
    i=int(input("Press from 1 to 7 to get required information : "))
    if i == 1:
        company = TourCompany("PK Guides & Tours","Multan","03000000000")
        company.display()
    elif i == 2:
        tour = Tour("Multan City Tour","Visit the historical and cultural sites of Multan",3000,"1 day","Ali Khan")
        tour.display()
        tour2 = Tour("Skardu Tour","Do mountain climbing and treakking",20000,"4 days","Wan Fateh")
        tour2.display()
    elif i == 3:
        course = MonthlyCourses("Tour guiding","Learn to guide tours ",10000,"2 week")
        course.display()
        course2 = MonthlyCourses("First Aid course","Learn to give first aid at any emergency",5000,"1 week")   
        course2.display()
    elif i == 4:
        guide = Guide("Ali Khan",5,4.8)
        guide.display()
        guide2 = Guide("Wan Fateh",6,4.9)
        guide2.display()
    elif i == 5:
        ride = Ride("Rickshaw Ride",1000)
        ride.display()
        ride = Ride("Car ride",1000)
        ride2.display()
    elif i == 6:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        customer = Customer(name, email, phone)
        tour = Tour("Multan City Tour","Visit the historical and cultural sites of Multan",3000,"1 day","Ali Khan")
        ride = Ride("Rickshaw Ride",1000)
        date = input("Enter your preferred date for the tour (DD/MM/YYYY): ")
        booking = Booking(customer.name, tour, ride, date)
        print("Your booking has been confirmed!")
        booking.display()
    elif i == 7:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        customer = Customer(name, email, phone)
        course = MonthlyCourses("Tour guiding","Learn to guide tours ",10000,"2 week")
        date = input("Enter your preferred date for the course (DD/MM/YYYY): ")
        booking = BookingCourses(customer.name, course, date)
        print("Your booking has been confirmed!")
        booking.display()  
    elif i == 8:
        print("Your tour information : ")
        customer1=Customer("ALISHBA","alishba@gmail.com","0909909","Sakardu tour") 
        customer1.display()
    else:
        print("Invalid input. Please enter a valid option.")
        continue
    endloop = input("Do you want to continue? (yes/no): ")
    if endloop.lower() != "yes":
        break