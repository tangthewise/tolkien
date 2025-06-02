class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        print("Calling __repr__")
        print(f"HTMLNode({self.tag}. {self.value}. {self.children}. {self.props})")

    def to_html(self):
      raise NotImplementedError()
    
    def _map_prop_to_string(self, prop_name, prop_value):
        return f" {prop_name}=\"{prop_value}\""

    def props_to_html(self):
        properties = list()
        if self.props != None:
            for property in self.props:
                properties.append(self._map_prop_to_string(property, self.props[property]))
        
        return "".join(properties)
    


