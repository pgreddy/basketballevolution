mkdir -p data/data_$1/temp
mkdir -p data/data_$1/final
python src/util/translate_categorization.py data/data_$1/maps_$1.csv data/raw_data/ data/data_$1/temp/ $1
python src/util/generate_features.py data/data_$1/features_$1.txt data/data_$1/temp/ data/data_$1/final/ $1