
from stage.utils import en_majuscule

def test_en_majuscule():
    assert en_majuscule("bonjour") == "BONJOUR"
    assert en_majuscule("Hello World") == "HELLO WORLD"
    assert en_majuscule("") == ""  # test vide