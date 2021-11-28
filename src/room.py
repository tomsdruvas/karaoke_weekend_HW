class Room:
    def __init__(self, name, size, current_guests):
        self.name = name
        self.size = size
        self.current_guests = current_guests
        self.songs = []


    def room_size(self):
        return len(self.current_guests)


    def check_guest_out(self):
        return self.current_guests.pop()

    def add_song(self, song):
        self.songs.append(song)

    def check_in(self, guest):
        self.current_guests.append(guest)