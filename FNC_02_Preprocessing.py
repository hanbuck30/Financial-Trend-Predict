import numpy as np
import scipy.io
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from pathlib import Path
from FNC_Func_PST  import FNC_Func_PST

def FNC_02_Preprocessing(data):
    # 데이터 로딩
    #data_path = Path("../../DATA/FNC/") / f"{Type}.mat"
    #data = scipy.io.loadmat(data_path)
    DATA = data#[Type]

    # KOSPI KOSDAQ는 시가총액, 나머지는 종가를 기준으로 가격 값을 일정 범위로 스케일링
    # KOSPI KOSDAQ 경우 증자 감자가 때문에 가격이 급격하게 변할 수 있으므로 시가총액을 기준으로 함.
    for i, data in enumerate(DATA):
        scaler = StandardScaler()
        data['A1'] = scaler.fit_transform(data['Marketcap'])

        scaler = MinMaxScaler(feature_range=(0, 1))
        data['A2'] = scaler.fit_transform(data['Marketcap'])

        scaler = MinMaxScaler(feature_range=(-1, 1))
        data['A3'] = scaler.fit_transform(data['Marketcap'])

        print(f"{Type} Scaling: {i+1} / {len(DATA)} - {data['codeName']} Done.")

    # 주가의 Target으로 사용할 Price_Series_Transform
    # 지그재그형 주가를 T, P를 기준으로 smooting

    # PST 파라매터 설정
    T=5  # time interval
    P=0.05  # percentage

    # PST
    for j, data in enumerate(DATA):
        # nPST=0 means there is no BUY and SELL point by PST
        if data['A2'].size == 0 or len(data['A2']) <= 10:
            # too short time series to calculate pst
            data['PST'] = []
            data['nPST'] = 0
        else:
            data['PST'], data['nPST'] = FNC_Func_PST(T, P, data['A2'])

        print(f"{Type} PST: {j+1} / {len(DATA)} - {data['codeName']} Done.")

    # Save
    save_path = data_path.parent / f"{Type}_{str(DATA[0]['Date'][-1])}.mat"
    scipy.io.savemat(save_path, {Type: DATA})
    scipy.io.savemat(data_path, {Type: DATA})

    print('FNC_02_Preprocessing Done.')
