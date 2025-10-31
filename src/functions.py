from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextType, TextNode
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


   
def OLD_split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
        first_string = [] 
        inner_string = []
        last_string = []
        inner = False
        inner_exists = False
        for word in node.text.split():
            #start of inline element
            if delimiter == "**" and word[:2] == delimiter:
                inner = True
                inner_exists = True
                inner_string.append(word)
                if word[-2:] == delimiter:
                    inner = False
            elif delimiter == "**" and word[-2:] == delimiter:
                inner = False
                inner_string.append(word)
            elif word[0] == delimiter:
                inner = True
                inner_exists = True
                inner_string.append(word)
                if word[-1] == delimiter:
                    inner = False 
                #end of inline element
            elif word[-1] == delimiter:
                inner = False
                inner_string.append(word)
            #word is still in inline element
            elif inner == True:
                inner_string.append(word)
            #add to first string since inner does not exisit yet
            elif inner_exists == False:
                first_string.append(word)
            else:
                last_string.append(word)
        #never matched delimiter -> error
        if inner == True and word[-1] != delimiter:
            #print(node_list)
            #print(word)         
            raise Exception(f"No matching closing delimiter: {delimiter}")
        if first_string != []:
            #print(f"first_string: {first_string}")
            node_list.append(TextNode(" ".join(first_string) + " ", TextType.TEXT))
        if inner_string != []:
            #print(f"inner_string: {inner_string}")
            #print(f"delimiter: {delimiter}")
            if delimiter == "**":
                #print(f"ENTERED BOLD CASE with innerstring: {inner_string}")
                node_list.append(TextNode(" ".join(inner_string).replace("**", ""), TextType.BOLD))
            elif delimiter == "_":
                node_list.append(TextNode(" ".join(inner_string).replace("_", ""), TextType.ITALIC))
            elif delimiter == "`":
                node_list.append(TextNode(" ".join(inner_string).replace("`", ""), TextType.CODE))

        if last_string != []:
            #print(f"last_string {last_string}")
            node_list.append(TextNode(" " + " ".join(last_string), TextType.TEXT))
    #print(f"Node list from delimiter func: {node_list} with delimiter: {delimiter}")
    return node_list        
        
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

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


