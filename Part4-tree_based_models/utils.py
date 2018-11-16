import pandas as pd
import numpy as np

from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import LabelEncoder

def prepare_hospital(fn):
    """
    Input: the filename of the hospital data set
    Output: A dataframe preprocessed as in the notebook (DAT158-Part4-3-Gradient_Boosting)
    """
    
    LOS = pd.read_csv(fn)
    
    categorical = ['rcount', 'gender', 'facid']
    
    numerical = [col for col in LOS.columns if LOS[col].dtype in ['int64', 'float64']]
    dates = ['vdate', 'discharged']
    
    transformer = make_column_transformer(
        (categorical, OrdinalEncoder()),
        remainder='passthrough')
    
    LOS_enc = transformer.fit_transform(LOS)
    
    columns = ['rcount', 'gender', 'facid'] + list(LOS.columns.drop(['rcount', 'gender', 'facid']))
    
    LOS = pd.DataFrame(data=LOS_enc, columns=columns)
    
    LOS[numerical] = LOS[numerical].astype('float32')
    
    for datecol in dates:
        LOS[datecol] = pd.to_datetime(LOS[datecol])
        
    lbl = LabelEncoder()
    for catcol in categorical:
        LOS[catcol] = lbl.fit_transform(LOS[catcol])
        
    return LOS