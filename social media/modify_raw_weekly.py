import pandas as pd

# 假設你已經有 weekly DataFrame
weekly = pd.read_csv("raw_weekly_scores.csv")  # 或 resample 後的結果

# 將 date 轉成 datetime
weekly["date"] = pd.to_datetime(weekly["date"])

# 將 date 設為 index（方便用時間插值）
weekly = weekly.set_index("date")

# 對所有需要插值的欄位做時間插值
cols_to_interpolate = [
    'finbert_score_100', 'reddit_score_100', 'cryptobert_score_100',
    'finbert_max', 'finbert_min', 'reddit_max', 'reddit_min',
    'cryptobert_max', 'cryptobert_min'
]

weekly[cols_to_interpolate] = weekly[cols_to_interpolate].interpolate(method='time')

# 如果想把 index 再變回欄位
weekly = weekly.reset_index()

# 儲存
weekly.to_csv("weekly_sentiment_scores_filled.csv", index=False)
