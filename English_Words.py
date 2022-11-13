from PyDictionary import PyDictionary
import random
words = ['abort', 'absurd', 'accord', 'accumulate', 'bankrupt', 'blast', 'breed', 'brew', 'caption', 'cater', 'cathedral', 'chamber', 'chronic', 'commence', 'deficiency', 'deficit', 'degradedelegate', 'deliberate', 'explicit', 'extract', 'extraordinary', 'facilitate', 'faculty', 'fatal', 'federal', 'fertile', 'guardian', 'gulf', 'habitat', 'halt', 'haunt', 'headquarters', 'intervene', 'intrigue', 'judicial', 'keen', 'knot', 'lease', 'legislate', 'sweep', 'swell', 'swift', 'tease', 'telegraph', 'temporary', 'tempt', 'tenant', 'yield']
def eng_word():
    word = random.choice(words)
    dict = PyDictionary()
    meaning = dict.meaning("%s" %word)
    print(word)
    try:
        print("Noun: "+meaning["Noun"][0], "\nVerb: " + meaning["Verb"][0])
    except:
        try:
            print("Noun: "+meaning["Noun"][0])
        except:
            print("Verb: " +meaning["Verb"][0])