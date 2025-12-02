# RightStr – （內建函數） <kbd>字串函數</kbd>

## 語法

> **回傳字串的右邊子字串**  
> **子字串 = RightStr(原始字串，字元長度)**  

---

## 說明

這個函數傳入兩個參數：

- 第一個參數是原始字串
- 第二個參數是欲取出的字元個數

回傳值是從原始字串右邊開始長度為第二個參數的子字串。

```pascal
Var: str1("");

str1 = RightStr("abcdefg", 3);  // str1 = "efg"
```

在上面範例內，str1是"abcdefg"從右邊算起長度為3的子字串，"efg"。

請參考 [LeftStr函數](api.aspx?a=leftstr&b=bif) 以及 [MidStr函數](api.aspx?a=midstr&b=bif)。
