from data_cleaning_and_preparation.clean import remove_unwanted_rows, remove_unwanted_columns
from data_cleaning_and_preparation.pre_process import encode_categorical_features

remove_unwanted_rows("movie_metadata.csv")
remove_unwanted_columns("clean_movie_data.csv")
print(encode_categorical_features("features.csv"))
