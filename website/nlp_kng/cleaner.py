import pandas as pd
import re
import nltk
nltk.download('punkt')

from nltk import tokenize
from . import config

@config.timer
def clean_data(text):
    text_df = pd.DataFrame(columns =['sentences'])
    for line in text.splitlines():
        if(len(line) > 2):
                sentence = re.sub('[^A-Za-z0-9.,\-\'|!$% ]+ ', '', line.strip())
                if len(sentence) > 1 and sentence[-1] not in ['?','.']:
                    sentence = str(sentence)+'.'
                if len(sentence.split(' ')) > 2:
                    text_df.loc[len(text_df.index)] = [sentence]
        text_df.sentences = text_df.sentences.drop_duplicates()
        text_df = text_df[text_df.sentences.str.len() > 2]
        text_df = text_df.reset_index(inplace = False,drop=True)
    new_df = pd.DataFrame(columns = ['sentences'])
    for sentences in text_df.sentences:
        sentence_list = tokenize.sent_tokenize(sentences)
        for sentence in sentence_list:
            new_df.loc[len(new_df)] = [sentence]
    new_df.sentences = new_df.sentences.drop_duplicates()
    new_df = new_df[new_df.sentences.str.len() > 2]
    new_df = new_df.reset_index(inplace = False,drop=True)
    clean_text = ''
    for index, row in new_df.iterrows():
        clean_text = clean_text + row.sentences+'\n'
    return new_df, clean_text

# if __name__ == "__main__":
#     ## Reading data
#     text_df = pd.DataFrame(columns =['sentences'])
#     with open(f'{RAW_TEXT_FILE_NAME}','r') as file:
#         lines = file.readlines()
#         file.close()
#         for line in lines:
#             if(len(line) > 2):
#                 sentence = re.sub('[^A-Za-z0-9.,\-\'|!$% ]+ ', '', line.strip())
#                 if len(sentence) > 1 and sentence[-1] not in ['?','.']:
#                     sentence = str(sentence)+'.'
#                 if len(sentence.split(' ')) > 2:
#                     text_df.loc[len(text_df.index)] = [sentence]
#         text_df.sentences = text_df.sentences.drop_duplicates()
#         text_df = text_df[text_df.sentences.str.len() > 2]
#         text_df = text_df.reset_index(inplace = False,drop=True)
    
#     new_df = pd.DataFrame(columns = ['sentences'])

#     for sentences in text_df.sentences:
#         sentence_list = tokenize.sent_tokenize(sentences)
#         for sentence in sentence_list:
#             new_df.loc[len(new_df)] = [sentence]
#     new_df.sentences = new_df.sentences.drop_duplicates()
#     new_df = new_df[new_df.sentences.str.len() > 2]
#     new_df = new_df.reset_index(inplace = False,drop=True)
        
#     with open(f'{DATA_TEXT_FILE_NAME}','w') as file:
#         for sentence in new_df.sentences:
#             file.write(sentence)
#             file.write('\n')
#         file.close()

#     del new_df
#     del file
#     del line
#     del lines
#     del sentence
#     del text_df
#     del sentence_list
#     del sentences