README.txt
Install:
NLTK,lxmlparser, stopwords, wordnet

Run Command: python ./res/parsernltk.py ./res/test1.listfile ./res/female.txt ./res/male.txt
test1.listfile : list of relative paths of all inputfiles (unprocessed, corefs)
male.txt - male corpus
female.txt - female corpus
main file - parsernltk.py
results are store in responses

Accuracy checked using:
Command: python new2-coref-scorer.py responselist.txt ./responses
responselist.txt : list of relative paths of all response files
new2-corefscorer - scorer program