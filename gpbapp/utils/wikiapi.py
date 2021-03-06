import requests


class WikiApi:
    def req_wikimedia(self, wiki_location):
        """ Request the API with location,
        get some page around the location,
        get a random page in result and return to the HTML page"""

        url = "https://fr.wikipedia.org/w/api.php"
        payload = {'action': 'query', 'format': 'json', 'uselang': 'fr',
                   'list': 'geosearch', 'gscoord': wiki_location}
        req = requests.get(url, params=payload)
        if req.status_code == 200:
            wiki_req = req.json()
        else:
            print("The Wiki request has failed with the html error:" + str(req.status_code))
        return wiki_req

    def req_story(self, wiki_request, ran_story):
        """ Get a random story from the geosearch"""

        url = "https://fr.wikipedia.org/w/api.php"
        page_id = wiki_request['query']['geosearch'][ran_story]['pageid']
        payload = {'action': 'query', 'format': 'json', 'prop': 'extracts',
                   'utf8': '1', 'formatversion': 'latest', 'exsentences': '3',
                   'explaintext': '1', 'exsectionformat': 'wiki', 'pageids': page_id}
        req = requests.get(url, params=payload)
        if req.status_code == 200:
            result = req.json()
            wiki_req = result['query']['pages']
        else:
            print("The Wiki request has failed with the html error:" + str(req.status_code))
        return wiki_req
