import pandas as pd
import devintern1804KHK.sub1 as s1
import datetime


def func2(df1, df2):
    
    """
    5분간격으로 data를 샘플링하여 Pandas.DataFrame 형태로 반환 한다. 
    
    parameter::
   
    df1 : pandas.DataFrame, "time" 과 "value"라는 필드를 포함 하고 있어야 합니다. 
    df2 : pandas.DataFrame, "time" 과 "value"라는 필드를 포함 하고 있어야 합니다. 
    
    return :: 
    
    records : 합쳐지고, 시간 순으로 정렬된 데이터프레임
    """

    # 데이터 프레임 합쳐서, 시간 순으로 오름 차순 정렬
    concated = s1.func1(df1, df2)
    
    #concated 프레임에서 5분 단위로 데이터를 스택하고 보여줘야함
    init_time = concated.loc[0].time
    
    # threshold = 5 minutes, 첫번째 5분 단위의 스레스홀드를 찾는다. 
    threshold = init_time - datetime.timedelta(minutes=init_time.minute % 5) + datetime.timedelta(minutes=5)
    
    # 첫번째 시간과 마지막 시간의 차, 데이터의 범위를 timedelta로 만든다.
    range_time = (concated.iloc[-1].time - init_time)
    
    # 5분단위의 record를 담을 리스트
    records = []
    
    for time in range(int(range_time.total_seconds() // 300)):
        
        record = concated[concated.time <= threshold]
        record = record.iloc[-1]
        records.append(record)
        
        # threshold  update
        threshold += datetime.timedelta(minutes=5)
    
    return pd.DataFrame(records, columns=["time", "value"])



def unit_test():
    
    """
    패키지 내의 함수(func1, func2)가 실행 되는지 확인한다. 성공적으로 실행되면, True 반환
    
    Return ::
    
    True : 성공적으로 실행된다. 
    or 
    False : 에러 발생 
    """
    
    # 이 함수가 성공적으로 실행되면, True를 출력 
    import devintern1804KHK.sub1 as s1
    import devintern1804KHK.sub2 as s2
    df1 = s1.time_sampling(n=100)
    df2 = s1.time_sampling(n=100)

    try:
        s2.func2(df1, df2)
        
    except:
        return False
    
    return True