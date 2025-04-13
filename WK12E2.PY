#creating the class
class HotelRoom:

    def __init__(self, roomnumber, roomtype, isbooked=False):
        self.roomnumber = roomnumber
        self.roomtype = roomtype
        self.isbooked = isbooked
    

    def __str__(self):
        return f"Room{self.roomnumber} {self.roomtype} {'Booked' if self.isbooked else 'Available'}"

#method to book room
    def BookRoom(self):
        self.isbooked = True

#method to cancel room
    def CancelBooking(self):
        self.isbooked = False
    
#method for availability
    def RoomAvailability(self):
        print(self)
        #status = 'Booked' if self.isbooked else 'Available'
        #print(f" 'Room' {self.roomnumber} ({self.roomtype}): {status}")
    
#creating objects
r1 = HotelRoom(100, "King")
r2 = HotelRoom(200, "Suite")

#print
r1.RoomAvailability()
r2.RoomAvailability()