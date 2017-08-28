Team-A^2

The program has been tested on machine 1-7, engman lab. The program is successfully running with proper environment 
and the output files are saved in our "responses" directory inside "res folder".

Python files needed to run the script file is :
1. corefoutput.py
2. Feature_Copy.py
3. parsernltk.py

Program can be succesfully run from file: parsernltk.py
You need 2 extra input files namely female.txt and male.txt

For installing and actiavting virtual environment:
1. $ cd NLP_Proj_Final
2. $ chmod + x getenv.sh
3. $ ./getenv.sh
4. $ source virtual_env/bin/activate.csh

Now after activating virtual environment use these commands:

Firstly install the nltk and lxml using:
1. pip install -r requirements.txt

For installing wordnet:
1. python
2. import nltk
3. nltk.download()
4. wordnet
5. exit()


Please use the commands as:
1. ./run_me.sh
2. Python new2-coref-scorer.py responselist.txt /home/asesh/NLP_Proj_Final/dev -V   (This is for development set)
3. Python new2-coref-scorer.py responselist.txt /home/asesh/NLP_Proj_Final/tst1 -V   (This is for Initial Test set)

Scorer program used is: new2-coref-scorer.py

nltk and lxml package needs to be installed in order to run the program successfully, We have set up the
Virtual environment needed to run the program. Let us know if any problem occurs during execution.

Reference to some support codes (if needed) have been mentioned in respective program files.

For details of our system : you can have a look at A^2-Poster.pdf 