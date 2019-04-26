#!/bin/bash

DIR=$PWD

AGGLOM_DIR=$DIR/src/algos/agglom
KMEANS_DIR=$DIR/src/algos/kmeans
MIXMOD_DIR=$DIR/src/algos/mixmod

print_algos_ops () {
	echo "Choice of algorithms:"
	echo -e "\tagglomerative"
	echo -e "\tkmeans"
	echo -e "\tmixture"
}

print_data_ops () {
	echo "Choice of data version should follow:"
	echo -e "\tv1"
	echo -e "\tv2"
	echo -e "\tv3"
	echo -e "\text..."
}

if [ $# -ne 2 ]
then
	echo "ERROR: Input should be: <algorithm> <data version>"
	echo ""
	print_algos_ops
	echo ""
	print_data_ops
	exit
fi

if [ $1 = "agglomerative" ]
then
	ALGO=$AGGLOM_DIR/agglomerative.py
elif [ $1 = "kmeans" ]
then
	ALGO=$KMEANS_DIR/kmeans.py
elif [ $1 = "mixture" ]
then
	ALGO=$MIXMOD_DIR/gaussian.py
else
	echo "ERROR: Target algorithm not supported"
	print_algos_ops
	exit
fi

DATA=$DIR/data/data_$2/final/training_data_$2_final.csv
if [ ! -f $DATA ] # Test to see if file doesn't exist
then
	echo "ERROR: data version doesn't exist or improper format"
	print_data_ops
	exit
fi

# algorithm and data is now valid
python3 $ALGO $DATA
