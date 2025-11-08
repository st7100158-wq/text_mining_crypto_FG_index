import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# === 繪製折線圖 ===
emotion_index = pd.read_csv("emotion_index_normalized.csv", parse_dates=['date'], index_col='date')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# 對每個子圖分別設置x軸格式
for ax in [ax1, ax2]:
    ax.xaxis.set_major_locator(mdates.MonthLocator())        # 主刻度：每個月
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # 格式化顯示「年-月'

# 圖1: 恐懼 vs 貪婪指數
ax1.plot(emotion_index.index, emotion_index['Fear_Index'], label='Fear Index', linewidth=2.5, color='#FF6B6B')
ax1.plot(emotion_index.index, emotion_index['Greed_Index'], label='Greed Index', linewidth=2.5, color='#51CF66')
ax1.set_title("Ethereum: Normalized Fear vs Greed Index", fontsize=14, fontweight='bold')
ax1.set_ylabel("Normalized Index (0-100)", fontsize=12)
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.4)

# 圖2: 使用更簡單但可靠的填充方法
x_data = emotion_index.index
y_data = emotion_index['Greed_Fear_Normalized']
neutral_line = 50

# 直接使用 fill_between，但添加邊界點
# 在數據開始和結束處添加中性點以確保完整填充
extended_dates = pd.DatetimeIndex([x_data[0] - pd.Timedelta(days=1)]).append(x_data).append(
    pd.DatetimeIndex([x_data[-1] + pd.Timedelta(days=1)]))
extended_scores = pd.Series([neutral_line] + list(y_data) + [neutral_line])

# 繪製填充區域
ax2.fill_between(extended_dates, extended_scores, neutral_line, 
                where=(extended_scores >= neutral_line), 
                alpha=0.3, color='green', label='Greed Zone', interpolate=True)
ax2.fill_between(extended_dates, extended_scores, neutral_line, 
                where=(extended_scores <= neutral_line), 
                alpha=0.3, color='red', label='Fear Zone', interpolate=True)

# 繪製線條
ax2.plot(x_data, y_data, label='Greed-Fear Score', linewidth=3, color='#3B82F6')
ax2.axhline(y=neutral_line, color='gray', linestyle='--', alpha=0.7, label='Neutral (50)')

ax2.set_title("Ethereum: Greed-Fear Composite Score", fontsize=14, fontweight='bold')
ax2.set_xlabel("Date", fontsize=12)
ax2.set_ylabel("Score (0-100)", fontsize=12)
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()