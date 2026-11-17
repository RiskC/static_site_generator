
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_images_links import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode



def text_to_textnodes(text):
    temp_obj = TextNode(text, TextType.TEXT, None)
    text1 = split_nodes_delimiter([temp_obj], "**", TextType.BOLD)
    
    text2 = split_nodes_delimiter(text1, "_", TextType.ITALIC)
    
    text3 = split_nodes_delimiter(text2, "`", TextType.CODE)
    
    text4 = split_nodes_image(text3)
    
    text5 = split_nodes_link(text4)
    
    return text5

   
