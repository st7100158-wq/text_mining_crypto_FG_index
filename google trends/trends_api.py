import pandas as pd
import time
import random
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError
from sklearn.preprocessing import MinMaxScaler

# === 初始化 pytrends ===
pytrends = TrendReq(
    hl='en-US',
    tz=360,
    geo='US',
    retries=8,
    backoff_factor=1.0,
    timeout=(10, 60),
    requests_args={
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
    },
)

# === 安全查詢函式 ===
def safe_interest(pytrends, keywords, timeframe):
    backoff_seconds = 120
    max_backoff = 600
    while True:
        try:
            time.sleep(random.uniform(3, 8))
            pytrends.build_payload(keywords, timeframe=timeframe)
            data = pytrends.interest_over_time()
            if not data.empty:
                print(f"✅ 成功抓取: {keywords}")
                return data
        except TooManyRequestsError:
            wait_for = min(max_backoff, backoff_seconds) + random.uniform(5, 25)
            print(f"🚫 429 Too many requests. Waiting {int(wait_for)}s...")
            time.sleep(wait_for)
            backoff_seconds = min(max_backoff, backoff_seconds * 2)
        except Exception as e:
            wait_for = min(max_backoff, backoff_seconds) + random.uniform(5, 15)
            print(f"⚠️ Error: {e}, waiting {int(wait_for)}s and retrying...")
            time.sleep(wait_for)
            backoff_seconds = min(max_backoff, backoff_seconds * 2)

# === 標準化函式 ===
def normalize_keywords(data):
    """對每個關鍵字分別進行標準化 (0-100)"""
    scaler = MinMaxScaler()
    normalized_data = data.copy()
    
    for col in data.columns:
        if col != 'isPartial':
            # 將每個關鍵字的數據標準化到 0-100 範圍
            normalized_data[col] = scaler.fit_transform(data[[col]].values) * 100
    
    return normalized_data

# === 關鍵字設定 ===
fear_keywords = ["Ethereum crash","Ethereum fraud","Ethereum sell","Ethereum risk"]
greed_keywords = ["buy Ethereum","Ethereum profit","Ethereum bull run"]
fear_keywords2 = ["Ethereum fear","Ethereum scam","Ethereum bubble", "SEC ETH"]
greed_keywords2= ["Ethereum investment", "the most profitable crypto","Ethereum DeFi","Ethereum surge", "Ethereum growth"]
print("開始抓取恐懼關鍵字...")
fear_data = safe_interest(pytrends, fear_keywords, '2024-10-01 2025-10-01')

time.sleep(random.uniform(45, 90))
fear_data2 = safe_interest(pytrends, fear_keywords2, '2024-10-01 2025-10-01')

print("開始抓取貪婪關鍵字...")
time.sleep(random.uniform(45, 90))
greed_data = safe_interest(pytrends, greed_keywords, '2024-10-01 2025-10-01')
time.sleep(random.uniform(45, 90))
greed_data2 = safe_interest(pytrends, greed_keywords2, '2024-10-01 2025-10-01')
# === 資料清理與標準化 ===

fear_data = fear_data.drop(columns=['isPartial'])
fear_data2 = fear_data2.drop(columns=['isPartial'])
fear_data = pd.merge(fear_data2, fear_data, on='date', how='left')
greed_data = greed_data.drop(columns=['isPartial'])
greed_data2 = greed_data2.drop(columns=['isPartial'])
greed_data = pd.merge(greed_data2, greed_data, on='date', how='left')
print("\n=== 標準化前統計 ===")
print("恐懼關鍵字平均值:")
print(fear_data.mean().round(2))
print("\n貪婪關鍵字平均值:")
print(greed_data.mean().round(2))

# 對每個關鍵字進行標準化
fear_normalized = normalize_keywords(fear_data)
greed_normalized = normalize_keywords(greed_data)

print("\n=== 標準化後統計 ===")
print("標準化恐懼關鍵字平均值:")
print(fear_normalized.mean().round(2))
print("\n標準化貪婪關鍵字平均值:")
print(greed_normalized.mean().round(2))

# === 計算情緒指數 ===
fear_index = fear_normalized.mean(axis=1)
greed_index = greed_normalized.mean(axis=1)

emotion_index = pd.DataFrame({
    'Fear_Index': fear_index,
    'Greed_Index': greed_index,
})
emotion_index['Greed_Fear_Score'] = emotion_index['Greed_Index'] - emotion_index['Fear_Index']

# 將綜合分數也標準化到 0-100 範圍以便解讀
scaler_final = MinMaxScaler()
emotion_index['Greed_Fear_Normalized'] = scaler_final.fit_transform(
    emotion_index[['Greed_Fear_Score']].values
) * 100

# === 儲存與顯示 ===
emotion_index.to_csv('emotion_index_normalized.csv', encoding='utf-8-sig')
print("\n💾 已儲存成 emotion_index_normalized.csv")
print("\n前5天數據:")
print(emotion_index.head())
