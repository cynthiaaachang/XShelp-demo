retval

retval 是一個系統的內建函數，主要是用來顯示函數腳本執行結果。
通常用於選股中心內的自訂排行。
以下範例：外資持股比例排行的函數腳本，可以篩選出外資持股比例的前N大。

```xs
if GetField("外資持股比例") <= 0 then return;
retval = GetField("外資持股比例");

```
