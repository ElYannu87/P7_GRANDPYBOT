import json
import random

import requests
from flask import Flask, render_template, request
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
    """Get the user question, parse it and show the address on map"""
    parserQuestion = Parser.get_address(sentence)

    # Get location for Google Map API marker
    geoLat, geoLng = GoogleApi.geocode_request(parserQuestion)

    # Get random story & title for Wiki Media API
    wikiLocation = str(geoLat) + "|" + str(geoLng)
    wikiRequest = WikiApi.req_wikimedia(wikiLocation)
    lenResult = len(wikiRequest['query']['geosearch'])
    if lenResult >= 1:
        ranStory = random.randrange(lenResult)
        story = WikiApi.req_story(wikiRequest, ranStory)
    else:
        story = "Je ne me rapelle de rien concernant ce lieux..."
        title = ""

    # Build the Json result to return
    data = {}
    data['lat'] = geoLat
    data['lng'] = geoLng
    if lenResult >= 1:
        data['title'] = story[0]['title']
        data['story'] = story[0]['extract']
    else:
        data['title'] = title
        data['story'] = story
    jsonData = json.dumps(data, ensure_ascii=False, indent=4)
    return jsonData