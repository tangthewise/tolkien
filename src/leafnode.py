from htmlnode import HTMLNode

class LEAFNode(HTMLNode):
    def __init__(self, value, tag = None, props = None):
        super(LEAFNode, self).__init__(tag, value, None, props)

    def __repr__(self):        
        print(f"LEAFNode({self.value}. {self.tag}. {self.props})")

    def to_html(self):
        if self.value == None:
            raise ValueError()
        
        if self.tag == None or self.tag == "":
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    
    

