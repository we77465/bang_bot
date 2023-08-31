# bang_bot
這是一個關於我想製作bot的故事 原因是AIS3讓我的衝擊太大ㄌ 再加上看能不能混過專題
這邊只有架在本地端的部分 所以note都會丟在我的mysql上
## 你需要載的東西
* PyMySQL
* discord.py 我的版本為2.3.0 (2以上就可以了)
* asyncio
* python3
## 功能



| Column 1    | Column 2 |
|:----------- | -------- |
| !clean       |    清除      |
| !em          |    顯示我的東C      |
| !online      |    查看上線人員      |
| !ping        |    查看ping      |
| !said        |    叫機器人說東西      |
| !add_note    |    新增note      |
| !change_user |    換user      |
  !delete_note |刪除note
| !loop        |   循環查看note紀錄的時間是否要到達   |
| !set_channel |   note顯示的地方要在哪個頻道   |
| !show_note   |   顯示全部的note   |
| !unloop      |   停止循環   |
| !GPT         |   利用api接到chatGPT來達成回應   |
| !clean       |   清除先前的聊天紀錄   |

另外還有他會偵測是否為url並利用google來查看是否為惡意網址(safebrowsing.googleapis)
