import sys

def settings():
    fd = open("settings.py", "r")
    ret = dict()
    lines = fd.readlines()
    for line in lines:
        ret[line.split(" =")[0]] = line.split('"')[1]
    return ret

def check_file(file):
    
    


def modify_html(file):
    key_to_modif = settings()
    html = convert_str(file)



if __name__ == '__main__':
    if len(sys.argv) == 2:
        modify_html(sys.argv[1])