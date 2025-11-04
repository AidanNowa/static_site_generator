from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextType, TextNode
from blocktype import *
import re

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, props=["href"])
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", props=["src", "alt"])
    raise Exception("Invalid TextType")
     
def extract_markdown_images(text):
    matched = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #print(matched)
    return matched

def extract_markdown_links(text):
    #matched = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    matched = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)
    #print(matched)
    return matched

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:        
        original_text = node.text
        matches = extract_markdown_images(original_text)
        #print(f"Node: {node} --- Matches:{matches}")
        if matches == []:
            #print(f"No matches for node: {node}")
            node_list.append(node)
            continue
        if node.text == None:
            continue
        #for i in range(len(matches)):
        #sections = node.text.split(f"![{matches[i][0]}]({matches[i][1]})", 1)    
        text_sections = re.split(r'\!\[.*?\]\(.*?\)', original_text)
        if text_sections[-1] == '':
            text_sections = text_sections[:-1]
        #print(text_sections)
        
        j = 0 #image counter
        k = 0 #text counter
        #were starting with an image - add matches first
        if original_text[:2] == "![":
            for i in range(max(len(matches), len(text_sections))):
                #add image node when even (start with 0)
                if i % 2 == 0:
                    node_list.append(TextNode(matches[j][0], TextType.IMAGE, url=matches[j][1]))
                    j += 1                
                else:
                    node_list.append(TextNode(text_sections[k], TextType.TEXT))
                    k += 1
 
        else:
            for i in range(len(text_sections + matches)):
                #add image node when even (start with 0)
                if i % 2 != 0:
                    node_list.append(TextNode(matches[j][0], TextType.IMAGE, url=matches    [j][1]))
                    j += 1
                else:
                    node_list.append(TextNode(text_sections[k], TextType.TEXT))
                    k += 1

    if node_list[-1] == TextNode(" ", TextType.TEXT, None):
        node_list = node_list[:-1]
    #print(node_list)
    return node_list

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        original_text = node.text
        matches = extract_markdown_links(original_text)
        #print(matches)
        if matches == []:
            node_list.append(node)
            continue
        if node.text == None:
            continue
        #for i in range(len(matches)):
        #sections = node.text.split(f"![{matches[i][0]}]({matches[i][1]})", 1)    
        text_sections = re.split(r'\[.*?\]\(.*?\)', original_text)
        if text_sections[-1] == '':
            text_sections = text_sections[:-1]
        #print(text_sections)

        j = 0 #image counter
        k = 0 #text counter
        #were starting with an image - add matches first
        if original_text[0] == "[":
            for i in range(max(len(matches), len(text_sections))):
                #add image node when even (start with 0)
                if i % 2 == 0:
                    node_list.append(TextNode(matches[j][0], TextType.LINK, url=matches[j][1]))
                    j += 1
                else:
                    node_list.append(TextNode(text_sections[k], TextType.TEXT))
                    k += 1

        else:
            for i in range(len(text_sections + matches)):
                #add image node when even (start with 0)
                if i % 2 != 0:
                    node_list.append(TextNode(matches[j][0], TextType.LINK, url=matches[j][1]))
                    j += 1
                else:
                    node_list.append(TextNode(text_sections[k], TextType.TEXT))
                    k += 1
    
    if node_list[-1] == TextNode(" ", TextType.TEXT, None):
        node_list = node_list[:-1]

    return node_list

def markdown_to_blocks(markdown):
    block_list = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        #print(f"block is: {block}")
        if block != '':
            block_list.append(block.strip())
    return block_list    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(f"No matching cloing delimiter: {delimiter}")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        node_list.extend(split_nodes)
    return node_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def block_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED:
        return ulist_to_html_node(block)
    if block_type == BlockType.ORDERED:
        return olist_to_html_node(block)
    raise Exception("Invalid block type")
 
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise Exception(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)
 
def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise Exception("Invalid code block")
    #remove back ticks
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])
 
def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise Exception("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_html_node(block):
    items =block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        new_node = block_to_html_node(block, block_type)
        children.append(new_node)
    return ParentNode("div", children, None)





