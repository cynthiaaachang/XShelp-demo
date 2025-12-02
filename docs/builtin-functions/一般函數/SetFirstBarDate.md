# SetFirstBarDate – （內建函數） <kbd>一般函數</kbd>

## 語法

> 指定腳本執行時第一筆資料的日期(不支援交易腳本)  
> SetFirstBarDate(資料開始日期)  

---

## 說明

關於資料讀取範圍的定義，請參考[資料讀取範圍與腳本執行的關係](http://www.xq.com.tw/lesson/xspractice/資料讀取範圍與腳本執行的關係/)。

SetFirstBarDate 函數用於控制腳本執行時，所使用的第一個資料的日期，從而確定資料讀取的起始範圍。

語法為 SetFirstBarDate(YYYYMMDD)，其中 YYYYMMDD 是起始日期的年、月、日，且必須為合理有效的日期。

需要注意的是，SetFirstBarDate **不支援交易腳本**。  
<br />
<br />

**如果在腳本中多次使用 SetFirstBarDate 函數，並設定了不同的日期：**

   - 將會採用其中最早（最小值）的日期作為最終的資料開始日期。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若設定的日期不是合理有效的日期，該行的 SetFirstBarDate 將被視為編譯失敗。

**如果在腳本中同時存在數個 [SetTotalBar](https://xshelp.xq.com.tw/XSHelp/?HelpName=SetTotalBar&group=GENERALFUNC) 和 SetFirstBarDate，並設定了不同的數值時：**<br />

   - 系統將分別根據兩者被多次使用時的規則，決定接下來各自採用哪一個 [SetTotalBar](https://xshelp.xq.com.tw/XSHelp/?HelpName=SetTotalBar&group=GENERALFUNC) 與 SetFirstBarDate 做比較。
   - 接著採用兩者當中，最後一個成功完成編譯的函數設定。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若其中一個函數因參數無效（例如 [SetTotalBar](https://xshelp.xq.com.tw/XSHelp/?HelpName=SetTotalBar&group=GENERALFUNC) 的資料讀取筆數為負數，或 SetFirstBarDate 的日期不合理）而編譯失敗，則只有另一個成功編譯的函數設定會被採用。
