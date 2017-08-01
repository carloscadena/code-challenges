"""The Forbes Top 40 kata."""
import json
import os
import sys


with open(os.path.join(
    sys.path[0],
    "json/forbes_billionaires_2016.json"
)) as json_file:
    info = json.loads(json_file.read())


def forbes():
    """Return name, net worth, and industry of oldest billionaire under 80
    AND youngest billionaire with a valid age.
    """
    old = None
    young = None

    for billionaire in info:
        if not old:
            old = billionaire
        if not young:
            young = billionaire
        if billionaire['age'] > old['age'] and billionaire['age'] < 80:
            old = billionaire
        if billionaire['age'] < young['age'] and billionaire['age'] > 0:
            young = billionaire
    return 'oldest: ', old['name'], old['net_worth (USD)'], old['source'], 'youngest: ', young['name'], young['net_worth (USD)'], young['source'],
