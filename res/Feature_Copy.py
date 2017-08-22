import sys
from collections import defaultdict
from nltk.corpus import wordnet as wn
from collections import Counter
#import numpy
import itertools
import re

'''
simplePronouns = ("he", "her", "his", "hers", "him")
personPronouns = ("i", "we", "you")
neuteredPronouns = ("its", "it", "they", "them", "theirs", "their")
reflexivePronouns = ("himself", "themselves", "herself", "itself")
'''
#pronoun = ["he", "her", "his", "hers", "him", "i", "we", "you", "its", "it", "they", "them", "theirs", "their", "himself", "themselves", "herself", "itself"]
#articles = ["a", "an", "the"]  

"""for i in coref_nouns_maam:
    print i"""

#coref_nouns_maam = ['f14-crashes', 'accidents', 'feb. 22', 'bloomberg', 'its northrop\ngrumman corp. f-14s', 'it', 'three recent f-14 crashes', 'today', 'navy', 'its', 'today', 'the recent mishaps involving f-14as and ds', 'navy', 'all f-14\naircraft', 'a navy spokesman', 'these mishaps', 'all f-14s', 'f-14', 'navy', 'the standdown', 'persian gulf', 'geisen', 'those planes', "the f14 ``tomcat''", "the navy's first-line fighter aircraft", 'it', 'navy', 'about 330 f-14s', 'a unit', 'navy', 'that\nfigure', 'navy', 'geisen', 'the aircraft', 'then', 'geisen', 'the planes', 'now northrop grumman', 'the company', 'navy', 'he', 'today', 'navy', 'the three recent crashes', 'their', 'three days', 'geisen', 'northrop grumman', '02-22-96']

#coref_nouns_maam = ['trans world airlines', 'additional shares of usair group inc.', 'the order', 'usair', 'another blow', 'washington-based usair', 'proposed transaction', 'chairman of twa', 'twa', 'usair', 'mr. icahn', 'twa', "usair's largest shareholder", 'mr. icahn', 'the attempt', 'usair', 'piedmont', 'twa', 'usair', 'piedmont', 'a securities analyst', 'mr. marckesano', 'twa', 'mr. icahn', 'usair', 'piedmont', 'twa', 'usair', 'department', 'it', 'it', 'serious application', 'department', 'new filing', 'usair', 'it', 'usair', 'twa', 'tender-offer', 'usair', 'mr. icahn', 'chairman and chief executive officer', 'usair', 'usair', 'the filings', 'mr. icahn', 'mr. colodny', 'twa', 'usair', 'twa', 'usair', 'usair', 'twa', 'usair', 'piedmont', 'mr. icahn', 'mr. colodny', 'the documents', 'mr. icahn', 'the documents', 'mr. colodny', 'twa', 'mr. icahn', 'he', 'mr. icahn', 'usair', 'twa', 'usair', 'mr. icahn', "twa's offer for usair", 'he', 'the bid', 'usair', 'piedmont', 'mr. icahn', 'twa', 'tender offer for piedmont', 'carl', 'usair', 'he', 'he', 'mr. icahn', 'mr. icahn', 'twa', 'the airline', 'usair', 'twa', 'usair', 'its', 'mr. icahn', 'twa', 'usair', 'twa', 'the drop', 'mr. icahn', 'icahn', 'twa', 'usair', 'piedmont', 'piedmont', 'merger with usair', 'usair', 'the merger', 'the company', 'its tender', 'usair', 'piedmont', 'twa', 'usair', 'mr. icahn', 'twa', 'sec', 'its', 'usair', 'twa', 'usair', 'usair', 'its', 'the piedmont acquisition', 'the company', 'it', 'bank', 'the purchase', 'usair', 'manufacturers hanover', 'usair', 'it', 'the acquisition', 'it', 'the airline', 'the filing', 'it', 'piedmont', 'usair', 'chairman and chief executive of piedmont', 'usair', 'the merger', 'twa', 'usair', 'twa', 'usair', 'the court', 'twa', 'more usair shares', "usair's tender offer for piedmont stock", 'usair', 'mr. icahn', 'twa', 'usair', 'usair', 'mr. icahn', 'twa', 'usair', 'transportation department', 'twa', 'mr. icahn', 'twa', 'usair', 'twa', 'it', 'hart-scott-rodino', 'transportation department', 'twa', 'department', 'the airline', 'usair', 'usair', 'twa', 'it', 'department', 'texas air']

#coref_nouns_maam = ['western union corp.', 'western union telegraph co.', 'the contracts', 'unions', 'communications systems company', 'the existing contracts', 'the company', 'the unions', 'the accord', 'western union', 'company']

#print mainarray

#print maindict
#newarray=[]

def score(np1,np2):
    simplePronoun = ["he", "her", "his", "hers", "him"]
    personPronoun = ["i", "we", "you"]
    neuteredPronoun = ["its", "it", "they", "them", "theirs", "their"]
    reflexivePronoun = ["himself", "themselves", "herself", "itself"]
    relativePronoun = ["that", "which", "whom", "who", "whoever", "whomever", "whichever", "whose", "when", "whomsoever", "whosoever", "whatever", "whatsoever", "whichsoever", "whosesoever"]
    pronoun = ["he", "her", "his", "hers", "him", "i", "we", "you", "its", "it", "they", "them", "theirs", "their", "himself", "themselves", "herself", "itself"]
    dates = ["today","tomorrow", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "yesterday", "day", "night"]
    np1_list_upper = np1.split(" ")
    #print np1_list
    np2_list_upper = np2.split(" ")
    #print np1_list
    #print np2_list
    np1_list = [element.lower() for element in np1_list_upper]
    np2_list = [element.lower() for element in np2_list_upper]
    match = len(set(np2.split())&set(np1.split()))
    mismatch = max(len(np1.split()),len(np2.split()))-match
    if float(max(len(np1.split()),len(np2.split())))!= 0.0:
        words = 10*(float(mismatch) / float(max(len(np1.split()),len(np2.split()))))

    if(np1_list[-1] == np2_list[-1]):
        head_noun = 0.0
    else:
        head_noun = 1.0
    pronoun_score1 = 0.0
    pronoun_score2 = 0.0
    pronoun_score3 = 0.0
    pronoun_score4 = 0.0
    pronoun_score5 = 0.0
    for word1 in np1_list:
        #print word1, "word1"
        for word2 in np2_list:
            #print word2, "word2"
            if (word1 in pronoun) and (word2 not in pronoun):
                pronoun_score1 = 100* (pronoun_score1 + 1)
                #print "sim"
            else:
                pronoun_score1= 0.0
            '''
            if (word1 in simplePronoun) and (word2 not in simplePronoun):
                pronoun_score1= pronoun_score1 + 1
                #print "sim"
            else:
                pronoun_score1= pronoun_score1 + 0
            if (word1 in personPronoun) and (word2 not in personPronoun):
                pronoun_score2= pronoun_score2 + 1
                #print "sim2"
            else:
                pronoun_score2= pronoun_score2 + 0
            if (word1 in neuteredPronoun) and (word2 not in neuteredPronoun):
                pronoun_score3= pronoun_score3 + 1
                #print "sim3"
            else:
                pronoun_score3= pronoun_score3 + 0
            if (word1 in reflexivePronoun) and (word2 not in reflexivePronoun):
                pronoun_score4= pronoun_score4 + 1
                #print "sim4"
            else:
                pronoun_score4= pronoun_score4 + 0

            if (word1 not in relativePronoun) and (word2 in relativePronoun):
                pronoun_score5= pronoun_score5 + 0
                #print "sim4"
            else:
                pronoun_score5= pronoun_score5 + 1
            '''
                

    if(np2 in np1 or np1 in np2):
        word_substring = -10000*1
    else:
        word_substring = 0
    

    if(np1_list[-1][-1]== np2_list[-1][-1] == 's'):
        number = -100
    else:
        number = 1

    Semantic_Class1 = []
    Semantic_Class2 = []
    #print np1_list[-1],"Avani"
    #print np2_list[-1], "Avnu"
    for synset in wn.synsets(np1_list[-1], wn.NOUN):
        #print np1_list[-1],"Avani"
        #print "<%s>" % (synset.lexname())
        Semantic_Class1 = Semantic_Class1 + [synset.lexname()]
        
    for synset in wn.synsets(np2_list[-1], wn.NOUN):
        #print np2_list[-1], "Avnu"
        #print "<%s>" % (synset.lexname())
        Semantic_Class2 = Semantic_Class2 + [synset.lexname()]
        

    if(Most_Common(Semantic_Class1) == Most_Common(Semantic_Class2)):
        semantic_score = 0
    else:
        semantic_score = 1*10000

    
    if(np2_list[-1][-1] == ',' and np1_list[0].isalpha()):
        #print("Avani")
        appos_score = -10000*1
    else:
        appos_score = 0

    
    date_score = 0
    for npp1 in np1_list:
        for npp2 in np2_list:
            h1 = re.findall(r"(..?)[-/](..?)[-/](..?)",npp1)
            h2 = re.findall(r"(..?)[-/](..?)[-/](..?)",npp2)
            if(h1 != [] and npp2 in dates or h2 != [] and npp1 in dates):
                date_score = date_score - 10000*1

            if(np1 in dates and np2 in dates):
                date_score = date_score - 10000*1

    abbr_score = 0
    #np1_list.append("hi")
    #print np1_list
    if(len(np2_list) == 1 and len(np1_list) == len(np2_list[0])):
        for i,npp1 in enumerate(np1_list):
            if(npp1[0]==np2_list[0][i]):
                abbr_score = abbr_score - 10000*1
    if(len(np1_list) == 1 and len(np2_list) == len(np1_list[0])):
        for i,npp2 in enumerate(np2_list):
            #print np2_list
            #print npp2
            if(npp2[0]==np1_list[0][i]):
                abbr_score = abbr_score - 10000*1
    
    pnoun_score = 0.0
    
    list_np1_pnoun = []
    list_np2_pnoun = []
    #print np1_list_upper
    for word1 in np1_list_upper:
        #print word1[0]
        if(word1[0].isupper()):
            list_np1_pnoun.append(1)
        else:
           list_np1_pnoun.append(0)

    #print np2_list_upper
    for word1 in np2_list_upper:
        #print word1
        if(word1[0].isupper()):
            list_np2_pnoun.append(1)
        else:
           list_np2_pnoun.append(0)

    #print np1_list_upper
    #print np2_list_upper 
    np11 = ' '.join(np1_list_upper)
    np22 = ' '.join(np2_list_upper)

    if len(set(list_np1_pnoun)) == 1 and len(set(list_np2_pnoun)) == 1 and np11 in np22 or np22 in np11:
        pnoun_score = -10000
    else:
        pnoun_score = 1

    #if len(set(list_np1_pnoun)) == 1 and any((True for x in a if x in b))

    final_score = float(words + head_noun + pronoun_score1 + appos_score + date_score + pnoun_score + abbr_score + word_substring + number)
    #print type(final_score)
    #np1 = ' '.join(np1)
    #np2 = ' '.join(np2)
    return final_score

'''
def Calculate_score(mainarray):
    #print("Avani")

    #pronoun = ["he", "her", "his", "hers", "him", "i", "we", "you", "its", "it", "they", "them", "theirs", "their", "himself", "themselves", "herself", "itself"]

    Final_Score = []
    for i,np1 in enumerate(mainarray):
        for np2 in mainarray[i+1:len(mainarray)-1]:
            final_score =score(np1,np2)
            Final_Score = Final_Score + [[np1,np2,final_score,i,mainarray.index(np2)]]
    return Final_Score
    '''
def reverse_enumerate(iterable, start=0):
    """
    Enumerate over an iterable in reverse order while retaining proper indexes
    """
    if(start == 0):
        return itertools.izip(reversed(xrange(len(iterable))), reversed(iterable))
    else:
        return itertools.izip(reversed(xrange(len(iterable[::start]))), reversed(iterable[::start]))

def clustering(mainarray):
    #Using Clustering to find noun phrases belonging to same group
    #Paper used :Noun Phrase Coreference as Clustering - Cornell Computer Science
    #Link for paper : https://www.cs.cornell.edu/home/cardie/papers/emnlp-99.ps
    classes = [[] for x in range(0, len(mainarray))] 
    #print len(classes)
    for i,nps in enumerate(mainarray):
        classes[i] = classes[i] + [nps]
    l = len(classes)
    #print classes
    # and check(classes[two_nps[3]],classes[two_nps[4]]) < r
    r = float(12)
    faltu_list = []
    for i in range(l-1,-1,-1):
        #print i, "i"
        #print classes[i]
        for j in range(i-1,-1,-1):
            #print j
            #rint classes[i][0],i
            #print classes[j][0],j
            #if(classes[i]!=[] and classes[j]!=[]):
            final_score =score(classes[i][0],classes[j][0])

            if final_score < r and check(classes[i],classes[j]) < r: #and classes[i]!=[] and classes[j]!=[]:
                #print("Avani")
                #print classes[i],classes[j]
                classes[i].extend(classes[j])
                faltu_list.append(j)
                #print classes
                #del classes[j][:]
                
                #print classes[i],classes[j]
                #classes.pop(j)

    #print faltu_list            
    #print classes
           
    '''
    findItem(classes,np2[0])[0][0])
    for two_nps in Final_Scores:
        if(two_nps[2] < r and check(classes[two_nps[3]],classes[two_nps[4]]) < 10000):
            classes[two_nps[3]] = classes[two_nps[3]] + [two_nps[1]]
            print classes
            classes.pop(two_nps[4])
            print classes
    #print classes
    print len(classes)
    
    classes2 = []
    for item in classes:
        classes2 = classes2 + [[x for x in item if x != []]]
    #print classes2
    classes3 = []
    classes3 = classes3 + [x for x in classes2 if x != []]
    '''
    #print classes
    return classes

def findItem(theList, item):
    #print [[ind, theList[ind].index(item)] for ind in xrange(len(theList)) if item in theList[ind]]
    return [[ind, theList[ind].index(item)] for ind in xrange(len(theList)) if item in theList[ind]]

def check(class1,class2):
    f_score = 0.0
    if(class1 != [] and class2 != []):
        for np1 in class1:
            for np2 in class2:
                #np1 = ' '.join(np1)
                #np2 = ' '.join(np2)
                final_score = score(np1,np2)
                f_score = f_score + final_score
        return f_score/float(min(len(np1.split()),len(np2.split())))

def Most_Common(lst):
    #print lst
    if(lst == []):
        return
    else:
        return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]

def matchings(noun_phrases,males,females):
    #This method applied all rules over anaphora to find their antecedants.
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
                    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
                    'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
                    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
                    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
                    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
                    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
                    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
                    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
                    'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
                    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
    dates = ["today","tomorrow", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "yesterday", "day", "night"]
    pronouns = ["he","she","him","his","hers", "her","we","us","they","them","our","ours","our's","my","me","their","i",
           "theirs","her's","that","it","himself","herself","one","someone","anyone","somebody","anybody","everybody",'itself']
    male_pronouns = ['he','his','him','himself']
    neutral_pronouns = ['it','its', 'itself']
    female_pronouns = ['she','her','hers','herself']
    ambiguous_pronouns_singular = ['you','me','i','yours', 'my', 'mine']
    plural_pronouns = ['they','their','those','them','these', 'all', 'theirs', 'we', 'ours', 'our', 'everybody', 'us']
    #EXACT STRING MATCH
    #EXACT STRING MATCH

    for i,np1 in enumerate(noun_phrases):
        #np1[1] = np_1[1].lower()
        #a=0
        m = i
        n = i
        #print noun_phrases[i][1],"WORD1111111111111111111111111111111111111111111111",
        for j,np2 in enumerate(noun_phrases):
            
            if(2*i < len(noun_phrases)):
                if(j < 2*i):
                    if(i == 0):
                        k = j
                    else:
                        if(j%2 == 0):
                            m = m-1
                            k = m
                        else:
                            n = n+1
                            k = n
                else:
                    k = j
            else:
                if(n < len(noun_phrases)-1):
                    if(i == len(noun_phrases)-1):
                        k = len(noun_phrases)-1-j
                    else:
                        if(j%2 == 0):
                            m = m-1
                            k = m
                        else:
                            n = n+1
                            k = n
                else:
                    k = len(noun_phrases)-1-j
            #print noun_phrases[k][1]
            #n_noun_phrases[k][1] = noun_phrases[k][1].lower()
            #print noun_phrases[k][1],k,"WORDDDDD22222222222222222",
            if noun_phrases[i][1].lower() == noun_phrases[k][1].lower()  and noun_phrases[i][0] != noun_phrases[k][0]:
                if(len(np1)==2):
                    np1.append(noun_phrases[k][0])

    #ABBREVATION MATCH 
    flag = 0
    flag1 = 0
    for i,np1 in enumerate(noun_phrases):
        #np1[1] = np1[1].lower()
        np1_list = np1[1].split()
        for j,np2 in enumerate(noun_phrases):
            #np2[1] = np2[1].lower()
            np2_list = np2[1].split() 
            if(len(np2_list) == 1 and len(np1_list) == len(np2_list[0])):
                for i,npp1 in enumerate(np1_list):
                    if(npp1[0].lower()==np2_list[0][i].lower()):
                        continue
                    else:
                        flag = 1
                        break
                if(flag == 0):
                    if(len(np1)==2 and noun_phrases[i][0] != noun_phrases[j][0]):
                        np1.append(noun_phrases[j][0])
                    if(len(np2)==2 and noun_phrases[i][0] != noun_phrases[j][0]):
                        np2.append(noun_phrases[i][0])

    #Head noun MATCH
    for i,np1 in enumerate(noun_phrases):
        #np1[1] = np1[1].lower()
        np1_list = np1[1].split()
        #a = 0
        m = i
        n = i
        for j,np2 in enumerate(noun_phrases):
            #np2[1] = np2[1].lower()
            if(2*i < len(noun_phrases)):
                if(j < 2*i):
                    if(i == 0):
                        k = j
                    else:
                        if(j%2 == 0):
                            m = m-1
                            k = m
                        else:
                            n = n+1
                            k = n
                else:
                    k = j

            else:
                if(n < len(noun_phrases)-1):
                    if(i == len(noun_phrases)-1):
                        k = len(noun_phrases)-1-j
                    else:
                        if(j%2 == 0):
                            m = m-1
                            k = m
                        else:
                            n = n+1
                            k = n
                else:
                    k = len(noun_phrases)-1-j
            #np2_list = np2[1].split()
            #print k
            np2_list = noun_phrases[k][1].split(" ")

            if(len(np1_list) > 1 or len(np2_list) > 1):
                for word1 in np1_list:
                    if word1.lower() not in stopwords:
                        for word2 in np2_list:
                            if word2.lower() not in stopwords:
                                if(word1.lower() == word2.lower()):
                                    if(len(np1)==2 and noun_phrases[i][0] != noun_phrases[k][0]):
                                        np1.append(noun_phrases[k][0])
         

    #APPOSITIVES
    '''
    for i,np1 in enumerate(noun_phrases):
        np1[1] = np1[1].lower()
        np1_list = np1[1].split()
        for j,np2 in enumerate(noun_phrases):
            np2[1] = np2[1].lower()
            np2_list = np2[1].split()
            if(np2_list[-1][-1] == ','):
                if len(noun_phrases[i]) == 2:
                    noun_phrases[i].append(noun_phrases[j][0])
                if len(noun_phrases[j]) == 2:    
                    noun_phrases[j].append(noun_phrases[i][0])
    ''' 
    for i,np in enumerate(noun_phrases):
        if len(np) == 2:
            if i+1 <= len(noun_phrases)-1:
                if len(noun_phrases[i]) == 2 and noun_phrases[i][0] != noun_phrases[i+1][0]:
                    noun_phrases[i].append(noun_phrases[i+1][0])
                if len(noun_phrases[i+1]) == 2 and noun_phrases[i][0] != noun_phrases[i+1][0]:    
                    noun_phrases[i+1].append(noun_phrases[i][0])

    
                   
    #SEMANTIC MATCH
    for i,np1 in enumerate(noun_phrases):
        #np1[1] = np1[1].lower()
        np1_list = np1[1].split()
        for j,np2 in enumerate(noun_phrases):
            #np2[1] = np2[1].lower()
            np2_list = np2[1].split()
            Semantic_Class1 = []
            Semantic_Class2 = []
            #np2_list[-1].lower()
            #np2_list[-1].lower()
            for synset in wn.synsets(np1_list[-1].lower(), wn.NOUN):
                #print np1_list[-1],"Avani"
                #print "<%s>" % (synset.lexname())
                Semantic_Class1 = Semantic_Class1 + [synset.lexname()]
                
            for synset in wn.synsets(np2_list[-1].lower(), wn.NOUN):
                #print np2_list[-1], "Avnu"
                #print "<%s>" % (synset.lexname())
                Semantic_Class2 = Semantic_Class2 + [synset.lexname()]
            if(Most_Common(Semantic_Class1) == Most_Common(Semantic_Class2)):
                #print "Avani"
                if len(noun_phrases[i]) == 2 and noun_phrases[i][0] != noun_phrases[j][0]:
                    noun_phrases[i].append(noun_phrases[j][0])
                if len(noun_phrases[j]) == 2 and noun_phrases[i][0] != noun_phrases[j][0]:
                    noun_phrases[j].append(noun_phrases[i][0])

    #PROPER NOUNS
    semantic_class = []
    uppercase = re.compile(".*[A-Z].*")
    for i,np1 in enumerate(noun_phrases):
        #np1[1] = np1[1].lower()
        np1_list = np1[1].split()
        for j,np2 in enumerate(noun_phrases):
            #np2[1] = np2[1].lower()
            np2_list = np2[1].split()
            if uppercase.match(np1[1]) and (not np1[1][-1].find("The ") > -1) or (not np1[1].find("A ") > -1):
                #print "Avani"
                for synset in wn.synsets(np1_list[-1].lower(), wn.NOUN):
                    semantic_class = semantic_class + [synset.lexname()]
                classs = Most_Common(semantic_class)
                if (classs == 'noun.person') and (np2_list[-1].lower() in male_pronouns or np2_list[-1].lower() in female_pronouns or np2_list[-1].lower() in ambiguous_pronouns_singular):
                    if(len(np1)==2 and noun_phrases[i][0] != noun_phrases[j][0]):
                        #print "Avani"
                        np1.append(noun_phrases[j][0])
                if (classs == 'noun.person' or classs == 'noun.plant' or classs == 'noun.state' or classs == 'noun.process' or classs == 'noun.object' or classs == 'noun.atrifact' or classs == 'noun.phenomenon') and (np2_list[-1].lower() in neutral_pronouns or np2_list[-1].lower() in plural_pronouns):
                    if(len(np1)==2 and noun_phrases[i][0] != noun_phrases[j][0]):
                        print "Avani"
                        np1.append(noun_phrases[j][0])
    
    #PRONOUN MATCH
    for i,np1 in enumerate(noun_phrases):
        #np1[1] = np1[1].lower()
        np1_list = np1[1].split()
        for j,np2 in enumerate(noun_phrases):
            #np2[1] = np2[1].lower()
            np2_list = np2[1].split()
            if(np1[1] in male_pronouns and np2[1] in male_pronouns):
                if len(noun_phrases[i]) == 2 and noun_phrases[i][0] != noun_phrases[j][0]:
                    noun_phrases[i].append(noun_phrases[j][0])

            elif(np1[1] in female_pronouns and np2[1] in female_pronouns):
                if len(noun_phrases[i]) == 2 and noun_phrases[i][0] != noun_phrases[j][0]:
                    noun_phrases[i].append(noun_phrases[j][0])

            elif(np1[1] in neutral_pronouns and np2[1] in neutral_pronouns):
                if len(noun_phrases[i]) == 2 and noun_phrases[i][0] != noun_phrases[j][0]:
                    noun_phrases[i].append(noun_phrases[j][0])

            elif(np1[1] in ambiguous_pronouns_singular and np2[1] in ambiguous_pronouns_singular):
                if len(noun_phrases[i]) == 2 and noun_phrases[i][0] != noun_phrases[j][0]:
                    noun_phrases[i].append(noun_phrases[j][0])

            elif(np1[1] in plural_pronouns and np2[1] in plural_pronouns):
                if len(noun_phrases[i]) == 2 and noun_phrases[i][0] != noun_phrases[j][0]:
                    noun_phrases[i].append(noun_phrases[j][0])

    

    
    #DATE MATCH
    for i,np1 in enumerate(noun_phrases):
        #np1[1] = np1[1].lower()
        np1_list = np1[1].split()
        for j,np2 in enumerate(noun_phrases):
            #np2[1] = np2[1].lower()
            np2_list = np2[1].split()
            for npp1 in np1_list:
                for npp2 in np2_list:
                    h1 = re.findall(r"(..?)[-/](..?)[-/](..?)|(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)",npp1.lower())
                    h2 = re.findall(r"(..?)[-/](..?)[-/](..?)|(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)",npp2.lower())
                    if(h1 != [] and npp2.lower() in dates or h2 != [] and npp1.lower() in dates):
                        if(len(np1)==2 and noun_phrases[i][0] != noun_phrases[j][0]):
                            np1.append(noun_phrases[j][0])
                        

                    elif(np1[1].lower() in dates and np2[1].lower() in dates):
                        if(len(np1)==2 and noun_phrases[i][0] != noun_phrases[j][0]):
                            np1.append(noun_phrases[j][0])

    #APPOSITIVES
    '''
    for i,np1 in enumerate(noun_phrases):
        np1[1] = np1[1].lower()
        np1_list = np1[1].split()
        for j,np2 in enumerate(noun_phrases):
            np2[1] = np2[1].lower()
            np2_list = np2[1].split()
            if(np2_list[-1][-1] == ','):
                if len(noun_phrases[i]) == 2:
                    noun_phrases[i].append(noun_phrases[j][0])
                if len(noun_phrases[j]) == 2:    
                    noun_phrases[j].append(noun_phrases[i][0])
    ''' 
    for i,np in enumerate(noun_phrases):
        if len(np) == 2:
            if i+1 <= len(noun_phrases)-1:
                if len(noun_phrases[i]) == 2 and noun_phrases[i][0] != noun_phrases[i+1][0]:
                    noun_phrases[i].append(noun_phrases[i+1][0])
                if len(noun_phrases[i+1]) == 2 and noun_phrases[i][0] != noun_phrases[i+1][0]:    
                    noun_phrases[i+1].append(noun_phrases[i][0])
    
    #RANDOM NP
    for i,np in enumerate(noun_phrases):
        if len(np) == 2 and noun_phrases[i][0] != noun_phrases[i-1][0]:
            j = noun_phrases[i-1][0]
            np.append(j)
    

    
    '''          
    elif(len(np1_list) == 1 and len(np2_list) == len(np1_list[0])):
        for i,npp2 in enumerate(np2_list):
            if(npp2[0]==np1_list[0][i]):
                continue
            else:
                flag1 = 1
                break
            if(flag1 == 0):
                if(len(np1)==2 and len(np2) == 2 and noun_phrases[i][0] != noun_phrases[j][0]):
                    np2.append(noun_phrases[i][0])
                    np1.append(noun_phrases[j][0])
    '''
    #print noun_phrases,"................................"
    return noun_phrases
              
    

def main(coref_nouns_maam,males,females):
    #coref_nouns_maam = ['pantex', 'flights', 'federal aviation administration', 'the number', 'pantex weapons plant', 'plutonium', 'faa', 'passes', 'flight', 'the plant', 'energy', 'plutonium', 'a highly radioactive\nelement', 'one chance in\n10 million', 'flight', 'this year', 'a safety board', 'trish neusch', 'amarillo', 'the airport', 'there', 'these planes', 'the faa air traffic manager', "a ``manual count on a pad,''", 'that 60-day accounting', '25 planes a day', 'pantex', 'the energy department', 'plutonium', 'the former weapons assembly plant', 'the amarillo airport', 'mcnulty', 'military planes', 'texas', 'he', 'about 25 percent of the airport traffic', 'a flight pattern\nover the plutonium storage bunkers', 'mcnulty', 'air traffic controllers', 'the bunkers', 'he', 'airport', 'the\nnuclear storage area', 'mcnulty', 'he', 'vortac', 'amarillo', 'he', 'mcnulty', 'these planes', 'the plutonium area', 'oklahoma', 'the plant', 'mcnulty', 'they', '02-14-96']
    #coref_nouns_maam = ['trans world airlines', 'additional shares of usair group inc.', 'the order', 'usair', 'another blow', 'washington-based usair', 'proposed transaction', 'chairman of twa', 'twa', 'usair', 'mr. icahn', 'twa', "usair's largest shareholder", 'mr. icahn', 'the attempt', 'usair', 'piedmont', 'twa', 'usair', 'piedmont', 'a securities analyst', 'mr. marckesano', 'twa', 'mr. icahn', 'usair', 'piedmont', 'twa', 'usair', 'department', 'it', 'it', 'serious application', 'department', 'new filing', 'usair', 'it', 'usair', 'twa', 'tender-offer', 'usair', 'mr. icahn', 'chairman and chief executive officer', 'usair', 'usair', 'the filings', 'mr. icahn', 'mr. colodny', 'twa', 'usair', 'twa', 'usair', 'usair', 'twa', 'usair', 'piedmont', 'mr. icahn', 'mr. colodny', 'the documents', 'mr. icahn', 'the documents', 'mr. colodny', 'twa', 'mr. icahn', 'he', 'mr. icahn', 'usair', 'twa', 'usair', 'mr. icahn', "twa's offer for usair", 'he', 'the bid', 'usair', 'piedmont', 'mr. icahn', 'twa', 'tender offer for piedmont', 'carl', 'usair', 'he', 'he', 'mr. icahn', 'mr. icahn', 'twa', 'the airline', 'usair', 'twa', 'usair', 'its', 'mr. icahn', 'twa', 'usair', 'twa', 'the drop', 'mr. icahn', 'icahn', 'twa', 'usair', 'piedmont', 'piedmont', 'merger with usair', 'usair', 'the merger', 'the company', 'its tender', 'usair', 'piedmont', 'twa', 'usair', 'mr. icahn', 'twa', 'sec', 'its', 'usair', 'twa', 'usair', 'usair', 'its', 'the piedmont acquisition', 'the company', 'it', 'bank', 'the purchase', 'usair', 'manufacturers hanover', 'usair', 'it', 'the acquisition', 'it', 'the airline', 'the filing', 'it', 'piedmont', 'usair', 'chairman and chief executive of piedmont', 'usair', 'the merger', 'twa', 'usair', 'twa', 'usair', 'the court', 'twa', 'more usair shares', "usair's tender offer for piedmont stock", 'usair', 'mr. icahn', 'twa', 'usair', 'usair', 'mr. icahn', 'twa', 'usair', 'transportation department', 'twa', 'mr. icahn', 'twa', 'usair', 'twa', 'it', 'hart-scott-rodino', 'transportation department', 'twa', 'department', 'the airline', 'usair', 'usair', 'twa', 'it', 'department', 'texas air']
    #mainarray = []
    #print coref_nouns_maam
    '''
    for line in coref_nouns_maam:
        line=line.lower()
        mainarray.append(line)
    '''
    #print mainarray

    #Final_Scores = Calculate_score(mainarray)
    #print Final_Scores
    #Final_Clusters = clustering(mainarray)
    #print Final_Clusters
    #print coref_nouns_maam
    results = matchings(coref_nouns_maam,males,females) 
    return results



if __name__ == '__main__':
    import sys
    main(coref_nouns_maam,males,females)

            
            