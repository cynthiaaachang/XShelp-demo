# 因子_QMJ安全 – （選股欄位） <kbd>財務</kbd>

| 項目 | 說明 |
| ---- | ---- |
| 欄位名稱 | 因子_QMJ安全 |
| 欄位分類 | 財務 |
| 代碼 | `Factor_QMJ_SAFETY`<br>`因子_QMJ安全因子`<br>`Factor_QMJ_Safety Factor` |
| 格式 | 數值 |
| 支援腳本 | 選股、函數 |
| 可用頻率 | 月 |
| 支援商品 | 台股 |

## 語法
> 從六個指標(貝他因子、負債比率、股東權益報酬率的波動度、特質波動度、Altman’s Z分數、以及Ohlson's O分數)個別找出每項指標中某檔股票在整體市場的排名，將這六個排名的標準化數值平均，即為該檔股票的綜合安全評分。  

```pascal
Value1 = GetField("因子_QMJ安全", "M");
Value1 = GetField("Factor_QMJ_SAFETY", "M");
Value1 = GetField("因子_QMJ安全因子", "M");
Value1 = GetField("Factor_QMJ_Safety Factor", "M");
```

---

## 說明
從六個指標(貝他因子、負債比率、股東權益報酬率的波動度、特質波動度、Altman’s Z分數、以及Ohlson's O分數)個別找出每項指標中某檔股票在整體市場的排名，將這六個排名的標準化數值平均，即為該檔股票的綜合安全評分。
