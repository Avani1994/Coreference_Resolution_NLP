#!/bin/bash
chmod +x getenv.sh
./getenv.sh
source virtual_env/bin/activate
pip install -r requirements.txt
python -m nltk.downloader wordnet
python parsernltk.py test1.listfile female.txt male.txt