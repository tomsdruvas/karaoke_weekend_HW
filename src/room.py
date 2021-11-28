class Room:
    def __init__(self, name, size, current_guests, price):
        self.name = name
        self.size = size
        self.current_guests = current_guests
        self.price = price
        self.songs = []


    def room_size(self):
        return len(self.current_guests)


    def check_guest_out(self):
        return self.current_guests.pop()

    def add_song(self, song):
        self.songs.append(song)
    
    def reduce_customer_cash(self, amount):
        self.cash -= amount

    def check_in(self, guest):
        if self.room_size() <= 3:
            if self.price < guest.cash:
                self.current_guests.append(guest)