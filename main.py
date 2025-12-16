from text_document import TextDocument

original = TextDocument("Hello", "Bold")
clone = original.clone()

print(original.text, original.style)
print(clone.text, clone.style)
