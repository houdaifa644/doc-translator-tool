from docx import Document

# load the existing document
doc = Document("docs/example.docx")

# go through each paragraph in the document
for para in doc.paragraphs:
    para.text = para.text.upper()  # convert text to uppercase

# save the result in a new file
doc.save("docs/exemple_traduit.docx")

print("file translated and saved successfully")