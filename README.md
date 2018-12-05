# Mini-Search-Engine
Search Engine using Trie Tree

Data Structure used: Trie Tree

Algorithm:

	(Inserting in tree)
•	Every character of input key is inserted as an individual trie node.
•	The children is an array of pointer to next level trie nodes
•	Key refers to the word that you are inserting or searching in the trie

(Searching in trie)


•	While searching we only compare the character and move down.
•	Search can terminate due to end of string, if the value field of last node is non-zero then the key exists in trie.
•	The search can also terminate due to lack of key nodes in trie without examining all characters.  
Insert and search cost O(k) where is length of the key
Memory requirement of the trie is O(ALPHABET_SIZE*k*N) where N is number of keys in trie.
