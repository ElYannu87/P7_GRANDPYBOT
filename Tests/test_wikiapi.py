from gpbapp.utils.wikiapi import WikiApi
import requests
import requests_mock


def test_req_wikimedia():
    wiki_api = WikiApi()
    with requests_mock.Mocker() as m:
        m.get('https://fr.wikipedia.org/w/api.php?action=query&format=json&uselang=fr&list=geosearch&gscoord=48.957802%7C1.812542', json={'a': 'b'})
        result = wiki_api.req_wikimedia("48.957802|1.812542")
        assert result == {'a': 'b'}

def test_req_story():

    wiki_api = WikiApi()

    wikiRequest = {'batchcomplete': '', 'query': {'geosearch': [{'pageid': 121171, 'ns': 0,
                    'title': 'Ports de Paris', 'lat': 48.856614, 'lon': 2.3522219, 'dist': 0,
                    'primary': ''}, {'pageid': 7738248, 'ns': 0, 'title': "Deaflympics d'été de 1924",
                    'lat': 48.85667, 'lon': 2.35194, 'dist': 21.5, 'primary': ''}, {'pageid': 404157,
                    'ns': 0, 'title': 'Hôtel de ville de Paris', 'lat': 48.856389, 'lon': 2.352222,
                    'dist': 25, 'primary': ''}, {'pageid': 5559673, 'ns': 0,
                    'title': "Bibliothèque de l'hôtel de ville de Paris", 'lat': 48.856389, 'lon': 2.352222,
                    'dist': 25, 'primary': ''}, {'pageid': 49947, 'ns': 0, 'title': 'Mairie de Paris',
                    'lat': 48.85638889, 'lon': 2.35222222, 'dist': 25, 'primary': ''}, {'pageid': 5785941,
                    'ns': 0, 'title': 'Prise de Paris (1420)', 'lat': 48.8566, 'lon': 2.35183, 'dist': 28.7,
                    'primary': ''}, {'pageid': 5773488, 'ns': 0, 'title': 'Siège de Paris (1370)',
                    'lat': 48.856578, 'lon': 2.351828, 'dist': 29.1, 'primary': ''}, {'pageid': 5044060,
                    'ns': 0, 'title': 'Bataille de Lutèce (383)', 'lat': 48.856578, 'lon': 2.351828,
                    'dist': 29.1, 'primary': ''}, {'pageid': 6394516, 'ns': 0,
                    'title': '1re session du Comité du patrimoine mondial', 'lat': 48.856578, 'lon': 2.351828,
                    'dist': 29.1, 'primary': ''}, {'pageid': 5757771, 'ns': 0, 'title': 'Siège de Paris (861)',
                    'lat': 48.856578, 'lon': 2.351828, 'dist': 29.1, 'primary': ''}]}}

    reqStory = {'batchcomplete': True, 'warnings': {'extracts': {'warnings': '"exlimit" was too large for a whole article extracts request, lowered to 1.'}},
                'query': {'pages': [{'pageid': 49947, 'ns': 0, 'title': 'Mairie de Paris',
                'extract': "La mairie de Paris, sise à l'hôtel de ville de la capitale, est le siège de l'administration dirigée par les élus municipaux et départementaux de Paris.\n\n\n == Histoire ==\n\n\n === Sous l'Ancien Régime ===\nLa première municipalité parisienne est constituée vers 1260, lorsque Saint Louis octroie aux prévôts et jurés de la puissante corporation des marchands de l'eau le droit d'administrer une partie de la cité. Cette association détient alors le monopole de la navigation sur la Seine, l'Oise, la Marne et l'Yonne, réglemente le trafic du fleuve et fixe les taxes à percevoir."}]}}

    resultNeed = [{'pageid': 49947, 'ns': 0, 'title': 'Mairie de Paris',
               'extract': "La mairie de Paris, sise à l'hôtel de ville de la capitale,"
                " est le siège de l'administration dirigée par les élus municipaux et départementaux de Paris.\n\n\n"
                " == Histoire ==\n\n\n === Sous l'Ancien Régime ===\nLa première municipalité parisienne est constituée vers 1260,"
                " lorsque Saint Louis octroie aux prévôts et jurés de la puissante corporation des marchands"
                " de l'eau le droit d'administrer une partie de la cité. Cette association détient alors"
                " le monopole de la navigation sur la Seine, l'Oise, la Marne et l'Yonne,"
                " réglemente le trafic du fleuve et fixe les taxes à percevoir."}]

    with requests_mock.Mocker() as m:
        m.get(
            'https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&utf8=1&formatversion=latest&exsentences=3&explaintext=1&exsectionformat=wiki&pageids=49947', json=reqStory)
        result = wiki_api.req_story(wikiRequest, 4)
        assert result == resultNeed