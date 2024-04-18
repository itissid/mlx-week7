#!/usr/bin/env python3

map_link = "https://maps.google.com/?q={lat},{long}"


def from_nominatim_search_response(responses: "JSON") -> str:
    """
        Given this:
        [
      {
        "place_id": 274867889,
        "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright",
        "osm_type": "way",
        "osm_id": 736488881,
        "lat": "51.49329525",
        "lon": "-0.061058087505277026",
        "class": "leisure",
        "type": "sports_centre",
        "place_rank": 30,
        "importance": 0.00000999999999995449,
        "addresstype": "leisure",
        "name": "The Arch Climbing Wall: Building One",
        "display_name": "The Arch Climbing Wall: Building One, Drummond Road, South Bermondsey, Bermondsey, London Borough of Southwark, London, Greater London, England, SE16 4DG, United Kingdom",
        "boundingbox": [
          "51.4931359",
          "51.4934479",
          "-0.0612326",
          "-0.0608870"
        ]
      }
    ]
        return the map_link with lat long in it
    """
    links = []
    for response in responses:
        if "lat" in response and "lon" in response:
            lat = response["lat"]
            long = response["lon"]
            links.append(map_link.format(lat=lat, long=long))
    return links

# Script that given a lat long return the link
if __name__ == "__main__":
    import sys

    # if len(sys.argv) == 3:
    #     lat = sys.argv[1]
    #     long = sys.argv[2]
    #     print(map_link.format(lat=lat, long=long))
    # else:
    import json
    print("\n."+sys.argv[0]+"\n")
    j = json.load(sys.stdin)
    # print(j)
    print('\n'.join (from_nominatim_search_response(j)))
