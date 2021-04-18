import sys
import argparse

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

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


def pprint(self, indent="", last=True, stack=""):
    if indent != "":
        stack = stack + self.char
    sys.stdout.write(indent)
    if last:
        sys.stdout.write("┗-")
        indent += "  "
    else:
        sys.stdout.write("┣-")
        indent += "┃ "
    sys.stdout.write("{} ({})".format(self.char, self.counter))
    if self.word_finished:
        print(" - {}".format(stack))
    else:
        print()
    for i, v in enumerate(self.children):
        pprint(v, indent, i == len(self.children) - 1, stack)


if __name__ == "__main__":
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

    root = TrieNode(' ')

    print('Action Status:\n')

    print('Add:')

    if add_args is not None:
        for v in add_args:
            print(add(root, v.lower()))
    else:
        print('No action')

    print('\nDelete:')
    if delete_args is not None:
        for v in delete_args:
            print(remove(root, v.lower()))
    else:
        print('No action')

    print('\nAutocomplete Suggestions:')
    if auto_args is not None:
        for v in auto_args:
            print(autocomplete(root, v.lower()))
    else:
        print('No action')

    print('\nSearch:')
    if search_args is not None:
        for v in search_args:
            print(find_prefix(root, v.lower()))
    else:
        print('No action')

    print('\nTrie Display:')
    if display_args:
        pprint(root)

