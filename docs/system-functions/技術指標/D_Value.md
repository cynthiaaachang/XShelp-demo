# D_Value – （系統函數） <kbd>技術指標</kbd>

## 語法

> 計算KD指標中的D值。  
> **回傳數值=D_Value(資料期數,D值平滑期數)**  
> 傳入二個參數:  
> - 第一個參數是資料期數，指定計算的區間長度。  
> - 第二個參數是D值平滑期數，指定計算D值所用的平滑期數。  

---

## 說明

KD指標為美國交易員George Lane所創，原名為Stochastic Oscillator。 
D_Value即隨機指標中的慢速線（%D）。

範例：

```pascal
value1 = D_Value(9,3);       //計算KD指標中的D值
plot1(value1, "D");
```
