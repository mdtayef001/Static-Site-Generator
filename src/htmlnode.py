class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: object | None = None,
        props: object | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotADirectoryError("to_html method not implemented")

    def props_to_html(self) -> str:

        if self.props is None or self.props == {}:
            return ""

        return "".join(f' {k}="{v}"' for k, v in self.props.items())

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: object | None = None,
    ) -> None:
        super().__init__(tag, value, None, props)
