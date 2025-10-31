import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text  node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_difftext(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a diff node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_defaulturl(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)         
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diffurl(self):
        node = TextNode("test text", TextType.ITALIC, url="https://dumb.com")
        node2 = TextNode("test text", TextType.ITALIC)
        #print(f"Node1: {node}, Node2: {node2}")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

