import pandas as pd
from transformers import AutoTokenizer
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer
from util.config_util import Config
from util.path_util import Path
class Preprocessing:
    def __init__(self, model_name):
        self.config = Config()
        self.config.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.twd = TreebankWordDetokenizer()
        self.stopwords = set(stopwords.words('english'))

    def _tokenize(self):

        return
    def run(self,data_path:str ,mode='train'):
        data = pd.read_csv(data_path)







if __name__ == "__main__":
    config = Config()
    model_name = config.model_name
    train_data_path = Path().train_path
    preprocess = Preprocessing(model_name)

    train_data = preprocess.run(data_path=train_data_path,mode='train')

