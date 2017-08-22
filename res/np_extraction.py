import nltk
import xml.etree.ElementTree
from lxml import etree
from nltk.corpus import stopwords
import argparse

stopwords = stopwords.words('english')

#This file extracts noun phrases from corpus, is not used in our system because our system
#already had a structure using <COREF> and was not plain Corpus, we use other method 'parsexml()' defined in
#parsernltk to get noun phrases.

# Used when tokenizing words

sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'

lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()

def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    #word = word.lower()
    #word = stemmer.stem_word(word)
    #word = lemmatizer.lemmatize(word)
    #word = word.rstrip()
    #word = word.lstrip()
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    #.lower()
    accepted = bool(2 <= len(word) <= 40
        and word not in stopwords)
    return accepted

# Get independent terms
def get_terms(tree):
    for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term


def main(inp_file):
    #parser = argparse.ArgumentParser(description="Do something.")
    #parser.add_argument("-file", "--crf", type=str)
    #args = parser.parse_args(args)
    #data = open(inp_file, 'r')
    

    grammar = r"""
        NBAR:
            {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
        NP:
            {<NBAR>}
            {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
    """
    np = []

    chunker = nltk.RegexpParser(grammar)
    #trees = etree.parse(inp_file)

    xml_data = etree.fromstring(inp_file)
    
    notags = etree.tostring(xml_data, encoding='utf8', method='text')


    toks = nltk.regexp_tokenize(notags, sentence_re)


    postoks = nltk.tag.pos_tag(toks)

    #print toks
    #print postoks

    #Obtain noun phrases
    tree = chunker.parse(postoks)

    terms = get_terms(tree)
    for term in terms:
        term_string = ",".join(term)
        term_space = term_string.replace(",", " ") 
        np = np + [term_space]
    print np
    return np

if __name__ == '__main__':
    import sys
    main(inp_file)

#Taken from Su Nam Kim Paper...