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

## How to run:

1. Dow
