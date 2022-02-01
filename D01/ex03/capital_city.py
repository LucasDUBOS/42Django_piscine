import sys

def capital_city(city):
    capital = "Unknown state"
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if city in states:
        capital = capital_cities[states[city]]
    print(capital)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        capital_city(sys.argv[1])