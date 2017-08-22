#from nltk import Nonterminal, nonterminals, Production, CFG
import sys
#import nltk
#from nltk.parse import RecursiveDescentParser
#from nltk.corpus import wordnet as wn
#from textblob import TextBlob
import xml.etree.ElementTree
from pprint import pprint
from lxml import etree
import np_extraction
import lxml.etree as ET
import mmap
import corefoutput
import Feature_Copy
'''
def inputfileforcluster(inputfile, coref_ids, np):
	

	f = open(inputfile, 'r')
	fs = f.read()
	#fs = fs.lower()
	#print fs
	i = 0
	for n_phrase in np:
		
		init_start=0
		flag = 0
		for corefs in coref_ids:
			if n_phrase not in corefs:
				continue
			else:
				flag = 1
				break
		while fs.find(n_phrase,init_start)!=-1:
			
			cur_index=fs.find(n_phrase,init_start)
			
			if fs[fs.find(n_phrase,init_start)-2:fs.find(n_phrase,init_start)] not in '">' and fs[fs.find(n_phrase,init_start)+len(n_phrase):fs.find(n_phrase,init_start)+len(n_phrase) + 5] not in '</COREF>' and flag == 0:
				
				fs=fs[:cur_index-1]+'<COREF ID="*'+str(i)+'">'+fs[cur_index:cur_index+len(n_phrase)]+'</COREF>'+fs[cur_index+len(n_phrase):]
				#print fs 
				i = i+1
				#print init_start,"if"
				init_start=cur_index+len(n_phrase)
			else:
				#print init_start,"else"
				init_start=cur_index+len(n_phrase)
		#break
		coref_ids = coref_ids + [n_phrase]
	print fs
	f.close()
	f = open(inputfile, 'w')
	f.write(fs)
	#f.seek(0)
	f.close()
	return {'self_coref':fs,'inputfile':f}		
'''			
			
# returns all Coref Ids (Anaphora and their IDS)
def parsexml(inputfile):
	pre_coref_ids = []
	e = xml.etree.ElementTree.parse(inputfile).getroot()

	
	for phrases in e.findall('COREF'):
		#pre_coref_ids = pre_coref_ids + [atype.text.lower()]
		sing_string = phrases.text
		if "\n" in sing_string:
			sing_string = sing_string[:sing_string.index("\n")] + " " + sing_string[sing_string.index("\n")+1:]

		pre_coref_ids = pre_coref_ids + [[str(phrases.get('ID')),sing_string]]
	#print pre_coref_ids
	return pre_coref_ids

'''
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
'''

def main():
	#print('avani')

	inputfiles_list = []

	#Input file names
	input_file = sys.argv[1]
	female_file = sys.argv[2]
	male_file = sys.argv[3]
	

	#Read input Files : Inputfiles, female corpus, male corpus
	f = open(input_file, 'r')
	fs = f.read().splitlines()
	m = open(male_file, 'r')
	m_file = m.readlines()
	fe = open(female_file, 'r')
	f_file = fe.readlines()

	#Store males and females names in list
	fe_file = []
	ma_file = []
	for fem in f_file:
		fe_file = fe_file + [fem.rstrip()]
	for ma in m_file:
		ma_file = ma_file + [ma.rstrip()]

	#Store input file names in list
	for line in fs:
		inputfiles_list = inputfiles_list + [line]
	

	for file in inputfiles_list:
		file_temp = file.split('/')[-1]
		filename = file_temp.split('.')[0]
		inFile = open(file, 'r')
		coref_ids = parsexml(file)
		

		# apply all rules and return antecedents for anaphoras
		Final_Result = Feature_Copy.main(coref_ids,ma_file[6:],fe_file[6:])
		
		# Generate output in desired Format
		Outputfile	= corefoutput.main(Final_Result)

		inFile.close()

		# Write output to response files.
		fwrite = open('/Users/avanisharma/Masters/1st_SEM/NLP/Project_1/res/responses/'+filename+'.response', 'w')
		fwrite.write(Outputfile)
		fwrite.close()

	#Generate responselist.txt	
	responsefile = open('/Users/avanisharma/Masters/1st_SEM/NLP/Project_1/res/responselist.txt', 'w')
	for file in inputfiles_list:
		file_temp = file.split('/')[-1]
		filename = file_temp.split('.')[0]
		#print filename
		responsefile.write('responses/'+filename+'.response\n')

	responsefile.close()
	
main()
