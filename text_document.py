from document import Document

class TextDocument(Document):
    def __init__(self, text, style):
        self.text = text
        self.style = style
