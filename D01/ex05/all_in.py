import sys

def all_in(var):
    city = var.capitalize()
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
        state = city
    for key, value in capital_cities.items():
        if value == city:
            for key2, value2 in states.items():
                if value2 == key:
                    capital = city
                    state = key2
    if 'capital' in locals():
        print(capital, "is the capital of", state)
    else:
        print(var, "is neither a capital nor a state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        for arg in sys.argv[1].split(","):
            clear_arg = arg.strip()
            if clear_arg:
                all_in(clear_arg)