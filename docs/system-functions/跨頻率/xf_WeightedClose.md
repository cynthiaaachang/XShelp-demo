# xf_WeightedClose – （系統函數） <kbd>跨頻率</kbd>

## 語法
> 計算指定頻率的加權平均收盤價。  
> **回傳數值=xf_WeightedClose(頻率)**  
> 傳入一個參數:  
> - 第一個參數是頻率，指定傳入數列的資料期別，支援"D", "W", "M", "AD", "AW", "AM"。  

---

## 說明
xf_WeightedClose是[WeightedClose](api.aspx?a=WeightedClose&b=sys) 函數的跨頻率版本，增加了指定頻率的參數，可以計算指定頻率的WeightedClose值。

範例：

```pascal
plot1(xf_WeightedClose("W"));    //繪製週線加權平均收盤價的連線
```
