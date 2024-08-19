import pytest
import pandas as pd
def test_checkDuplicates():
    target_df = pd.read_csv("target.csv", sep=",")
    count = target_df.duplicated().sum()
    assert count == 0 , "Duplication found - please verify the target"

def test_DataCompletenss():
    target_df = pd.read_csv('target.csv')
    assert not target_df.empty,"Target file is empty- please verify the ETL process"

def test_deptNoForNullValueCheck():
    target_df = pd.read_csv('target.csv')
    isDeptNoNUll = target_df['deptno'].isnull().any()
    assert isDeptNoNUll == True ,"deptno is having a null value - Please check"

def test_deptNoForUniqueValueCheck():
    target_df = pd.read_csv('target.csv')
    totalcount = target_df['eno'].count()
    deptNoUniqueValueCount = len(target_df['eno'].unique())
    assert totalcount == deptNoUniqueValueCount ,"eno column values are not unique - please check"