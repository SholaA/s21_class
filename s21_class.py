import numpy as np
import pandas as pd 
import matplotlib as plt
import spacy 
from scipy.stats.distributions import chi2

def remove_list_item(*, the_list, the_item):
  new_list = [item for item in the_list if item != the_item]
  return new_list

def plot_x_by_class_y(*, table, x_column, y_column):
  assert isinstance(table, pd.core.frame.DataFrame), f'table is not a dataframe but instead a {type(table)}'
  assert x_column in table.columns, f'unrecognized column: {x_column}. Check spelling and case.'
  assert y_column in table.columns, f'unrecognized column: {y_column}. Check spelling and case.'
  assert table[y_column].nunique()<=5, f'y_column must be of 5 categories or less but has {table[y_column].nunique()}'

  pd.crosstab(table[x_column], table[y_column]).plot(kind='bar', figsize=(15,8), grid=True, logy=True)
  return None

#create a gene table for proteins analyzed for positive selection. omega = overall, chi squared = Model 7 & 8 
def paml_table_one_gene(*, nm, leng, species, sp_num,PAML, omega, title, M7, M8):
  assert isinstance(nm, str), f'Expected a string value. Got {type(nm)} instead.' 
  assert isinstance(leng, int), f'Expected an integer value. Got {type(leng)} instead.'
  LR = 2*(abs(M7 - M8))
  fin = chi2.sf(LR,5)
  df = {'Name': nm, 
        'Protein Length':leng, 
        'Species':species, 
        'Max Species':sp_num ,
        'Evolving Amino Acids':[PAML], 
        '\u03C9 > 1':omega, 
        '\u03C7\u00B2 p-value': f'{fin:.5E}'} 
  pd_df = pd.DataFrame(data= df, index = np.arange(1))
  pd_df.style
  return pd_df.style.set_caption(title)

def wrangle_text(*,essay):
  ##Turning into a SpaCy item
  doc = nlp(essay)
  # word types to remove: stop,punctuation, oov, 
  # word type to keep: alpha
  # list compehension  = [for, in, if not, and not, and] 
  word = [token.text.lower() for token in doc if not token.is_stop and not token.is_oov and token.is_alpha]
  return word 
