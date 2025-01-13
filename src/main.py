from textnode import *
from htmlnode import *

def main():
    #node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    node0 = HTMLNode()
    node = HTMLNode("<a>", "hey hoe", node0, {"href": "https://www.google.com"})
    #print(node)
    #print(node.props_to_html())

main()