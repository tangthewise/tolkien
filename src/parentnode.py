from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super(ParentNode, self).__init__(tag, None, children, props)

    def __repr__(self):        
        print(f"ParentNode({self.tag}, {self.children}, {self.props}")

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Missing tag")
        
        if self.children == None or len(self.children) == 0:
            raise ValueError("Missing children")
        
        result = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            result += child.to_html()

        result += f"</{self.tag}>"

        return result
    
    
    

