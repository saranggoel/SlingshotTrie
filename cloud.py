from flask import Flask, request
import sys

app = Flask(__name__)

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

root = TrieNode(' ')

def exists(root, word:str):
    node = root
    matching_word = ''
    for char in word:
        for child in node.children:
            if child.char == char:
                node = child
                matching_word += child.char
                if matching_word == word and node.word_finished == True:
                    return True

def add(root, word: str):
    node = root
    if exists(root, word):
        return f"Can not add '{word}', already exists!"
    if not word.isalpha():
        return f"Can not add '{word}', includes characters other than letters!"
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True
    return f"'{word}' successfully added!"


def remove(root, word: str):
    removed = True
    isAssigned = False
    isdelAssigned = False
    node = root
    if not exists(root, word):
        return f"Can not delete '{word}', does not exist!"
    if not word.isalpha():
        return f"Can not delete '{word}', includes characters other than letters!"
    for i, char in enumerate(word):
        for ind, child in enumerate(node.children):
            if child.char == char:
                child.counter -= 1
                if len(word) - 1 == i:
                    child.word_finished = False
                if child.counter == 0:
                    if not isAssigned:
                        delete_ind = i - 1
                        isAssigned = True
                    if not isdelAssigned:
                        deletechar = child.char
                        isdelAssigned = True
                node = child
                break
    delete = root
    if isAssigned:
        for i, char in enumerate(word):
            for ind, child in enumerate(delete.children):
                if child.char == char:
                    if delete_ind == -1 and removed:
                        root.children.remove(child)
                        removed = False
                    if i == delete_ind:
                        for i, ch in enumerate(child.children):
                            if ch.char == deletechar:
                                del child.children[i]
                    delete = child
                    break
    return f"'{word}' successfully deleted!"


def find_prefix(root, word: str):
    if exists(root, word):
        return f"'{word}' - Found: True"
    else:
        return f"'{word}' - Found: False"

def find_prefix_auto(root, prefix: str):
    node = root
    for char in prefix:
        for child in node.children:
            if child.char == char:
                node = child
                break
    return node


def autocomplete(root, prefix:str):
    autolist = []
    startNode = find_prefix_auto(root,prefix)
    autolist = printPaths(startNode,prefix, autolist)
    return f"'{prefix}': {autolist}"


def printPaths(root,prefix, autolist):
    path = []
    autolist = printPathsRec(root, path, 0,prefix, autolist)
    return autolist


def printPathsRec(root, path, pathLen, prefix, autolist):
    if root is None:
        return

    if (len(path) > pathLen):
        path[pathLen] = root.char
    else:
        path.append(root.char)

    pathLen = pathLen + 1
    if root.word_finished:
        autolist = printArray(path, pathLen,prefix, autolist)

    for child in root.children:
        autolist = printPathsRec(child, path, pathLen,prefix, autolist)
    return autolist


def printArray(ints, len,prefix, autolist):
    latter = ""
    for i in ints[1: len]:
        latter+=i
    autolist.append(prefix+latter)
    return autolist

def pprint(self, finToPrint, indent="", last=True, stack=""):
    if indent != "":
        stack = stack + self.char
    sys.stdout.write(indent)
    finToPrint.append(indent)
    if last:
        sys.stdout.write("┗-")
        finToPrint.append("┗-")
        indent += "  "
    else:
        sys.stdout.write("┣-")
        finToPrint.append("┣-")
        indent += "┃ "
    sys.stdout.write("{} ({})".format(self.char, self.counter))
    finToPrint.append("{} ({})".format(self.char, self.counter))
    if self.word_finished:
        print(" - {}".format(stack))
        finToPrint.append(" - {}".format(stack)+"\n")
    else:
        print()
        finToPrint.append("\n")
    for i, v in enumerate(self.children):
        pprint(v, finToPrint, indent, i == len(self.children) - 1, stack)
    return finToPrint


@app.route("/", methods=['GET', 'POST'])
def main():

    if request.method == 'POST':
        pr = ''
        request_data = request.get_json()
        add_args = request_data['add']
        delete_args = request_data['delete']
        auto_args = request_data['auto']
        search_args = request_data['search']
        display_args = request_data['display']

        pr+=('Action Status:\n\n')

        pr+=('Add:\n')

        if add_args is not None:
            for v in add_args:
                pr+=(add(root, v.lower())+'\n')
        else:
            pr+=('No action\n')

        pr+=('\nDelete:\n')
        if delete_args is not None:
            for v in delete_args:
                pr+=(remove(root, v.lower())+'\n')
        else:
            pr+=('No action\n')

        pr+=('\nAutocomplete Suggestions:\n')
        if auto_args is not None:
            for v in auto_args:
                pr+=(autocomplete(root, v.lower())+'\n')
        else:
            pr+=('No action\n')

        pr+=('\nSearch:\n')
        if search_args is not None:
            for v in search_args:
                pr+=(find_prefix(root, v.lower())+'\n')
        else:
            pr+=('No action\n')

        pr+=('\nTrie Display:\n')

        if display_args:
            toPrint = []
            returnFromPrint = pprint(root, toPrint, indent="", last=True, stack="")
            for i in returnFromPrint:
                pr+=(i)

        return pr

    else:
        return '''
    <!doctype html>
        <title>SlingShot Trie</title>
         '''


if __name__ == "__main__":
    root = TrieNode(' ')
    app.run()

