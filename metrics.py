import pandas as pd
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import argparse


def aggregate_runs(case,n):
    df=None
    cols=[]
    for i in range(1,n+1):
        run='run'+str(i)
        cols.append(run)
        fpath="./predictions/pred_"+case+"_"+str(i)+".tsv"
        df_run=pd.read_csv(fpath, sep="\t")
        df_run=df_run[['target','predicted']]
        if df is None:
            df=df_run
        else:
            df=pd.merge(df,df_run['predicted'],how='inner',left_index=True,right_index=True)
        df.rename(columns={'predicted': 'run'+str(i)},inplace=True)
            
    print("Computing mode")
    mode= df[cols].mode(axis=1).iloc[:,0]
    
    df=pd.DataFrame()
    df['target']=df_run['target']
    df['predicted']=mode
   

    df['tgt'] = df['target'].apply(lambda x: i2a_dict[x])
    df['pred'] = df['predicted'].apply(lambda x: a2i_dict[x])
    true = df['tgt']
    pred = df['predicted']
    
    precision, recall, f1, _ = precision_recall_fscore_support(true, pred, average="macro")
    acc=accuracy_score(true, pred)
    print("Overall Metrics:")
    print("     Precision: " + str(round(precision,4)))
    print("     Recall: "+ str(round(recall,4)))
    print("     F-1 Score: "+ str(round(f1,4)))
    print("   Acc. Score: "+str(round(acc,4)))

    print()
    print("Per-Artist Metrics:")
    labels=list(i2a_dict.values())
    artistMetrics = precision_recall_fscore_support(df['tgt'], df['predicted'], labels=labels,average=None)
    df_artists=pd.DataFrame(columns=["Artist","Precision","Recall","F1-Score"]) #,dtype=[str,float,float,float])
    for i, label  in enumerate(labels):
        artist,prec,rec,f1=label,artistMetrics[0][i],artistMetrics[1][i],artistMetrics[2][i]
        df_artists.loc[len(df_artists)] =[artist,prec,rec,f1] 
    
   
   
    pd.set_option('display.float_format', lambda x: '%.3f' % x)    
    # print(df_artists.sort_values(by='F1-Score',ascending=False))
    print(df_artists)
    
    
    print("Constructing Confusion Matrix")
    
    conf_mat = confusion_matrix(true,pred,labels=labels)
    
    artists=labels
    conf_df = pd.DataFrame(conf_mat, index=artists, columns=artists)

    # Save the confusion matrix to a CSV file
    conf_df.to_csv('confusion_matrix_'+case+'.csv', index=True)
    # Save artist metrics
    df_artists.to_csv('artist_metrics_'+case+'.csv', index=True)
    # Save detailed outputs 
    df_agg=df[['tgt','predicted']]
    df_agg.to_csv('predictions_'+case+'.csv', index=True)
    

    #print(conf_mat)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_df, annot=True, cmap='Blues', fmt='d')
    plt.xlabel('Predicted Labels')
    plt.ylabel('Actual Labels')
    plt.title('Confusion Matrix')
    #plt.show()
    plt.savefig('confmat_'+case+'.png', dpi=300, bbox_inches='tight')

    
    return
            
        
        
# def calculate_metrics(fPath):
#     df = pd.read_csv(fPath, sep="\t")
#     df['tgt'] = df['target'].apply(lambda x: i2a_dict[x])
#     df['pred'] = df['predicted'].apply(lambda x: a2i_dict[x])
#     true = df['tgt']
#     pred = df['predicted']

    

#     precision, recall, f1, _ = precision_recall_fscore_support(true, pred, average="macro")
#     print("Overall Metrics:")
#     print("     Precision: " + str(round(precision,3)))
#     print("     Recall: "+ str(round(recall,3)))
#     print("     F-1 Score: "+ str(round(f1,3)))

#     print()
#     print("Per-Artist Metrics:")
#     labels = sorted(df['tgt'].unique())
#     precs,recs,f1s,supps = precision_recall_fscore_support(true, pred, labels=labels, average=None)
#     df_artists=pd.DataFrame(columns=["Artist","Precision","Recall","F1-Score"]) #,dtype=[str,float,float,float])
#     for i, label in enumerate(labels):
#         artist,prec,rec,f1=label,precs[i],recs[i],f1s[i]
#         df_artists.loc[len(df_artists)] =[artist,prec,rec,f1] 
#         # print("  Artist: "+label)
#         # print("    Precision: "+str(round(prec)))
#         # print("    Recall: "+str(round(rec,3)))
#         # print("    F1-Score: "+str(round(f1,3))+"\n")
   
#     #df_artists['Artist'] = df_artists['Artist'].str.ljust(10)
#     pd.set_option('display.float_format', lambda x: '%.3f' % x)    
#     print(df_artists.sort_values(by='F1-Score',ascending=False))
#     return


if __name__ == "__main__":
    # Create parser
    parser = argparse.ArgumentParser(description='final')
    parser.add_argument('--case', type=str, help='case: 1960s, 1990s, 2010s, all')
    parser.add_argument('--n', type=int, help='number of runs')
   # args.case='all'
   # args.n=6
    args = parser.parse_args()
    

    
    if  args.case == 'all':
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
    aggregate_runs(args.case,args.n)
    # file_path = "./predictions/allLyricstest.tsv"
    # calculate_metrics(file_path)
