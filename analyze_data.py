import pandas as pd
import string
import nltk
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
import argparse

def analyze(fpath):
    print("Analyzing ",fpath)
    df=pd.read_csv(fpath, sep="\t")
    # Remove stop words, these words add more noise rather than signal
    stop_words = set(stopwords.words('english'))
    counts =  [defaultdict(int) for _ in range(len(i2a_dict))]
    table = str.maketrans('', '', string.punctuation)
    max_len=[0]*len(i2a_dict)
    avg_len=[0]*len(i2a_dict)
    samples=[0]*len(i2a_dict)
    for i in range(df.shape[0]):
        sent=df.loc[i,'text'].lower()
        idx=df.loc[i,'label']
        #tokenize
        temp=word_tokenize(sent)
        samples[idx]+=1
        max_len[idx]=max(max_len[idx],len(temp))
        avg_len[idx]+=len(temp)
        #remove punctuations
        temp = [token.translate(table) for token in temp]
        #remove empty tokens
        temp = [token for token in temp  if token != '']
        #remove stop words
        temp = [token for token in temp if token not in stop_words]    
        #update counts
        for token in temp:
            counts[idx][token]+=1
   
    for idx  in range(len(i2a_dict)):
        top_words = dict(sorted(counts[idx].items(), key=lambda item: item[1], reverse=True)[:10])
        print("Stats for :",i2a_dict[idx])
        print(top_words.keys())
        print("Max length =",max_len[idx])
        print(f"Avg length ={avg_len[idx]/samples[idx]:.0f}")
   
    #compute overlap
    olaps=defaultdict(float)
    ist=0
    ind=-1
    for idx in range(len(i2a_dict)):
        iwords=set(dict(sorted(counts[idx].items(), key=lambda item: item[1], reverse=True)[ist:ind]).keys())
        iartist=i2a_dict[idx]
        for jdx in range(idx+1,len(i2a_dict)):
            jartist=i2a_dict[jdx]
            key=(iartist,jartist)
            jwords=set(dict(sorted(counts[jdx].items(), key=lambda item: item[1], reverse=True)[ist:ind]).keys())
            for word in iwords:
                if word in jwords:
                    olaps[key]+=1
            olaps[key]=olaps[key]/len(iwords.union(jwords))
            
    
    top_olaps = dict(sorted(olaps.items(), key=lambda item: item[1], reverse=True)[:10])         
    print("Top overlaps between artists")      
    print(top_olaps.keys())
   
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='final')
    parser.add_argument('--case', type=str, help='case: 1960s, 1990s, 2010s, all',default='2010s')
   
    args = parser.parse_args()
    

    
    if  args.case == 'all':
        fpath='./data/allLyricstrain.tsv'
        i2a_dict= {
             0:"Miley Cyrus",
            1:"Taylor Swift",
            2:"Demi Lovato",
            3:"Mariah Carey",
            4:"Christina Aguilera",
            5:"Britney Spears",
            6:"Aretha Franklin",
            7:"Etta James",
            8:"Nancy Sinatra",
            9:"Elvis Presley",
            10:"Chuck Berry",
            11:"The Beatles",
            12:"Green Day",
            13:"Pearl Jam",
            14:"Blink-182",
            15:"Coldplay",
            16:"Imagine Dragons",
            17:"Foo Fighters",
            18:"Johnny Cash",
            19:"Dolly Parton",
            20:"Glen Campbell",
            21:"Shania Twain",
            22:"Garth Brooks",
            23:"Dixie Chicks",
            24:"Carrie Underwood",
            25:"Jason Aldean",
            26:"Miranda Lambert"
         }
    elif args.case=='1960s':
        fpath='./data/train1960s.tsv'
        i2a_dict={
            0: "Aretha Franklin",
            1: "Etta James",
            2: "Nancy Sinatra",
            3: "Elvis Presley",
            4: "Chuck Berry",
            5: "The Beatles",
            6: "Johnny Cash",
            7: "Dolly Parton",
            8: "Glen Campbell"
        }
    elif args.case=='1990s':
        fpath='./data/train1990s.tsv'
        i2a_dict={
            0: "Mariah Carey",
            1: "Christina Aguilera",
            2: "Britney Spears",
            3: "Green Day",
            4: "Pearl Jam",
            5: "Blink-182",
            6: "Shania Twain",
            7: "Garth Brooks",
            8: "Dixie Chicks"
        }
    else:
        fpath='./data/train2010s.tsv'
        i2a_dict={
            0: "Miley Cyrus",
            1: "Taylor Swift",
            2: "Demi Lovato",
            3: "Coldplay",
            4: "Imagine Dragons",
            5: "Foo Fighters",
            6: "Carrie Underwood",
            7: "Jason Aldean",
            8: "Miranda Lambert"
        }

    a2i_dict= {v: k for k, v in i2a_dict.items()}
    
    
   
    analyze(fpath)
    

    

