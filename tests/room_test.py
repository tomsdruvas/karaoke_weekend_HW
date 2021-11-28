import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.bob = Guest("Bob", 25, 100)
        self.john = Guest("John", 30, 200)
        self.current_guests = [self.bob, self.john]
        self.room_one = Room("Room One", 2, self.current_guests, 10)
        self.rap = Song("Rap")
        self.jazz = Song("Jazz")
        self.carl = Guest("Carl", 46, 500)
        self.rick = Guest("Rick", 18, 344)
        self.current_guests2 = [self.carl, self.john]

        self.room_two = Room("Room_Two", 3, self.current_guests2, 110)

    def test_room_has_name(self):
        self.assertEqual("Room One", self.room_one.name)

    def test_size_of_room(self):
        self.assertEqual(2, self.room_one.size)
    
    def test_room_full(self):
        self.assertEqual(self.room_one.size, self.room_one.room_size())

    def test_check_out_guests(self):
        self.room_one.check_guest_out()
        self.assertEqual(1, self.room_one.room_size())
    
    def test_song_list_start_empty(self):
        self.assertEqual([], self.room_one.songs)

    def test_add_songs_to_rooms(self):
        self.room_one.add_song(self.rap)
        self.room_one.add_song(self.jazz)
        self.assertEqual(2, len(self.room_one.songs))
    


    # def test_check_people_in_not_ok(self):
    #     self.room_two.check_in(self.carl)
    #     self.room_two.check_in(self.rick)
    #     self.assertEqual(3, self.room_one.room_size())
    
    def test_reduce_cust_cash(self):
        self.bob.reduce_customer_cash(self.room_one.price)
        self.assertEqual(90, self.bob.cash)
    
    def test_if_not_enough_cash(self):
        self.room_two.check_in(self.bob)
        self.assertEqual(2, self.room_two.room_size())

    def test_full_function(self):
        self.room_two.check_in(self.rick)
        self.assertEqual(3, self.room_two.room_size())

