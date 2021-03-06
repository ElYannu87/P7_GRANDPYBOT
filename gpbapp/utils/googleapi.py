import requests
import config

url = "https://maps.googleapis.com/maps/api/geocode/json"


class GoogleApi:

    @staticmethod
    def geocode_request(user_address):
        """ Request the Google Geocode API for latitude and longitude position """
        payload = {'address': user_address, 'key': config.GOOGLE_APP_ID}
        req = requests.get(url, params=payload)
        if req.status_code == 200:
            if req:
                result = req.json()
                coordinate_lat = result["results"][0]['geometry']['location']['lat']
                coordinate_lng = result["results"][0]['geometry']['location']['lng']
                return coordinate_lat, coordinate_lng
            else:
                return "none"
        else:
            print("The Geo_Code request has failed with the html error:" +
                  str(req.status_code))
