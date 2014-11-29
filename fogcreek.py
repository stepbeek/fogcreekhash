# Solution to the fogcreek dehashing problem

import unittest

key = "acdegilmnoprstuw"

initial = 7

#the fogcreek hash function
def hash(s):
    h = initial
    for c in s:
        if not c in key:
            return -1
        h = 37 * h + key.index(c)
    return h

# Dehash function which checks for valid answer and reverses if valid
def dehash(h):
    rt = dehashfunct(h)
    if "!" in rt:
        return "!"
    else:
        return rt[::-1]

#Recursive function to dehash the problem
def dehashfunct(h):
    if h == initial:
        return ""
    elif h > initial:
        indx = h % 37
        return key[indx] + dehashfunct(((h - indx)/37))
    else: 
        return "!"



# Unittest cases for the fogcreek function
class TestHash (unittest.TestCase):
    def test_hash(self):
        self.assertEqual(680131659347, hash("leepadg"))
        
    def test_failedhash(self):
        self.assertEqual(-1, hash("acksjdjz"))

    def test_dehash(self):
        self.assertEqual("leepadg", dehash(680131659347))

    def test_faileddehash(self):
        self.assertEqual("!", dehash(0))

if __name__ == "__main__":
#    unittest.main()
    print dehash(945924806726376)
