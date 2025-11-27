# BarAdjusted（BarAdjusted 函數）

## 🧮 語法（Syntax）
回傳執行腳本資料頻率是否為還原頻率。回傳布林值。
若為還原頻率，則回傳「True」
若不為還原頻率，則回傳「False」

## 📘 函數說明
運用這個函數來判斷目前的執行頻率是否為還原頻率。

在執行頻率為「分鐘」的資料表達為：

如果資料頻率是還原5分鐘，則 BarInterval = 5，BarFreq = "Min"，BarBarAdjusted = true。
如果資料頻率是5分鐘，則 BarInterval = 5，BarFreq = "Min"，BarBarAdjusted = false。
在執行頻率為「日」以上頻率的資料表達為：

如果資料是還原日線, 則 BarFreq = "AD", BarAdjusted = true。
如果資料是日線, 則BarFreq = "D", BarAdjusted = false。
