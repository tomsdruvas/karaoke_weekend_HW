import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.bob = Guest("Bob", 25, 100)
        self.john = Guest("John", 30, 200)
        self.current_guests = [self.bob, self.john]
        self.room_one = Room("Room One", 2, self.current_guests, 10)

    def test_guest_has_name(self):
        self.assertEqual(self.bob.name, "Bob")
    
    def test_guest_has_cash(self):
        self.assertEqual(self.john.cash, 200)

    def test_reduce_cust_cash(self):
        self.bob.reduce_customer_cash(self.room_one.price)
        self.assertEqual(90, self.bob.cash)