from gpbapp.utils.parser import Parser


def test_get_stopwords():
    assert type(Parser.get_stopwords_list()) == list

def test_split_the_user_question():
    assert Parser.split_user_question("J'ai été au 7 rue des champs à Paris avant hier") == [
        "j", "ai", "été", "au", "7", "rue", "des", "champs", "à", "paris", "avant", "hier"]

def test_compare_the_user_sentence_to_dict_list():
    """ Compare the user_sentence to the stop words list """
    assert Parser.get_address("J'ai été au 7 rue des champs à Paris avant hier") == "7 rue des champs paris"
    assert Parser.get_address("Ou est la Tour Eiffel ?") == "tour eiffel"
    assert Parser.get_address("Sais tu où est le Ministère de la défense ?") == "ministère défense"
