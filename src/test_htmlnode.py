import unittest
from htmlnode import HTMLNode, LeafNode

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
            'tag = a, value = uh-uh, children = None, props = target="_blank" href="www.whar.bruh" alt="this is a test"'
            )
    
    def test_all_work(self):
        node = HTMLNode("a", "oh well", "meh", props_to_test)
        self.assertEqual(
            repr(node), 
            'tag = a, value = oh well, children = meh, props = target="_blank" href="www.whar.bruh" alt="this is a test"'
            )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        
        self.assertEqual(node.to_html(), "Hello, world!")