from my_module.text_blob import SentimentAnalysis
from my_module.data_module import DataModule
import pandas as pd

test_data = ['happy', 'exciting', 'good', 'rich', 'smile', 'sad', 'disappointed', 'bad', 'poor', 'anger', 'food', 'animal']

for x in test_data:
    print(x, SentimentAnalysis.sentiment_analyzer(x))



file_path = 'sentiment-analysis-tool\my_module\Amazon_Unlocked_Mobile.csv'
product_name = 'BLU Studio 5.0 C HD Unlocked Cellphone, Black'
data_module = DataModule(file_path)
data_module.filter_by_product(product_name)
data_description = data_module.describe_data()

for key, value in data_description.items():
    print(f"{key}: {value}")
