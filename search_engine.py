from typing import Tuple


class TrieNode(object):
    
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1
        self.OccurrenceList={}
    
#Adding a word in the trie structure
def insert(root, word: str,document):
        node = root
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    child.counter += 1
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
        # Everything finished. Mark it as the end of a word.
        if document not in node.OccurrenceList:  #If document is not in OccurenceList for that word

            node.OccurrenceList[document]=1     # Create a new key with document name

        node.OccurrenceList[document]= node.OccurrenceList[document]+1 # We append the position in the document
        node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    
#     Check and return 
#       1. If the prefix exsists in any of the words we added so far
#       2. If yes then in which file
    
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False when we did not find a char.
    if char_not_found:
        print("Your search - " + Enter + " did not match any document")
    # Well, we are here means we have found the prefix. Return true to indicate that
    return True,node.OccurrenceList


root = TrieNode('*')



#for scrapping words from website
from bs4 import BeautifulSoup
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
stop_words = set(stopwords.words('english'))
stop_words.update(string.punctuation) 
import os

#selecting file for scrapping
#please change the dircectory to run on your device
fdata = "C:/Users/shali/OneDrive/Desktop/New Folder/input/"
files=os.listdir(fdata)
for file in files:  

    fname=file
    file=open(fdata+str(file), encoding="utf8")
    soup = BeautifulSoup(file.read(), 'html.parser')
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    words = word_tokenize(soup.get_text())
    # remove the words containing punctuation
    words = [i for i in words if all(j not in string.punctuation for j in i)]
    for word in words:
        if word.lower() not in stop_words and len(word) > 2 and word.isdigit()==False:
                # build compressed trie tree
                try:
                    # remove the words whcih can't encode to ascII
                    word = word.lower().strip().encode('ascII')
                except:
    #                             print word
                    a = 1
                else:
                #inserting words into tree
                     insert(root, word.decode("utf-8"), fname)

Enter=input("Search: ")
Enter= Enter.lower()
inp=Enter.split(' ')
rank={}
for word in inp:
    boolw,dic=find_prefix(root, word)
#     print(dic)
    for key in dic:
        if key not in rank:
            rank[key]=dic[key]
        else:
            rank[key]=rank[key]+dic[key]
#ranking website based on number of time word present
items=[(v,k) for k,v in rank.items()]
items.sort()
items.reverse()
for key in items:
        print("Search results about: " + Enter)
        break
for key in items:
        print(key)
