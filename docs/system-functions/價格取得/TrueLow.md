# TrueLow – （系統函數） <kbd>價格取得</kbd>

## 語法

> 取得價格真實區間(TrueRange)的低點。  
> **回傳數值=TrueLow**  

---

## 說明

計算方法為比較當根K棒的低點與前根K棒的收盤價，取數值較小者。

範例：

```pascal
plot1(TrueLow);    //繪製當期真實區間低點的連線
plot2(TrueLow[1]); //繪製前一期真實區間低點的連線
```

請參考 [TrueHigh函數](api.aspx?a=truehigh&b=sys)以及[TrueRange函數](api.aspx?a=truerange&b=sys)。
