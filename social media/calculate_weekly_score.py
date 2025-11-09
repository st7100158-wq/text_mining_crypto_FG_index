import pandas as pd

# 讀取原始資料
df = pd.read_csv("sentiment_with_scores_100.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

# 計算每週平均值
weekly_mean = df.resample("W-SUN", label="left")[["finbert_score_100", "reddit_score_100", "cryptobert_score_100"]].mean()
weekly_max  = df.resample("W-SUN", label="left")[["finbert_score_100", "reddit_score_100", "cryptobert_score_100"]].max()
weekly_min  = df.resample("W-SUN", label="left")[["finbert_score_100", "reddit_score_100", "cryptobert_score_100"]].min()

# 合併
weekly = weekly_mean.copy()
weekly["finbert_max"] = weekly_max["finbert_score_100"]
weekly["finbert_min"] = weekly_min["finbert_score_100"]
weekly["reddit_max"] = weekly_max["reddit_score_100"]
weekly["reddit_min"] = weekly_min["reddit_score_100"]
weekly["cryptobert_max"] = weekly_max["cryptobert_score_100"]
weekly["cryptobert_min"] = weekly_min["cryptobert_score_100"]

# 產生完整週日期範圍（週日作為週起始日）
full_week_index = pd.date_range(start="2024-09-29", end="2025-09-30", freq="W-SUN")
weekly = weekly.reindex(full_week_index)  # 這會補上缺失週，值為 NaN

# 重設 index
weekly = weekly.reset_index().rename(columns={"index": "date"})

# 儲存
weekly.to_csv("raw_weekly_scores.csv", index=False)

print("已輸出 raw_weekly_scores.csv")
