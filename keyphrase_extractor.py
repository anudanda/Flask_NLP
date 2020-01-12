import pandas as pd
import numpy as np
import re
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import pickle
#stemmer = SnowballStemmer("english") ; Bad root words with stemmer , use only lemmatizer
L = WordNetLemmatizer()




# open stopwords file, create a list of stopwords, close.
#pd_RTMdata = pd.read_excel('RTM_comment_tags.xlsx',sheet_name = '2019-07-22_taggedComments (2)')


def key_phrase_extract(sentence):
        
        list_interim = list()
        tokens_postagged = nltk.pos_tag(nltk.word_tokenize(sentence))
        tokens_postagged = [tup for tup in tokens_postagged if tup[1] not in ('CC','RP','DT')]
        #print(pd_RTMdata.loc[j,'comment'])
        for i in range(2,len(tokens_postagged)):        
    
            if ((tokens_postagged[i][1] in ('NN','NNS')) and
                  (tokens_postagged[i-1][1] in ('NN','NNS')) and
                  (tokens_postagged[i-2][1] in ('JJ','JJR','JJS'))):
                  list_interim.append((" ".join((tokens_postagged[i-2][0],tokens_postagged[i-1][0],tokens_postagged[i][0]))))    
                            
            elif ((tokens_postagged[i][1] in ('NN','NNS')) and
                  (tokens_postagged[i-1][1] in ('JJ','JJR','JJS')) and
                  (tokens_postagged[i-2][1] in ('RB','RBR','RBS'))):
                  list_interim.append((" ".join((tokens_postagged[i-2][0],tokens_postagged[i-1][0],tokens_postagged[i][0]))))    
    
            elif ((tokens_postagged[i][1] in ('NN','NNS')) and
                  (tokens_postagged[i-1][1] in ('JJ','JJR','JJS'))) :
                  list_interim.append((" ".join((tokens_postagged[i-1][0],tokens_postagged[i][0]))))
            
            elif ((tokens_postagged[i][1] in ('NN','NNS')) and
                  (tokens_postagged[i-1][1] in ('RB','RBR','RBS'))):
                  list_interim.append((" ".join((tokens_postagged[i-1][0],tokens_postagged[i][0]))))
                  
    
            elif ((tokens_postagged[i-1][1] in ('NN','NNS')) and
                  (tokens_postagged[i][1] in ('JJ','JJR','JJS')) and
                  (tokens_postagged[i-2][1] in ('RB','RBR','RBS'))):
                  list_interim.append((" ".join((tokens_postagged[i-2][0],tokens_postagged[i-1][0],tokens_postagged[i][0]))))    
    
            elif ((tokens_postagged[i-2][1] in ('NN','NNS')) and
                  (tokens_postagged[i-1][1] in ('JJ','JJR','JJS')) and
                  (tokens_postagged[i][1] in ('RB','RBR','RBS'))):
                  list_interim.append((" ".join((tokens_postagged[i-2][0],tokens_postagged[i-1][0],tokens_postagged[i][0]))))    
    
            elif ((tokens_postagged[i-1][1] in ('NN','NNS')) and
                  (tokens_postagged[i][1] in ('JJ','JJR','JJS')) and
                  (tokens_postagged[i-2][1] in ('VB','VBD','VBG','VBN','VBP','VBZ'))):
                  list_interim.append((" ".join((tokens_postagged[i-2][0],tokens_postagged[i-1][0],tokens_postagged[i][0]))))    
    
            elif ((tokens_postagged[i][1] in ('NN','NNS')) and
                  (tokens_postagged[i-1][1] in ('JJ','JJR','JJS')) and
                  (tokens_postagged[i-2][1] in ('VB','VBD','VBG','VBN','VBP','VBZ'))):
                  list_interim.append((" ".join((tokens_postagged[i-2][0],tokens_postagged[i-1][0],tokens_postagged[i][0]))))    
    
        if len(tokens_postagged) > 1:
            if ((tokens_postagged[1][1] in ('NN','NNS')) and
                    (tokens_postagged[0][1] in ('JJ','JJR','JJS'))) :
                    list_interim.append((" ".join((tokens_postagged[1][0],tokens_postagged[0][0]))))
                
            elif ((tokens_postagged[1][1] in ('NN','NNS')) and
                      (tokens_postagged[0][1] in ('RB','RBR','RBS'))):
                      list_interim.append((" ".join((tokens_postagged[1][0],tokens_postagged[0][0]))))
    
        #print(list_interim)
        #print(j)
        return( ';'.join(list_interim))
        

## Creating pickle file 
pickle.dump(key_phrase_extract, open('model.pkl','wb'))        

# Load model to compare result
model = pickle.load(open('model.pkl','rb'))    
