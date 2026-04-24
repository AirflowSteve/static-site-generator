import unittest
from htmlnode import HTMLNode

props_to_test = {
    "target" : "_blank",
    "href" : "www.whar.bruh",
    "alt" : "this is a test"
}

class TestTextNode(unittest.TestCase):
    def test_none_nodes(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "tag = None, value = None, children = None, props = None")
    
    def test_props(self):
        node = HTMLNode("a", "uh-uh", None, props_to_test)
        self.assertEqual(
            repr(node), 
            'tag = a, value = uh-uh, children = None, props = target="_blank" href="www.whar.bruh" alt="this is a test" '
            )
    
    def test_all_work(self):
        node = HTMLNode("a", "oh well", "meh", props_to_test)
        self.assertEqual(
            repr(node), 
            'tag = a, value = oh well, children = meh, props = target="_blank" href="www.whar.bruh" alt="this is a test" '
            )
