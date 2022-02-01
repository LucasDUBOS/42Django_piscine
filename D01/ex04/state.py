import sys

def state(city):
    state = "Unknown capital city"
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
    for key, value in capital_cities.items():
        if value == city:
            for key2, value2 in states.items():
                if value2 == key:
                    state = key2
    print(state)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        state(sys.argv[1])