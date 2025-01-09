#!/usr/bin/bash

for i in 1 2 3 4 5 6 7 8 9 10
do
	echo "Performing run $i"
	for y in train.yaml
	do
		echo "Running python ../NLPScholar/main.py $y"
		python ../NLPScholar/main.py $y
	done

	for y in eval.yaml
	do
		echo "Running python ../NLPScholar/main.py $y"
		python ../NLPScholar/main.py $y
	done
	
	cp predictions/predall.tsv predictions/pred_all_$i.tsv
done
