# xf_PercentR – （系統函數） <kbd>跨頻率</kbd>

## 語法
> 計算指定頻率的威廉指標值。  
> **回傳數值=xf_PercentR(頻率,期數)**  
> 傳入二個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  
> - 第二個參數是計算威廉指標的期數。  

---

## 說明
xf_PercentR是[PercentR](api.aspx?a=PercentR&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的PercentR值。

範例：

```pascal
value1 = xf_PercentR("W", 14) - 100;       //計算週線威廉指標
Plot1(value1, "週威廉指標");
```
