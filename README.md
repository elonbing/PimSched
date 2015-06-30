#PimSched

PimSched helps you study foreign vocabulary by converting lists of vocabulary/translations into audiolessons. The audiolesson-format allows you to study vocabulary while in the car, at work, cleaning the house, etc. The idioms and translations are played (in spoken form, using Google's unofficial TTS "API") in ever increasing intervals: the Pimsleur-intervals, found by various researchers to cause the largest amount of retention in the shortest amount of time.


### How to use
* Download the code
* Make PimSched.py executable: chmod +x ./PimSched.py
* ./PimSched.py to run

**Command-line arguments**

*PimSched.py language1 language2 wordlist [-o outputpath]*  

**Required**: *language1*: ISO-abbreviation(English=en, German=de, etc) of language of idioms on the left side of the "="  
**Required**: *language2*: ISO-abbreviation(English=en, German=de, etc) of language of idioms on the right side of the "="  
**Required**: *wordlist*: path to vocabularylist, a file with idioms and translations, separated by "="  
**Optional**: outputpath: Path specifying where the MP3-audiolesson should be stored. Default: ./result.mp3

For example:
* ./PimSched.py en fr /path/to/wordlist.txt
* ./PimSched.py en fr /path/to/wordlist.txt -o ~/French/chapter5.mp3


**Dependencies**  
* Python2

All other dependencies are already included for your convenience

**Information for experienced Linux-users**

If a library is also installed somewhere in your PYTHONPATH, PimSched will use that version; if not, PimSched will fall back to the included library. The included dependencies are located in the included_libraries folder; you can remove that folder if the libraries PimSched requires are installed into your PYTHONPATH. PimSched requires the following libraries:
* pydub
* argparse (already included in the standard library for Python>=2.7)