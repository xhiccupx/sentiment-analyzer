import preprocessor as p
import numpy as np
import pandas as pd
import emoji
import plotly.express as px
import tensorflow as tf
from transformers import AlbertTokenizerFast, TFAutoModel
albert = tf.keras.models.load_model(r"C:\Users\smdar\Downloads\multiclass\albert_model")
tokenizer = AlbertTokenizerFast.from_pretrained(r"C:\Users\smdar\Downloads\multiclass\tokenizer")

sent_to_id  = {"empty":0, "sadness":1,"enthusiasm":2,"neutral":3,"worry":4,
               "surprise":5,"love":6,"fun":7,"hate":8,"happiness":9,"boredom":10,"relief":11,"anger":12}

# path_to_spellFile should have path to aspell.txt
path_to_spellFile = "aspell.txt"
# path_to_ContractionsFile should have path to contractions.csv
path_to_contractions = "contractions.csv"

def setupMispeller():
  misspell_data = pd.read_csv(path_to_spellFile,sep=":",names=["correction","misspell"])
  misspell_data.misspell = misspell_data.misspell.str.strip()
  misspell_data.misspell = misspell_data.misspell.str.split(" ")
  misspell_data = misspell_data.explode("misspell").reset_index(drop=True)
  misspell_data.drop_duplicates("misspell",inplace=True)
  miss_corr = dict(zip(misspell_data.misspell, misspell_data.correction))

  return miss_corr

def setupContractions():
  contractions = pd.read_csv(path_to_contractions)
  cont_dic = dict(zip(contractions.Contraction, contractions.Meaning))

  return cont_dic

def misspelled_correction(val, miss_corr):
  for x in val.split(): 
    if x in miss_corr.keys(): 
      val = val.replace(x, miss_corr[x]) 
  return val

def cont_to_meaning(val, cont_dic): 
  for x in val.split(): 
    if x in cont_dic.keys(): 
      val = val.replace(x, cont_dic[x]) 
  return val

def punctuation(val): 
  punctuations = '''()-[]{};:'"\,<>./@#$%^&_~'''
  for x in val.lower(): 
    if x in punctuations: 
      val = val.replace(x, " ") 
  return val

def clean_text(val, miss_corr, cont_dic):
  val = misspelled_correction(val, miss_corr)
  val = cont_to_meaning(val, cont_dic)
  val = p.clean(val)
  val = ' '.join(punctuation(emoji.demojize(val)).split())
  
  return val

def regular_encode(texts, tokenizer, maxlen=512):
  enc_di = tokenizer.batch_encode_plus(
      texts, 
      return_attention_mask=False, 
      return_token_type_ids=False,
      padding='max_length',
      max_length=maxlen,
      truncation=True
  )
    
  return np.array(enc_di['input_ids'])

def getSentiment(model, tokenizer, text):
  #tokenize input text
  x_test1 = regular_encode([text], tokenizer, maxlen=160)
  test1 = (tf.data.Dataset.from_tensor_slices(x_test1).batch(1))
  #test1
  sentiment = model.predict(test1,verbose = 0)
  sent = np.round(np.dot(sentiment,100).tolist(),0)[0]
  result = pd.DataFrame([sent_to_id.keys(),sent]).T
  result.columns = ["sentiment","percentage"]
  return result

# def plot_result(df):
#   colors={'love':'rgb(213,0,0)','empty':'rgb(0,0,0)',
#           'sadness':'rgb(0,142,248)','enthusiasm':'rgb(245,178,123)',
#           'neutral':'rgb(237,236,236)','worry':'rgb(216,74,9)',
#           'surprise':'rgb(1,155,189)','fun':'rgb(255,208,0)',
#           'hate':'rgb(120,0,160)','happiness':'rgb(9,143,69)',
#           'boredom':'rgb(128,124,124)','relief':'rgb(133,221,233)',
#           'anger':'rgb(245,94,16)'}
#   col_2={}
#   for i in result.sentiment.to_list():
#     col_2[i]=colors[i]
#   fig = px.pie(df, values='percentage', names='sentiment',color='sentiment',color_discrete_map=col_2,hole=0.3)
#   fig.show()

def plotsenti (inp):
  # Sentence input

  miss_corr = setupMispeller()
  cont_dic = setupContractions()
  p.set_options(p.OPT.MENTION, p.OPT.URL)
  
  val = clean_text(inp, miss_corr, cont_dic)

  

  result = getSentiment(albert, tokenizer, val)
  return result
#  plot_result(result)
#print(plotsenti("This is a Bad Day"))