import pandas as pd

class DataModule:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def filter_by_product(self, product_name):
        self.df = self.df[self.df['product_name'] == product_name]

    def describe_data(self):
        product_name = self.df['product_name'].iloc[0]
        num_rows = len(self.df)
        num_columns = self.df.shape[1]
        review_lengths = self.df['review_text'].apply(len)
        shortest_review = review_lengths.min()
        longest_review = review_lengths.max()
        average_length = review_lengths.mean()

        return {
            'Product Name': product_name,
            'Number of Rows': num_rows,
            'Number of Columns': num_columns,
            'Shortest Review Length': shortest_review,
            'Longest Review Length': longest_review,
            'Average Review Length': average_length
        }

