import copy

import numpy as np
import pandas as pd


def six_root(df):
    dfc = df
    del dfc['Tweet']
    del dfc['brand']
    del dfc['Time']

    dfc = dfc**(1/6)
    return dfc

def print_index(df,m,n):
    """"
    This function returns the indexs of target columns of data,
    m the left index of the column range[m,n]
    n the right index of the column range[m,n]
    """
    label_need = df.keys()[m:n]
    print(label_need)
    print(df[label_need].values)
    return(df[label_need].values)


## Mehthod1 - Shannon-entropy

def normalization(data,m,n,ymin,ymax,lowest): 
    """return 0-1 normalization result,
    data refers to target array,
    ymin and ymax sets the range for all normalized values, usually
    min = 0.01, max=1, if set ymin =0.2, then all value between 0.2 and 1
    """
    data = print_index(data,m,n)
    [m,n] = data.shape
    data2=copy.deepcopy(data)
    data2=data2+(0+lowest)
    for j in range(0,n):
        d_max = max(data2[:,j])
        d_min = min(data2[:,j])
        data2[:,j] = (ymax-ymin)*(data2[:,j]-d_min)/(d_max-d_min)+ymin
    print(data2)
    print('norm_end')
    return data2

def entropy_value(data):
    """
    return entropy value for each dimension
    """
    [m,n]=data.shape
    p = copy.deepcopy(data)
    for j in range(0,n):
        p[:,j] = data[:,j]/sum(data[:,j])
    # calculate proportion value in a column for xij - x = xij/sum(xij) for any j 
    print(p)
    E = copy.deepcopy(data[0,:])
    for j in range(0,n):
        E[j] = -1/np.log(m)*sum(p[:,j]*np.log(p[:,j]))
    return(E)


def score_calculation(data,m,n,ymin,ymax,lowest):
    """
    calculate each index's weight and return final score for each observation
    """
    data1 = normalization(data,m,n,ymin,ymax,lowest)
    E = copy.deepcopy(data1[0,:])
    E = entropy_value(data1)
    print(E)
    print('E_end')
    w = (1-E)/sum(1-E) # calculate weight of each index
    print(w)
    print('w_end')
    score = np.dot(data1,w) # calculate final scoe using normalized dataset and weight
    return(score)
    

    
### method2 - CRITIC entropy method
    
def Contrast_intensity(data,m,n,ymin,ymax,lowest):
    """
    return contrast intensity of a dataset
    """
    data=normalization(data,m,n,ymin,ymax,lowest)
    [m,n]=data.shape
    std = copy.deepcopy(data[0,:])
    for j in range(0,n):
        std[j]=np.std(data[:,j])
    return(std)



def Conflict(data,m,n,ymin,ymax,lowest):
    """
    return conflict value of a dataset
    """
    data=normalization(data,m,n,ymin,ymax,lowest)
    [m,n]=data.shape

    dataframe = pd.DataFrame(data)
    dataframe = dataframe.rank()
    corre_table = dataframe.corr(method = "spearman")
    df=corre_table
    #print(df)
    #print('corre_table_end')
    df = 1 - df
    df = df.to_numpy()
    #print(df)
    #print('1-df_end')
    
    conflict = copy.deepcopy(data[0,:])
    for j in range(0,n):
        conflict[j] = sum(df[:,j])
    return(conflict)



def CRITIC(data,m,n,ymin,ymax,lowest):
    """
    Return CRITIC corss-efficiency results,
    processes include data normalization, calculating contrast intesity, and conflict
    """
    data=normalization(data,m,n,ymin,ymax,lowest)
    [m,n]=data.shape
    std = copy.deepcopy(data[0,:])
    for j in range(0,n):
        std[j]=np.std(data[:,j])
    print(std)
    print("standard deviation end")
    
    dataframe = pd.DataFrame(data)
    dataframe = dataframe.rank()
    corre_table = dataframe.corr(method = "spearman")
    df=corre_table
    #print(df)
    #print('corre_table_end')
    df = 1 - df
    df = df.to_numpy()
    #print(df)
    #print('1-df_end')
    
    conflict = copy.deepcopy(data[0,:])
    for j in range(0,n):
        conflict[j] = sum(df[:,j])
    print(conflict)
    print("total conflict equals to:")
    total_conflict=np.sum(conflict)
    print(total_conflict)
    print("conflict end")
    
    Ck = copy.deepcopy(data[0,:])
    for j in range(0,n):
        Ck[j] = std[j]*conflict[j] 
    print(Ck)
    print("information value end")
    
    wk = Ck/sum(Ck)
    print(wk)
    print("Weight end")
    
    score = np.dot(data,wk)
    return(score)










    

    
    