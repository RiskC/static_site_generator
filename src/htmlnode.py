class HTMLNode():
    def __init__(self, tag: None | str = None, value: None | str = None, children: None | list["HTMLNode"] = None, props: None | dict[str,str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        #child classes will override this method to render themselves as html
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if not self.props:
            return ''
        result = []
        for key in self.props:
            result.append(f' {key}="{self.props[key]}"')

        return ''.join(result)

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: None | dict[str, str] = None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        if self.props:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: None | dict[str,str] = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node does not have a tag")
        if not self.children:
            raise ValueError("Parent node has no children; children required for parent node")
        
        result = []

        for child in self.children:
            result.append(child.to_html())
        results = ''.join(result)

        return f'<{self.tag}{self.props_to_html()}>{results}</{self.tag}>'

    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'


