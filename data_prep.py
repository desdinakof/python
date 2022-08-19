# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:11:36 2021

@author: desdina.kof
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import statistics

for a in range(1,3):
    """**Downloading Datasets**"""
    print("Running file index: {:02d}".format(a))
    mat = pd.read_csv("D:/AwgnTx1Rx2Scs15A1PrIx00Cf01It{:02d}.csv".format(a))
    
    """**Labeling**"""  
    
    mat.columns = ['Position', 'Label','Correlation']
    mat['Label'] = mat['Label'].map({"PrachRxCorr": 0, "PrachActive": 1}).astype(float)
    """
    d = {'Position': ['0 0 2'], 'Label': 1.0, 'Correlation': '0'}
    df2 = pd.DataFrame(data=d)
    del d
    
    mat = df2.append(df, ignore_index= True)
    del df, df2
    """
    
    """Converting String to List and Combining The Rows"""
    
    mat.iloc[:,2] = mat.iloc[:,2].apply(lambda x: [float(b) for b in x.replace(";", " ").split(" ") if b != ""])
    #mat.iloc[:,2].transform(lambda x: [float(i) for i in x.replace(";", " ").split(" ") if i != ""])
        
    print("2")
    rows = []
    for i in mat.index:
      row = mat.iloc[i]
      if row.Correlation == [1.0] or row.Correlation == [0.0]:
        mat_copy3 = []
        j = i+1
        next_row = mat.iloc[j]
        while next_row.Correlation != [1.0] and next_row.Correlation != [0.0] and j< len(mat.index):
          mat_copy3 += next_row.Correlation
          next_row = mat.iloc[j]
          j +=1
        row.Label = row.Correlation
        row.Correlation = mat_copy3
        rows.append(row)
    print("3")
    del mat, mat_copy3,  next_row, row, i, j
    
    matter = pd.DataFrame(rows)
    del rows
    
    mat_cp2 = matter.copy(deep = True)

    mat_cp2.iloc[:,2] = mat_cp2.iloc[:,2].apply(lambda x: [x.index(max(x)), max(x) ] if x else x )
    matter = mat_cp2
    del mat_cp2
    """**Deep Learning Part**"""
    print("4")
    #data separation to train and test
    #x = np.array(matter.iloc[:,2], dtype=np.float)
    #y = np.array(matter.iloc[:,1], dtype=np.float)
    
    x = pd.DataFrame(matter.iloc[:,2].tolist()[:-1])
    y = (matter.iloc[:,1].apply(lambda i: float(i[0]))).iloc[:-1]
    del matter
    #Encoding for Target Values
    print("5")
    label_encoder = LabelEncoder()
    
    y3 = pd.DataFrame((label_encoder.fit_transform(y)).tolist())
    
    del y, label_encoder
    """
    #Scaling for X values
    print("6")
    scaler = StandardScaler()
    
    df2 = scaler.fit_transform(x)
    del x
    
    df3 = pd.DataFrame(df2.tolist())
    
    del df2, scaler
    """
    scaler = StandardScaler()
    df2 = scaler.fit_transform(x)
    #x.loc('None')
    
    print("7")
    index = x[x.isnull().any(axis=1)].index
    if (len(index) > 0):
      x.drop(inplace=True, index=index)
      y3.drop(inplace=True, index=index)

    
    x.to_csv("D:/preprocessed data/x_highSNRAwgnTx1Rx2Scs15A1PrIx00Cf01It{:02d}_3max_prep.csv".format(a), index = False)
    y3.to_csv("D:/preprocessed data/y_highSNRAwgnTx1Rx2Scs15A1PrIx00Cf01It{:02d}_3max_prep.csv".format(a), index= False)
    
    del x,y3