#LING 5410
#Jared Fromknecht and Maia Petee

#Internetification

#This aims to be a program that can take the dialogue of any work of fiction and "internetify it," using a few tools:
#Text transformations
#An informal register
#Acronymics
#Emoticons
#...and more!

import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sentiment

#Defining our dictionary of single lexeme replacements as well as multiple-word replacements (contractions, etc.)
replace = {

    'sister ' : 'sis ',
    'take delight' : 'love',
    'at the assemblies' : 'at the club',
    'fortnight ' : 'two weeks ',
    'decline' : 'turn down',
    ', however,' : '',
    'having spoken' : 'speaking',
    'aye' : 'yeah',
    'oh!': 'omg!!',
    ' very ' : ' ultra ',
    'young man' : 'fuccboi',
    'beautiful' : 'gorgeous',
    ' miss ' : ' ',
    ' thus ' : '',
    'above them' : 'more than them',
    'her ladyship': 'that bitch',
    'lady' : '',
    'my dear' : 'my homie',
    'tiresome' : 'boring',
    'design' : 'goal',
    'over-scrupulous' : 'OCD',
    'a few lines' : 'a DM',
    'mrs.' : 'that chick',
    'mr.' : '',
    'cried' : 'yelled',
    'till' : 'til',
    'behaviour' : 'behavior',
    'befall' : 'happen to',
    'is to' : 'will',
    'what will' : 'whatll',
    'shall' : 'will',
    'feelings' : 'feels',
    'letter' : 'PM',
    'affection ' : 'luv',
    ' ill ' : ' sick ',
    'father' : 'dad',
    'honour' : 'honor',
    'manner' : 'way',
    'mother' : 'mom',
    'oh' : 'whaaaaat',
    'amiable' : 'friendly',
    'myself' : 'me',
    'family' : 'fam',
    'brother' : 'bro',
    'carriage' : 'ride',
    'manners' : 'social skills',
    'sir' : 'fam',
    'neighbourhood' : 'hood',
    'marrying' : 'hooking up with',
    'good-humoured' : 'cheerful',
    'marry ' : 'hook up with ',
    'scarcely' : 'hardly',
    'perfectly' : 'just',
    'cannot' : 'cant',
    'pride' : 'ego',
    'whom' : 'who',
    'countenance' : 'face',
    'favourite' : 'fave',
    'gentleman' : 'dude',
    'evening' : 'night',
    'cousin' : 'cuz',
    'yes' : 'yeah',
    'endeavour' : 'try',
    'invitation' : 'msg',
    'exceedingly' : 'very much',
    'madam' : 'bitch',
    'certainly' : 'totes',
    'character' : 'personality',
    'instantly' : 'right away',
    'married' : 'attached',
    'what say you' : 'whaddaya say',
    'make extracts' : 'write book reports',
    'adjusting her ideas' : 'thinking about it',
    'parsonage' : 'house',
    ' morrow ' : ' next day ',
    'to-morrow' : 'tomorrow',
    ' love ' : ' lovee ',
    'mistaken' : 'wrong',
    'pleased' : 'happyyy',
    'glad' : 'happpy',
    'handsomest' : 'hottest',
    'handsome' : 'hottt',
    'arrival' : 'visit',
    'obliged' : 'gave into',
    'disposition' : 'personality',
    'eldest' : 'oldest',
    'has got' : 'has',
    ' ought ' : ' should ',
    'never could be' : 'couldnt be',
    'never can' : 'cant',
    'speedily' : 'quickly',
    'he has' : 'hes',
    'was totally ignorant' : 'didnt know',
    'had not' : 'hadnt',
    'acquaintance with' : 'talking to',
    'be contented' : 'deal with it',
    'wonder at' : 'care about',
    'engaged' : 'hookin up on the regs',
    'learnt' : 'learned',
    'tolerably' : 'kinda',
    'quite' : 'super',
    'endeavoured' : 'but',
    'pardon' : 'pls',
    'at last' : 'finally',
    'in want of' : 'needin',
    'chaise' : 'ride',
    'compassion' : 'feels',
    'parted' : 'peaced',
    'circumstance ' : 'stuff ',
    'everybody' : 'errbody',
    'appearance' : 'looks',
    'coming' : 'comin',
    'distressed' : 'shook',
    'elopement' : 'hookup',
    'imprudence' : 'craziness',
    'quitted' : 'quit',
    'prevented' : 'stopped',
    'pianoforte' : 'keyboard',
    'comprehend' : 'understand',
    'housekeeper' : 'girl',
    'vexation' : 'pissiness',
    'folly' : 'fuckedupness',
    'condescension' : 'throwin shade',
    'dreadful' : 'shitty',
    'could not' : 'couldnt',
    'the matter' : 'this shit',
    'falsehood' : 'lie',
    'improbable' : 'not gonna happen',
    'observing' : 'seein',
    'dancing' : 'twerkin',
    'detest' : 'hate',
    'an assembly' : 'a party',
    'fastidious' : 'picky af',
    ' is not ' : ' aint ',
    'every thing' : 'everything',
    'would not' : 'wouldnt',
    'most beautiful' : 'hottest',
    'who is' : 'whos',
    'she is' : 'shes',
    'tolerable' : 'aight',
    'i am' : 'im',
    'i want to' : 'i wanna',
    'lively' : 'fun',
    'had better' : 'oughta',
    'country-town' : 'ratchet',
    'that is' : 'thats',
    'marrying' : 'getting',
    ' man ' : ' guy ',
    'such another' : 'another',
    ' men ' : ' dudes ',
    ' men,' : ' dudes,',
    'dupe' : 'tool',
    'you will' : 'youll',
    'should to do' : 'should',
    'i must' : 'i',
    'confess' : 'admit',
    'has no pleasure in' : 'doesnt like',
    'despises' : 'hates',
    'and then' : 'then',
    'i have not' : 'i dont have',
    'you have' : 'youve',
    'rather singular' : 'kinda weird',
    'astonished' : 'shook',
    'should have' : '',
    'it has been' : 'its been',
    'father' : 'dad',
    'ought to' : 'should',
    'diverted' : 'amused',
    'this was all': 'all this shit was',
    'exact': 'right on',
    'hardly': 'barely',
    'blowsy': 'fucked up',
    'came into': 'came in',
    'petticoat': 'shorts',
    ' most ': ' craziest ',
    'vex me' : 'piss me off',
    'vex you' : 'piss you off',
    'singular': 'weird',
    'excessive': 'crazy high',
    'well settled': 'settled down',
    'an attorney': 'a lawyer',
    'capital': 'good',
    'of it': '',
    'afforded': 'could offer',
    'an idle fellow': 'a lazyass',
    'penetration' : 'insight',
    'sagacity' : 'intuition',
    'admirer' : 'crush',
    'a delightful': 'an awesome',
    'delightful': 'awesome',
    'delighted' : 'happy',
    'who has' : 'whos',
    'where is' : 'wheres',
    'i dare say' : 'i guess',
    'up stairs' : 'upstairs',
    'contrivance' : 'manipulation',
    'would have' : 'wouldve',
    'it is' : 'its',
    'we will' : 'well',
    'it would' : 'itd',
    'unforgiving' : 'mean',
    'more advantageously' : 'better',
    'many respects' : 'many ways',
    'do you not' : 'dont you',
    'encouragement': 'sign',
    'were grave': 'had RBF',
    'silent' : 'left me on read',
    'exaggerate them': 'talk them up',
    'afterwards' : 'after that',
    'affectionate' : 'nice',
    ' ill ' : ' sick ',
    'approbation' : 'approval',
    'roused' : 'slayed',
    'assiduously' : 'intensely',
    ' court ' : ' hit up ',
    'courted' : 'messaged',
    'liveliness' : 'cleverness',
    'rather' : 'kinda',
    'uncivil': 'bitchy',
    'impertinence': 'sass',
    'charmingly': 'well',
    'beauty': 'hotttness',
    'indeed' : ''
}

#Our main internetification function.
def internetify(text):

    #Opening the source text passed through and storing it as a variable
    source = open(text, 'r', encoding='utf-8')
    lit = source.read()
    outfile = open(text + ".text.out", 'w', encoding='utf-8')
    
    #defines a class to use as an argument in the re.sub function,
    #this portion of the code came from https://stackoverflow.com/questions/16761652/how-to-properly-iterate-with-re-sub-in-python
    #did not have any idea you could have counters work on the initialization and call level until I saw this
    class subNumbers1(object):
        #sets a counter on initialization
        def __init__(self, start=0):
            self.count = start - 1

        #on call within the sub function (i.e. when there is a match and replacement) - +1 the counter and return as a value "***{selfcounts value}***" to
        #to be used as the string replacement
        def __call__(self, match):
            self.count += 1
            return "***{}***$".format(self.count)
        

    #Creating one of two parallel texts - this version has all dialogue items subbed for index numbers so we can iterate over the items for re.sub and
    #restore the items to their rightful places.
    placeholder_lit = re.sub(r"“[^“”]*”", subNumbers1(), lit)
    placeholder_lit2 = placeholder_lit.split("$")

    #print(placeholder_lit2)

    #Creating the second of two parallel texts; this version just stores the lowercased items in a list that will be used as a template for the transformations
    dialogue = re.findall(r"“[^“”]*”", lit)
    transformed = [item.lower() for item in dialogue]

    #These are the two lists that will house both the iterated and the transformed dialogue items; they will be "melded" at the end.
    transformed_after = []
    placeholder_lit3 = []

    #Initializing an instance of sentiment analysis using Vader
    s = sentiment()

    for i in transformed:

        score = s.polarity_scores(i)
        #print(score)

        #Using the total sentiment score for a dialogue item to determine what acronymic gets appended to it

        if score['compound'] != 0.0:
            if score['neu'] >= 0.9 and score['pos'] > 0.05:
                i = i[:-2]
                i = i + ' lol”'
            elif score['neg'] >= 0.32:
                i = i[:-2]
                i = i + ' ;_;”'
            elif score['neg'] > .2 and score['neg']<= .31 and (score['neg'] > score['pos']):
                i = i[:-2]
                i = i + ' -.-”'
            elif score['pos'] >= .25 and score['pos'] <= 0.49 and (score['pos'] > score['neg']):
                i = i[:-2]
                i = i + ' :)”'
            elif score['pos'] >= .5 and score['pos'] <= 0.61:
                i = i[:-2]
                i = i + ' w00t!”'
            elif score['pos'] >= .62:
                i = i[:-2]
                i = i + ' w00t! ^.^”'
            elif score['neu'] >= 0.9 and score['neg'] > 0.05:
                i = i[1:]
                i = '“lol ' + i
            else:
                pass
        else:
            pass

        #Finally, the lexical replacement
        for key, value in replace.items():
            while key in i:
                i = i.replace(key, value)

                if key not in i:
                   break
               
        transformed_after.append(i)
   
    #Defining our iteration counter that will allow us to match re.subbed items to their proper places
    iteration_counter = 0

    y = "***" + str(iteration_counter) + "***"
        
    global final

    for x in placeholder_lit2:
        if iteration_counter < len(transformed_after):
            y = "***" + str(iteration_counter) + "***"              
            final = x.replace(y, transformed_after[iteration_counter])  
            iteration_counter += 1
            placeholder_lit3.append(final)
        else:
            break

    #Let's hope all that worked. Our list items are replaced; let's join them back up again.
    final2 = "".join(placeholder_lit3)
    final3 = final2.replace('  ', ' ')
    print(final3, file=outfile)
    print(final3)

internetify('Texts/pride.txt')