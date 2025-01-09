#!/usr/bin/bash

for p in 1960s 1990s 2010s
do
	for i in 1 2 3 4 5 6 7 8 9 10
	do
		echo "Performing run $i for period $p"
		for y in train$p.yaml
		do
			echo "Running python ../NLPScholar/main.py $y"
			python ../NLPScholar/main.py $y
		done
	
		for y in eval$p.yaml
		do
			echo "Running python ../NLPScholar/main.py $y"
			python ../NLPScholar/main.py $y
		done
		#touch predictions/pred$p.tsv	
		cp predictions/pred$p.tsv predictions/pred_${p}_${i}.tsv
	done
done
