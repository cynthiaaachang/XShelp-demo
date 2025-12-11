# EPS預估值 – （選股欄位） <kbd>財務</kbd>

| 項目 | 說明 |
| ---- | ---- |
| 欄位名稱 | EPS預估值 |
| 欄位分類 | 財務 |
| 代碼 | `EstimateQuarterlyEPS` |
| 單位 | 美元 |
| 格式 | 數值 |
| 支援腳本 | 選股、函數 |
| 可用頻率 | 季 |
| 支援商品 | 美(股票) |

## 語法
> 市場機構對個股的季度EPS預估值。  
> 美股股票才適用本欄位。  

```pascal
Value1 = GetField("EPS預估值", "Q");
Value1 = GetField("EstimateQuarterlyEPS", "Q");
```

---

## 說明
市場機構對個股的季度EPS預估值。
美股股票才適用本欄位。

請注意：
1. 這個數值是Diluted EPS before non-recurring items, 採Non-GAAP計算. 所以有可能與財務報表內依GAAP會計原則計算的EPS會有不同。
2. 市場機構並非會對每檔股票提供EPS的預估，所以並非每檔股票都會有此欄位。

如果想要知道這一筆欄位的對應財報年度的話，請使用GetFieldFiscalY("EPS預估值")，以及GetFieldFiscalQ("EPS預估值")這兩個函數。
