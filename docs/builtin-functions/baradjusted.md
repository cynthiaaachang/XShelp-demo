# BarAdjusted（內建函數）

此函數用於判斷目前的執行頻率是否為還原頻率。

---

## 📘 語法（Syntax）

回傳執行腳本資料頻率是否為還原頻率。

- 若為還原頻率，則回傳 **True**
- 若不是還原頻率，則回傳 **False**

---

## 📄 說明（Description）

運用此函數可判斷目前的執行頻率是否為「還原頻率」。

### ▶ 分鐘資料層級

- 若原資料頻率 = 還原版本的 5 分鐘  
　→ `BarInterval = 5`, `BarFreq = "Min"`, `BarAdjusted = true`

- 若原資料頻率 ≠ 還原版本 5 分鐘  
　→ `BarInterval = 5`, `BarFreq = "Min"`, `BarAdjusted = false`


### ▶ 日以上資料層級

- 若原資料是還原日線  
　→ `BarFreq = "AD"`, `BarAdjusted = true`

- 若原資料為一般日線  
　→ `BarFreq = "D"`, `BarAdjusted = false`

---

## 🧩 使用範例（Examples）

### 📌 範例 1：確認執行頻率必須是「還原日」頻率才可執行

```pascal
if BarFreq <> "D" or BarAdjusted <> True then 
    raiseRunTimeError("僅支援還原日頻率");

### 📌 範例 2：確認執行頻率必須是還原 5 分鐘線
if BarInterval <> 5 
or BarFreq <> "Min" 
or BarAdjusted <> true then 
    raiseRunTimeError("僅支援還原5分鐘線圖");

### 💡 補充說明（Notes）

此函數常用於腳本限制執行頻率，使腳本能正確處理還原資料。

常搭配 BarFreq、BarInterval 等函數一起使用。