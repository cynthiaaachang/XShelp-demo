# Gamma – （報價欄位） <kbd>期權</kbd>

| 項目 | 說明 |
| ---- | ---- |
| 欄位名稱 | Gamma |
| 欄位分類 | 期權 |
| 代碼 | `Gamma`<br>`q_Gamma` |
| 單位 | 值 |
| 格式 | 數值 |
| 支援腳本 | 警示、交易、函數 |
| 支援商品 | 台(權證)、選擇權 |

## 語法
> 選擇權／權證商品的Gamma值，用來衡量標的商品價格變動幅度對商品Delta的影響。  

```pascal
Value1 = GetQuote("Gamma");
Value1 = GetQuote("Gamma");
Value1 = q_Gamma
```

---

## 說明
選擇權／權證商品的Gamma值，用來衡量標的商品價格變動幅度對商品Delta的影響。

公式是，當標的商品價格變動Y元，選擇權(或權證)的Delta值將變動Gamma＊Y。

例如，台指選擇權履約價16500的買權，其Delta值為0.5，Gamma值為0.0008，表示當加權指數上漲100點時，此買權的Delta會增加0.08。

Gamma計算式，請參考Black & Scholes模型。
