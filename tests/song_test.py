import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.rap = Song("Rap")
        self.jazz = Song("Jazz")
        
