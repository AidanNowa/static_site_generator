class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return None
        #kv_pairs = []
        #for key in self.props.keys():
        #    kv_pairs.append(f"{key}={props[key]}")
        #return " ".join(kv_pairs)
        all_props = ""
        for key in self.props.keys():
            all_props = all_props + f" {key}=\"{self.props[key]}\""
        return all_props

    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value) #call parent HTMLNode constructor
        children = None #prevent any child nodes

    def to_html(self):
        if self.value == None:
            raise ValueError("All Leaf Nodes must have a value.")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children)
        value = None
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("All Parent Nodes must have a tag.")
        if self.children == None:
            raise ValueError("All Parent Nodes must have a child.")
        
        child_values = ''
        for child in self.children:
            child_values += child.to_html()

        return f"<{self.tag}>{child_values}</{self.tag}>"







