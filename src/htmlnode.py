class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented("nuh-uh")

    def props_to_html(self):
        if self.props is None:
            return "None"
        attributes = ""
        for key, value in self.props.items():
            attributes += f'{key}="{value}" '
        return attributes
    
    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props_to_html()}"