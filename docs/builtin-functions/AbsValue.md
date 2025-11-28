# AbsValue（內建函數） — 數學函數

## 語法

> 取得絕對值，傳回無正負號的數值  
> **回傳數值 = AbsValue(數值)**

---

## 說明

`AbsValue` 函數用來計算傳入數值的絕對值。  
例如：

```pascal
Value1 = Abs(3);
Value2 = Abs(-3);
```

在上述範例中，`Value1` 與 `Value2` 的數值皆為 3。

---

## 範例

以下示範以 AbsValue 來計算兩條均線的差異。  
由於腳本不關心差異的正負，只在意差距大小，因此使用 AbsValue 取得絕對值，不需考慮正負：

```pascal
Value1 = Average(Close, 5);
Value2 = Average(Close, 10);
Value3 = AbsValue(Value1 - Value2);

If Value3 <= 0.01 * Close Then
    Ret = 1;
```
