class Train:
    company = "Indian Express"

    def __init__(self,name,number,seats,fare):
        self.name = name
        self.number = number
        self.seats = seats
        self.fare = fare

    def getInfo(self):
        print(f"The Train name is {self.name} , Train no : {self.number}")
        print(f"Fare of Ticket is {self.fare}")

    def availableSeats(self):
        if self.seats>0:
            print(f"Limited Seats are Available, You have Booked Your Ticket...Have a Safe Joruney")
            print(f"Your seat Number : {self.seats}")
            self.seats = self.seats-1
            print(f"Available Seats {self.seats}")
        else:
            print("Sorry ,There are no tickets available")

chennai = Train("Chennai Express",12345,200,30)

chennai.getInfo()
chennai.availableSeats()
chennai.getInfo()
chennai.availableSeats()
