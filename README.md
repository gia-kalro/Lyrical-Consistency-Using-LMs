# Lyrical-Consistency-Using-LMs

Datasets:
- 

The full datasets containing all artists, time periods and genre used for training, evaluation and validation are:
- allLyricstrain.tsv
- allLyricsval.tsv
- allLyricstest.tsv


The smaller datasets, split by time period, used for training, evaluation and validation are:
  train1960s.tsv
  val1960s.tsv
  test1960s.tsv
  train1990s.tsv
  val1990s.tsv
  test1990s.tsv
  train2010s.tsv
  val2010s.tsv
  test2010s.tsv

The artist label's for the all the datasets are:

Full dataset:
- 0: Miley Cyrus
- 1: Taylor Swift
- 2: Demi Lovato
- 3: Mariah Carey
- 4: Christina Aguilera
- 5: Britney Spears
- 6: Aretha Franklin
- 7: Etta James
- 8: Nancy Sinatra
- 9: Elvis Presley
- 10: Chuck Berry
- 11: The Beatles
- 12: Green Day
- 13: Pearl Jam
- 14: Blink-182
- 15: Coldplay
- 16: Imagine Dragons
- 17: Foo Fighters
- 18: Johnny Cash
- 19: Dolly Parton
- 20: Glen Campbell
- 21: Shania Twain
- 22: Garth Brooks
- 23: Dixie Chicks
- 24: Carrie Underwood
- 25: Jason Aldean
- 26: Miranda Lambert

1960s: 
- 0: Aretha Franklin
- 1: Etta James
- 2: Nancy Sinatra
- 3: Elvis Presley
- 4: Chuck Berry
- 5: The Beatles
- 6: Johnny Cash
- 7: Dolly Parton
- 8: Glen Campbell

1990s:
- 0: Mariah Carey
- 1: Christina Aguilera
- 2: Britney Spears
- 3: Green Day
- 4: Pearl Jam
- 5: Blink-182
- 6: Shania Twain
- 7: Garth Brooks
- 8: Dixie Chicks

2010s:
- 0: Miley Cyrus
- 1: Taylor Swift
- 2: Demi Lovato
- 3: Coldplay
- 4: Imagine Dragons
- 5: Foo Fighters
- 6: Carrie Underwood
- 7: Jason Aldean
- 8: Miranda Lambert


Training the model:
- 
After choosing which dataset you are running, choose the corresponding .yaml file for training. Note that the .yaml for training the full data set is the train.yaml file. Using NLPScholar, you will run a TextClassification experiment on train mode. Depending on how your directories are set up, you may have to update the 
- trainfpath (path to the training dataset)
- validfpath (path to validation dataset)
- modelfpath (path where you are storing the model)

You can use the run_multi.sh for training the full dataset and the run_periods.sh for training the smaller datasets. 

Evaluating the model:
- 
To evaluate the model, choose the corresponding .yaml file. Note that the .yaml file for evaluating the full data set is the evaluate.yaml file. You will now run this TextClassification task on NLPScholar using evaluate mode. Depending on how your directories are set up, you may have to update the 
- datafpath (path to testing dataset)
- predfpath (the name of the output and where it will be stored)
- id2label (labels that correspond with artists (e.g. 0 corresponds to Miley Cyrus))

You can use the run_multi.sh for evaluating the full dataset and the run_periods.sh for evaluating the smaller datasets. 

Each time the model runs, it will output its predictions. To aggregate the predictions and get an overall predcitions by choosing the mode artist, utilize the aggregate_runs function in metrics.py. 

Analyzing the results:
- 

 To calculate F1-score, precision, recall, and accuracy, you can use metrics.py. To create a confusion matrix, you can use the confusion_matrix function in metrics.py. For further analysis on the data, such as computing overlap of words between artistis, use analyze_data.py
  



 














 
