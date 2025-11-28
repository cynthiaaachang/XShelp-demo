## GetSymbolFieldStartOffset（判斷欄位初始點）

**回傳類型**: 1\
**參數數量**: 3

### 說明

判斷欄位初始點 欄位筆數 = GetSymbolFieldStartOffset("ID", "欄位名稱")
欄位筆數 = GetSymbolFieldStartOffset("ID", "欄位名稱","頻率")
回傳目前最新一筆欄位與此欄位的第一筆資料間的欄位筆數。
如果無此欄位，或是欄位的初始點超過目前bar的位置，則回-1。
※如果不傳頻率的話，則讀取目前執行頻率的對應欄位。
※僅支援「選股」腳本類型。

### 參數

-   **商品名稱**（type: 3）
-   **欄位名稱**（type: 3）
-   **頻率**（type: 3）