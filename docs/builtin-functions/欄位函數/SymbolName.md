# SymbolName – （內建函數） <kbd>欄位函數</kbd>

## 語法
> **回傳目前執行腳本的商品名稱**  
> **回傳名稱 = SymbolName**  

---

## 說明
SymbolName函數回傳目前執行腳本的商品名稱，例如 "台積電"，"鴻海"，等。

通常可以在[Print函數](api.aspx?a=print&b=sys)內使用這個函數，在列印的內容內把商品名稱印出來。

範例:

```pascal
Print("商品名稱", SymbolName);
```

請參考[Symbol函數](api.aspx?a=symbol&b=bif)。
