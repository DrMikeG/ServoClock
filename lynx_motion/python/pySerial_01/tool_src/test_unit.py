import unittest
import os

from advent import convertLineDirectionToGridPosition
from advent import processInputFile
from advent import conway
from advent import countBlack
from advent import countNeighbours

class TestStringMethods(unittest.TestCase):

    def test_simpleLines(self):
        
        tile = convertLineDirectionToGridPosition("se")
        self.assertEqual((0,1),tile)
        #esew flips a tile immediately adjacent to the reference tile,        
        tile = convertLineDirectionToGridPosition("esew")
        self.assertEqual((0,1),tile)
        tile = convertLineDirectionToGridPosition("ew")
        self.assertEqual((0,0),tile)
        #  and a line like nwwswee flips the reference tile itself.
        tile = convertLineDirectionToGridPosition("nwwswee")
        self.assertEqual((0,0),tile)

    def test_testSimpleGrid(self):
        tiles = {}
        tiles[(0,0)] = "Black"
        self.assertEqual(1,countBlack(tiles))
        conway(tiles)
        self.assertEqual(0,countBlack(tiles))

    def test_testSimpleGrid01(self):
        tiles = {}
        tiles[(0,0)] = "Black"
        tiles[(0,1)] = "Black"
        self.assertEqual(2,countNeighbours(tiles,(1,0)))


    def test_testFile(self):
        input_path = os.path.join(os.path.dirname(__file__),"test_input.txt")
        tiles = processInputFile(input_path)
        self.assertEqual(10,countBlack(tiles))
        conway(tiles)
        self.assertEqual(15,countBlack(tiles))
        conway(tiles)
        self.assertEqual(12,countBlack(tiles))
        conway(tiles)
        self.assertEqual(25,countBlack(tiles))
        conway(tiles)
        self.assertEqual(14,countBlack(tiles))

    def test_testFile100(self):
        input_path = os.path.join(os.path.dirname(__file__),"test_input.txt")
        tiles = processInputFile(input_path)
        self.assertEqual(10,countBlack(tiles))
        
        for _ in range(100):
            conway(tiles)
        self.assertEqual(2208,countBlack(tiles))

if __name__ == '__main__':
    unittest.main()