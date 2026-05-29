from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list['HTMLNode'], props: dict[str, str] = None) -> None:
        super().__init__(tag, None, children, props)
        
    def to_html(self):

        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
        
        if not self.children:
            raise ValueError("ParentNode must have at least one child.")
        
        

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __str__(self):
        return f"<{self.tag} {self.attributes}> with {len(self.children)} children"

