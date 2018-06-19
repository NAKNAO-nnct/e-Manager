import os
tt = 'aaaa'

def reafFile():
    with open('template.tpl', 'r') as r_file:
        temp_data = ''
        for line_data in r_file:
            temp_data += line_data

reafFile()
