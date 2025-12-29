# Var

Var 語法用來宣告變數，並且給定變數的預設值。

系統會根據 Var 語法內給定的預設值的型態來決定變數的類型。目前系統提供以下三種變數類型:

  * 數值，例如 10, 5.3,
  * 字串, 例如 "String"，
  * 邏輯值, 例如 True, False

語法如下:

```xs
Var: SumValue(0);
Var: StrValue("");
Var: Flag(True);
```

在上述的範例內宣告了三個變數:

  * SumValue 是一個數值變數，初始值為0，
  * StrValue 是一個字串變數，初始值為"" (空白字串)，
  * Flag 是一個邏輯變數，初始值為True

多個變數也可以在同一行內宣告，例如可以把上述範例寫成:

```xs
Var: SumValue(0), StrValue(""), Flag(True);
```

除了 Var 語法之外，也可以使用 Vars 語法，Variable 語法，或是 Variables 語法來宣告變數，範例如下：
```xs
Vars: SumValue(0);
Variable: StrValue("");
Variables: Flag(True);
```
