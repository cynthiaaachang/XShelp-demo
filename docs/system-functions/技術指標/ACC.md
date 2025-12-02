# ACC – （系統函數） <kbd>技術指標</kbd>

## 語法

> ACC加速量指標(Acceleration)。用來觀察行情價格變化的加速度幅度。  
> **回傳數值=ACC(期數)**  

---

## 說明

ACC是將MTM運動量指標再做一次動量運算的指標。

範例：
```pascal
value1 = ACC(10);       //計算收盤價10期的加速量指標
plot1(value1, "ACC");   
```
