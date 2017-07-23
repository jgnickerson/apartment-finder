import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 5000

# The maximum rent you want to pay per month.
MAX_PRICE = 10000

MIN_BEDROOMS = 5

MAX_BEDROOMS = 5

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'sfbay'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["sfc"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "pac_heights": [
        [37.782548, -122.445792],
        [37.795812, -122.423473],
    ],
    "haight": [
        [37.766362, -122.453789],
        [37.774885, -122.424307],
    ],
    "sunset": [
        [37.75451, -122.46422],
        [37.76258, -122.50825],
    ],
    "richmond": [
        [37.77188, -122.47263],
        [37.78029, -122.51005],
    ],
    "presidio": [
        [37.77805, -122.43959],
        [37.78829, -122.47151],
    ],
    "mission": [
        [37.747961, -122.425041],  [37.769843, -122.406374]
    ],
    "noe_valley": [[37.740460, -122.441994], [37.754916, -122.425772]],
    "castro": [[37.753423, -122.445084], [37.769097, -122.426630]],
    "bernal_heights": [[37.731761, -122.425121], [37.748824, -122.404273]],
    "cole_valley": [[37.757945, -122.452581], [37.767070, -122.447392]],
    "nopa": [[37.771618, -122.458124], [37.785498, -122.423218]],
    "hayes_valley": [[37.769261, -122.429094], [37.778964, -122.421766]],
    "marina": [[37.792889, -122.446483], [37.810730, -122.424730]],
    "russian_hill_north_beach": [[37.795761, -122.423521], [37.808956, -122.405164]]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["cow hollow", "pac hts", "pacific heights", "lower haight", "presidio", "haight ashbury", "noe valley", "bernal heights", "mission", "potrero hill", "north beach", "castro", "marina", "nopa", "western addition"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 2 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "oakland_19th_bart": [37.8118051,-122.2720873],
    "macarthur_bart": [37.8265657,-122.2686705],
    "rockridge_bart": [37.841286,-122.2566329],
    "downtown_berkeley_bart": [37.8629541,-122.276594],
    "north_berkeley_bart": [37.8713411,-122.2849758]
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
