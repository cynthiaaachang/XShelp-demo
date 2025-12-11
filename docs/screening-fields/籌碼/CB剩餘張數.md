# CB剩餘張數 – （選股欄位） <kbd>籌碼</kbd>

| 項目 | 說明 |
| ---- | ---- |
| 欄位名稱 | CB剩餘張數 |
| 欄位分類 | 籌碼 |
| 代碼 | `CBConversionAmount`<br>`CB餘額張數` |
| 單位 | 張 |
| 格式 | 數值 |
| 支援腳本 | 選股、函數 |
| 可用頻率 | 週、月、季、半年、年 |
| 支援商品 | 1.B |

## 語法
> 目前流通在外的CB張數（就是還沒有轉換的）季底值，每週更新。  

```pascal
Value1 = GetField("CB剩餘張數");
Value1 = GetField("CBConversionAmount");
Value1 = CB餘額張數
```

---

## 說明
目前流通在外的CB張數（就是還沒有轉換的）季底值，每週更新。
