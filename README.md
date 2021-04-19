# SlingshotTrie
A trie that allows adding, deleting, searching, autocompleting, and displaying functions.

## Project Accomplishes:

### Trie Functions
1. Add keyword to trie
2. Delete a keyword from trie
3. Search for a keyword in trie [True/False]
4. Return list of autocomplete suggestion based on an input prefix
5. Display the trie

### Requirements:
1. The trie must be hosted online (AWS, GCloud, Azure or similar) so that multiple
concurrent clients from around the world can run the aforementioned operations on the
trie.
2. The trie must have one global state. All client operations must reflect changes in that one
global state.
3. A client interacts with the trie through a CLI (Command-Line Interface). There should be
clear instructions on how to download/install this CLI and run operations. <del>You can make
this CLI available through distributions such as `npm` (if using JS) or equivalent.<del>
4. Your trie must maintain the integrity of the order of requested operations across multiple
clients. If client A’s request is received before client B’s request, client A’s request must
be processed first before B’s request is processed. Think about if/what data structure
can help with this.
5. The operations must be as algorithmically efficient as you can think of.

The code has additionally been written in away to prevent users from adding incorrect data formats, and has been tested thoroughly for accuracy.

## How to run:

1. Download code as a .zip file using green download button.
2. Extract .zip file in file explorer.
3. Go to command line and type "pip install requests argparse" to install required packages.
4. After installing packages, "cd" into project directory.
5. Once in project directory, type "python request.py" followed by the various args that you want to run:
      * --add: Adds keywords to the trie. Ex: python request.py --add slingshot sling shot
      * --delete: Deletes keywords from the trie. Ex: python request.py --delete sling slingshot
      * --auto: Returns a list of autocompleted suggestions for a given prefix. Ex: python request.py --auto sl sho sling
      * --search: Return True or False depending on whether the given keyword is included in the trie or not. Ex: python request.py --search sling shot slingsh
      * --display: Show display (already does by default, but ㋡) Ex: python request.py --display True

Note: Multiple args can be added at the same time. If done so, the order in which they execute is as follows: --add, --delete, --auto, --search, and --display.
Note: To view how the request.py code works, open it using an app that supports the '.py' format. To view how to cloud/trie works, open the cloud.py file using an app that supports the '.py' format.

## Sample requests and responses:
Add:

![image](https://user-images.githubusercontent.com/64043281/115184428-72bc7980-a0a3-11eb-9164-817857d0dd99.png)

Delete:

![image](https://user-images.githubusercontent.com/64043281/115184507-9aabdd00-a0a3-11eb-8913-6108a852c44e.png)

Autocomplete:

![image](https://user-images.githubusercontent.com/64043281/115184581-b6af7e80-a0a3-11eb-917d-667a7e969f76.png)

Search:

![image](https://user-images.githubusercontent.com/64043281/115184632-d8a90100-a0a3-11eb-9cbf-66a8ec224bf7.png)

Display:

![image](https://user-images.githubusercontent.com/64043281/115184954-83b9ba80-a0a4-11eb-9992-8c4a56e07e3c.png)
