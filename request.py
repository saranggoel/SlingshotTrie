import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--add', nargs='+', type=str)
parser.add_argument('--delete', nargs='+', type=str)
parser.add_argument('--auto', nargs='+', type=str)
parser.add_argument('--search', nargs='+', type=str)
parser.add_argument('--display', type=bool, default=True)

args = parser.parse_args()

add_args = args.add
delete_args = args.delete
auto_args = args.auto
search_args = args.search
display_args = args.display

pos = {
        'add': add_args,
        'delete': delete_args,
        'auto': auto_args,
        'search': search_args,
        'display': display_args
}


response = requests.post('http://saranggoel.pythonanywhere.com/', json=pos)

print(response.text)