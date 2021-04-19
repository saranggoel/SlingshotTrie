# How it works:

The code for the trie and cloud is included in cloud.py. A trie was created that supported the functions of adding (function add), deleting (function remove), autocompleting (functions autocomplete, find_prefix_auto, printPaths, printPathsRec, and printArray), searching (function find_prefix), and displaying (function pprint). The code uses a global class that is updated everytime a request is made, allowing for a consistent trie among all users. For easy user access, the code uses Python Flask so that it can continuously run and update. It was then hosted on PythonAnywhere, a free hosting platform. 

The code to access the trie (hosted on the cloud) is included in request.py. A args system was created for easy user interaction with the trie. It accepts various parameter for the various different functions of the trie. In order to retrieve results, the code make a request to the trie hosted on the cloud. Finally, it prints all results.

