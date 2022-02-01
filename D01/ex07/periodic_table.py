import sys

def write_in_file(string,file):
    fd = open(file, "w")
    fd.write(string)
    fd.close()

def header():
    html = '<!doctype html>\n<html lang="fr">\n<head>\n    <meta charset="utf-8">\n    <title>table périodique</title>\n<style>td {border: 1px solid black; padding:10px;} </style>\n</head>\n<body>'
    return html

def convert_list_to_html(html, mend_list):
    html = html + "\n<table>\n<tr>"
    last_pos = 1
    for arg in mend_list:
        if last_pos == -1: #tricks for last row of tr w3c warning
            html = html + "\n</tr>\n<tr>"
        if int(arg[1]) - last_pos > 1:
            html = html + "\n<td colspan = " + str(int(arg[1]) - last_pos - 1) + ">\n</td>"
        # no else bcs we are in current arg when we add colspan
        html = html + "\n<td>\n<h4>" + arg[0] + "\n</h4>\n<ul>"
        for argument in arg[2:]:
            html = html + "\n<li>" + argument + "\n</li>"
        html = html + "\n</ul>\n</td>"
        last_pos = int(arg[1])
        if last_pos == 17:
            last_pos = -1
    html = html + "\n</tr>\n</table>\n</body>"
    return html


def file_to_list(file):
    fd = open(file, 'r')
    lines = fd.readlines()
    mend_list = []
    for line in lines:
        one_element = [line.split(" =")[0]]
        for elem in line.split(","):
            one_element.append(elem.split(":")[1].strip())
        mend_list.append(one_element)
    return mend_list

def create_html_from_file(file):
    mend_list = file_to_list(file)
    html = header()
    html = convert_list_to_html(html, mend_list)
    write_in_file(html, "periodic_table.html")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        create_html_from_file(sys.argv[1])