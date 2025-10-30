import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    #def test_blankeq(self):
    #    node1 = HTMLNode()
    #    node2 = HTMLNode()
    #    self.assertEqual(node1, node2)
    
    def test_no_prop(self):
        node1 = HTMLNode()
        test = node1.props_to_html()
        ans = None
        self.assertEqual(ans,test)

    def test_blankkey_blankval_prop(self):
        test_line = {"":"",}
        node1 = HTMLNode(props=test_line)
        test = node1.props_to_html()
        ans = " =\"\""

    def test_props_to_html(self):
        test_line = {"href": "https://www.google.com","target": "_blank",}
        node1 = HTMLNode(props=test_line)
        test = node1.props_to_html()
        ans =" href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(ans, test)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )       

    def test_to_html_with_two_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child1</span><span>child2</span></div>"
        )


if __name__ == "__main__":
    unittest.main()
