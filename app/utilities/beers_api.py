#from typing import Iterator, Dict, Any
from typing import Iterator, List
from urllib.parse import urlencode
import requests

from models.beer_details import BeerDetails
from utilities.dates import parse_first_brewed


def iter_beers_from_api(page_size: int = 5) -> List[BeerDetails]:
#def iter_beers_from_api(page_size: int = 5) -> List[BeerDetails]:
    session = requests.Session()
    page = 1
    rtnList = [] 
    while True and page < 4:
        response = session.get('https://api.punkapi.com/v2/beers?' + urlencode({
            'page': page,
            'per_page': page_size
        }))
        response.raise_for_status()
        print("x-ratelimit-remaining: {}".format(response.headers["x-ratelimit-remaining"]))
        data = response.json()

        if not data:
            break
        page += 1

        for entry in data:
            beerDetails = BeerDetails(
              id=entry["id"], 
              name=entry["name"] ,
              tagline=entry["tagline"], 
              first_brewed=parse_first_brewed(entry["first_brewed"]), 
              description=entry["description"], 
              image_url=entry["image_url"], 
              )
            rtnList.append(beerDetails)  

    return rtnList