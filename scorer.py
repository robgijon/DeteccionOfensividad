# Author: Flor Miriam Plaza del Arco
# Year: 2021

from __future__ import print_function
import re
import os
import sys

import pandas as pd
from ast import literal_eval

import sklearn.metrics as metrics
from sklearn.metrics import mean_absolute_error
import numpy as np

def evalTask(gold_file, prediction_file):
	
  # GOLD_FILE: gold_label_test.tsv
  print("GOLD_FILE:", gold_file)
  # PREDICTION_FILE: prediction_test.tsv
  print("PREDICTION_FILE:", prediction_file)
  if not os.path.exists(gold_file):
    print("ERROR: prediction file not found")
  if not os.path.exists(prediction_file):
    print("ERROR: gold file not found")

  # Load GOLD file
  GOLD = pd.read_csv(gold_file, sep="\t")

  # Load PREDICTION file
  PREDICTION = pd.read_csv(prediction_file, sep="\t")
  if len(PREDICTION.columns) == 1:
    print('Wrong run file format')
    return False

  # Merge both dataframes by comment_id
  GOLD_PREDICTION = pd.merge(GOLD, PREDICTION, on="comment_id")
  GOLD_PREDICTION.columns = ['comment_id', 'label', 'pred']
  
  # Binary-class classification
  label2id = {'NON':0, 'OFF':1}
  GOLD_PREDICTION[1] = GOLD_PREDICTION.apply(lambda r: label2id[r['label']], axis=1)
  GOLD_PREDICTION[2] = GOLD_PREDICTION.apply(lambda r: label2id[r['pred']], axis=1)

  y_true = GOLD_PREDICTION['label'].tolist()
  y_pred = GOLD_PREDICTION['pred'].tolist()


  # Calculate metrics
  label_precision = metrics.precision_score(y_true, y_pred, labels=range(len(label2id)), average=None)
  label_recall = metrics.recall_score(y_true, y_pred, labels=range(len(label2id)), average=None)
  label_f1 = metrics.f1_score(y_true, y_pred, labels=range(len(label2id)), average=None)
  macro_precision = metrics.precision_score(y_true, y_pred, average='macro')
  macro_recall = metrics.recall_score(y_true, y_pred, average='macro')
  macro_f1 = metrics.f1_score(y_true, y_pred, average='macro')
  micro_precision = metrics.precision_score(y_true, y_pred, average='micro')
  micro_recall = metrics.recall_score(y_true, y_pred, average='micro')
  micro_f1 = metrics.f1_score(y_true, y_pred, average='micro')
  weighted_precision = metrics.precision_score(y_true, y_pred, average='weighted')
  weighted_recall = metrics.recall_score(y_true, y_pred, average='weighted')
  weighted_f1 = metrics.f1_score(y_true, y_pred, average='weighted')

  dic = {'maf': macro_f1, 'map': macro_precision, 'mar': macro_recall, 'mif': micro_f1, 'mip': micro_precision, 'mir': micro_recall, 'avgf': weighted_f1, 'avgp': weighted_precision, 'avgr': weighted_recall}
  print(dic)
  df = pd.DataFrame(dic, index=[0])
  df.to_csv('results.txt', sep='\t', index=False)

if __name__=="__main__":
	
	gold_file = sys.argv[1]
	prediction_file = sys.argv[2]
	evalTask(gold_file, prediction_file)

	
  
