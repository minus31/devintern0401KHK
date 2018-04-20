import pandas as pd 
import datetime
import numpy as np

def func1(df1, df2):
    
    """
    이 함수는 "time"과 "value" 가 들어 있는 pandas 데이터 프레임 두개를 인수로 받고, 
    이 두 데이터 프레임을 합치고, "time" 을 기준으로 정렬하는 함수 입니다. 
    
    parameter :: 
    
    df1 : pandas.DataFrame, "time" 과 "value"라는 필드를 포함 하고 있어야 합니다. 
    df2 : pandas.DataFrame, "time" 과 "value"라는 필드를 포함 하고 있어야 합니다. 
    
    return :: 
    
    result : 합쳐지고, 시간 순으로 정렬된 데이터프레임

    """
    
    result = pd.concat([df1, df2], axis=0)
    result = result.sort_values(["time"], ascending=[True])
    result = result.reset_index(drop=True)
    
    return result 



# time sampling for test 
def time_sampling(n=100, f=True):
    
    """

    func 1의 테스트용 데이터 프레임 생성 
    
    paragmeter::
    
    n : 생성하고 싶은 샘플 개수, defalut=100
    f : 지금 샘플링을 첫번째로 하는 것인지 boolean 형식으로 표현, defalut=True
    
    return :: 
    
    samples : 날짜 데이터 샘플 (각 날짜의 자료형은 "datetime.datetime")
    
    """
    
    if f != True:
        now = datetime.datetime.now() + datetime.timedelta(minutes=5)
    else: 
        now = datetime.datetime.now()
    dates = pd.date_range(start=now, freq="H", periods=n)
    dates = pd.Series(dates)
    
    samples = pd.concat([dates, pd.Series(np.zeros(n))], axis=1)
    samples.columns = ['time', 'value']
    
    return samples
    
    