from docx import Document

def mettre_doc_en_majuscules(fichier_entree, fichier_sortie):

    doc = Document(fichier_entree)      #open file
    for para in doc.paragraphs:
        para.text = para.text.upper()
    doc.save(fichier_sortie)            #save in another file