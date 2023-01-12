#based on: https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python

#dictionary of contractions
CONTRACTIONS = { 
"ain't": "is not",
"aint": "is not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"i'd": "I would",
"i'd've": "I would have",
"i'll": "I will",
"i'll've": "I will have",
"i'm": "I am",
"i've": "I have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have",
"aint": "is not",
"arent": "are not",
"cant": "cannot",
"cantve": "cannot have",
"cause": "because",
"couldve": "could have",
"couldnt": "could not",
"couldntve": "could not have",
"didnt": "did not",
"doesnt": "does not",
"dont": "do not",
"hadnt": "had not",
"hadntve": "had not have",
"hasnt": "has not",
"havent": "have not",
"hed": "he would",
"hedve": "he would have",
"hes": "he is",
"howd": "how did",
"hows": "how is",
"id": "I would",
"idve": "I would have",
"ill": "I will",
"illve": "I will have",
"im": "I am",
"ive": "I have",
"isnt": "is not",
"itd": "it would",
"itdve": "it would have",
"itll": "it will",
"itllve": "it will have",
"lets": "let us",
"maam": "madam",
"maynt": "may not",
"mightve": "might have",
"mightnt": "might not",
"mightntve": "might not have",
"mustve": "must have",
"mustnt": "must not",
"mustntve": "must not have",
"neednt": "need not",
"needntve": "need not have",
"oclock": "of the clock",
"oughtnt": "ought not",
"oughtntve": "ought not have",
"shant": "shall not",
"shant": "shall not",
"shantve": "shall not have",
"shedve": "she would have",
"shellve": "she will have",
"shes": "she is",
"shouldve": "should have",
"shouldnt": "should not",
"shouldntve": "should not have",
"thatd": "that would",
"thatdve": "that would have",
"thats": "that is",
"thered": "there would",
"theredve": "there would have",
"theres": "there is",
"theyd": "they would",
"theydve": "they would have",
"theyll": "they will",
"theyllve": "they will have",
"theyre": "they are",
"theyve": "they have",
"wasnt": "was not",
"wed": "we would",
"wedve": "we would have",
"were": "we are",
"weve": "we have",
"werent": "were not",
"whatll": "what will",
"whatllve": "what will have",
"whatre": "what are",
"whats": "what is",
"whatve": "what have",
"whens": "when is",
"whered": "where did",
"wheres": "where is",
"wholl": "who will",
"whollve": "who will have",
"whos": "who is",
"whys": "why is",
"whyve": "why have",
"wont": "will not",
"wouldnt": "would not",
"wouldntve": "would not have",
"yall": "you all",
"youd": "you would",
"youdve": "you would have",
"youll": "you will",
"youllve": "you will have",
"youre": "you are",
"youve": "you have"
}

#dictionary of stopwords
STOPWORDS = {
'i': '',
'the': '', 
'and': '', 
'a': '', 
'it': '', 
'to': '', 
'is': '', 
'in': '', 
'of': '', 
'for': '', 
'on': '', 
'that': '', 
'at': '', 
'with': '', 
'do': '', 
'just': '', 
'this': ''
}

#dictionary of acronyms
ACRONYM_TRANSLATE = {
'lol' : 'laughing out loud',
'omg': 'oh my god',
'imo' : 'in my opinion',
'imho': 'in my honest opinion',
'btw' : 'by the way',
'idk' : 'I do not know',
'lmk' : 'let me know',
'tbh' : 'to be honest',
'tgif' : 'thank goodness it is Friday',
'rofl' : 'rolling on floor laughing',
'brb' : 'be right back',
'bbl' : 'be back later',
'ttyl' : 'talk to you later',
'thx' : 'thanks',
'ty' : 'thank you',
'yw' : 'you are welcome',
'asap' : 'as soon as possible',
'pov' : 'point of view',
'nbd' : 'no big deal',
'omw' : 'on my way',
'diy' : 'do it yourself',
'aka' : 'also known as',
'sms' : 'short message service',
'oatus' : 'on a totally unrelated subject',
'icymi' : 'in case you missed it',
'stfu' : 'shut the fuck up',
'bf' : 'boyfriend',
'gf' : 'girlfriend',
'so' : 'significant other',
'ily' : 'I love you',
'yolo' : 'you only live once',
'irl' : 'in real life',
'tmi' : 'too much information',
'atm' : 'at the moment',
'bff' : 'best friends forever',
'byob' : 'bring your own beer',
'cu' : 'see you',
'ur' : 'you are',
'fyi' : 'for your information',
'fomo' : 'fear of missing out',
'smh' : 'shaking my head',
'jmo' : 'just my opinion',
'nvm' : 'never mind',
'gl' : 'good luck',
'fwiw' : 'for what it is worth',
'gbu' : 'god bless you',
'imnsho' : 'in my not so humble opinion',
'rn' : 'right now',
'tldr' : 'too long did not read',
'qotd' : 'quote of the day',
'tbf' : 'to be fair',
'dkdc' : 'do not know do not care',
'idc' : 'I do not care',
'k' : 'okay',
'cwot' : 'complete waste of time',
'lmao' : 'laughing my ass off',
'mu' : 'miss you',
'ssdd' : 'same stuff different day',
'xoxo' : 'hugs and kisses',
'ott' : 'over the top',
'plz' : 'please',
'dm' : 'direct message',
'ruok' : 'are you okay',
'spk' : 'speak',
'sry' : 'sorry',
'sup' : 'what is up',
'ttfn' : 'ta ta for now',
'vn' : 'very nice',
'wtf' : 'what the fuck',
'y' : 'why',
'jk' : 'just kidding',
'bc' : 'because',
'tbc' : 'to be confirmed',
'tba' : 'to be announced',
'tbd' : 'to be determined',
'faq' : 'frequently asked questions',
'na' : 'not applicable',
'tia' : 'thanks in advance',
'np' : 'no problem',
'eod' : 'end of day',
'eta' : 'estimated time of arrival',
'embm' : 'early morning business meeting',
'cta' : 'call to action',
'roi' : 'return on investment',
'vfm' : 'value for money',
'ctr' : 'click through rate',
'bogof' : 'buy one get one free',
'otp' : 'one time password',
'hth' : 'hope this helps',
'wfh' : 'work from home',
'u' : 'you',
'w' : 'with'
}