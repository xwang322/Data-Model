#!/usr/bin/python -B

import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def _square_brackets(self, key):
        return self.trie[key]
    
    def test_addDict(self):
		self.trie["Insten"] = 164265
		self.trie["Coveroo"] = 43689
		self.trie["Superb Choice"] = 24540
		for k in self.trie:
			self.assertTrue(k in self.trie)
			self.assertEquals(164265, self.trie.get("Insten"))
		
		kset = self.trie.keys()
		self.assertTrue("Superb Choice" in kset)
		self.assertEquals(3, len(kset))
		#self.assertTrue("Superb" in kset)
		kset = self.trie.keys("Superb")
		self.assertTrue("Superb Choice" in kset)
		self.assertEquals(1, len(kset))
		self.assertTrue("Superb" in kset)

if __name__ == '__main__':
        unittest.main()
