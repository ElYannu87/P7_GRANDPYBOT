import json
import random

from flask import Flask, render_template
from .utils.parser import Parser
from .utils.googleapi import GoogleApi
from .utils.wikiapi import WikiApi

app = Flask(__name__)

# Add config.py file
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/question/<sentence>')
def question(sentence):
    """Get the user question,
     send to parser
     show the address on map"""
    parser_question = Parser(sentence)
    parser_answer = parser_question.get_address(sentence)

    # Get location for Google Map API marker
    geo_lat, geo_lng = GoogleApi.geocode_request(parser_answer)

    # Get random story & title for Wiki Media API
    wiki_location = str(geo_lat) + "|" + str(geo_lng)
    wiki_request = WikiApi.req_wikimedia(wiki_location)
    len_result = len(wiki_request['query']['geosearch'])
    if len_result >= 1:
        ran_story = random.randrange(len_result)
        story = WikiApi.req_story(wiki_request, ran_story)
    else:
        story = "Je ne me rapelle de rien concernant ce lieux..."
        title = ""

    # Build the Json result to return
    data = {}
    data['lat'] = geo_lat
    data['lng'] = geo_lng
    if len_result >= 1:
        data['title'] = story[0]['title']
        data['story'] = story[0]['extract']
    else:
        data['title'] = title
        data['story'] = story
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    return json_data
