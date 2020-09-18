# 依需求 只擷取檔案連結並不下載檔案
# 新增 websocket client

# 安裝
>pip install -r requirements.txt

# 執行
python3 beauty_spider2.py beauty 3 10 10000 <- 欲下載圖片數量上限
上述指令會將圖片連結以json型式儲存至urls.txt

python3 upload-img.py
上述指令將讀取前依指令所產生檔案 開啟websocket連結並將檔案內之訊息送至websocket api並將檔案內之訊息送至websocket api
