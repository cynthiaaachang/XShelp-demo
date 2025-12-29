Cross Above / Cross Below

Cross 相關的語法共有兩種：

  * Cross Above 或是 Cross Over 是用來檢查目前的欄位數值是否 向上穿越 某個欄位的前期數值。
  * Cross Below 或是 Cross Under 則是用來檢查目前的欄位數值是否 向下跌破 某個欄位的前期數值。

以下是 向上穿越 均線的寫法：

```xs
If Close Cross Above Average(Close, 5) Then ret = 1;

```

當這一期的Close欄位大於等於近5期的平均值(Average(Close,5))且前一期的Close欄位小於前一期的近5期的平均值的話，則ret會被設定成1。

以下則是 向下跌破均線 的寫法：

```xs
If Close Cross Below Average(Close, 5) Then ret = 1;

```

如果這一期的Close欄位小於等於近5期的平均值(Average(Close,5))且前一期的Close欄位大於前一期的近5期的平均值的話，則ret會被設定成1。

Cross 也可以寫成 Crosses。
