from gpbapp.utils.parser import Parser



def test_get_stopwords_file():
    """ Get the stop word list """
    assert type(Parser.get_stopwords_list()) == list

def test_split_the_user_question():
    """ Split the question in list """
    parser = Parser("J'ai été au 7 rue des champs à Paris avant hier")
    question = parser.split_user_question()
    assert question == [
        "j", "ai", "été", "au", "7", "rue", "des", "champs", "à", "paris", "avant", "hier"]

def test_compare_the_user_sentence_to_dict_list():
    """ Compare the user_sentence to the stop words list """
    parser_one = Parser("J'ai été au 7 rue des champs à Paris avant hier")
    parser_two = Parser("Ou est la Tour Eiffel ?")
    parser_three = Parser("Sais tu où est le Ministère de la défense ?")
    assert parser_one.get_address("J'ai été au 7 rue des champs à Paris avant hier") == "7 rue des champs paris"
    assert parser_two.get_address("Ou est la Tour Eiffel ?") == "tour eiffel"
    assert parser_three.get_address("Sais tu où est le Ministère de la défense ?") == "ministère défense"
