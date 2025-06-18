import sys
import os

# add parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stage.translation import traduire_document
from docx import Document
import sys

# main function to translate a docx file
def main():
    if len(sys.argv) != 3:
        print("usage : python test_docx_translation.py <fichier_entrée> <fichier_sortie>")
        sys.exit(1)

    chemin_entree = sys.argv[1]  # get input file path
    chemin_sortie = sys.argv[2]  # get output file path

    print(f"loading file : {chemin_entree}")
    doc_original = Document(chemin_entree)  # load the document

    print("starting translation")
    doc_traduit = traduire_document(doc_original, use_mock=True)  # translate the document

    print(f"saving translated file to : {chemin_sortie}")
    doc_traduit.save(chemin_sortie)  # save the translated document
    print("translation finished successfully")

# call main function if the script is run directly
if __name__ == "__main__":
    main()
