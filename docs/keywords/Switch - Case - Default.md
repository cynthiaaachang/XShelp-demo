Switch / Case / Default

Switch 語法是用來判斷某個變數的值是否符合某些運算式，同時定義符合時的執行指令。

語法如下：

```xs
Switch (變數)
Begin
  Case 運算式1:
     符合運算式1時所執行的指定;
  Case 運算式2:
     符合運算式2時所執行的指定;
  Default:
     都不符合時所執行的指令;
End;

```

在 Switch 語法內必須傳入一個變數，同時使用 Case 語法定義各種不同的運算式，以及當這個運算式符合時要執行的指令。同時也可以使用 Default 語法來定義當所有的Case都不符合時所需要執行的指令。

以下是一個範例:

```xs
Value1 =DayOfMonth(date);
Switch (value1)
Begin
  Case 1:   // value1=1時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日")
        ,"value1=1時執行這段程式碼");

  Case 2:   // value1=2時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=2時執行這段程式碼");
  Case 3:   // value1=3時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=3時執行這段程式碼");

  Case 4:   // value1=4時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=4時執行這段程式碼");

  Case 5:   // value1=5時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=5時執行這段程式碼");
  Case 6 to 20: // value1= 6 ~ 20 時執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "value1=6~20時執行這段程式碼");

  Default:  // 其他情形都執行這段程式碼
        print(Text("今天的日期是",numtoStr(date,0),
        "。是",numtoStr(DayOfMonth(date),0),"日"),
        "其他情形都執行這段程式碼");
End;

```

在上述範例內這個變數為 Value1，然後使用 Case 語法一一檢查 Value1 是否為1，2，3，4，5，6 20同時也使用 Default 語法定義當 Value1 不是1，2，3，4，5，6 20時所需要執行的指令。

由於DayOfMonth這個函數會計算出今天為幾日(如果是01日的話則回1，02日則回2，03日則回3)，所以以上的範例：
  * 在 01 日會印出「今天的日期是19941101。是1日 value1=1時執行這段程式碼」
  * 在 02 日會印出「今天的日期是19941102。是2日 value1=2時執行這段程式碼」
  * 在 03 日會印出「今天的日期是19941103。是3日 value1=3時執行這段程式碼」
  * 在 04 日會印出「今天的日期是19941104。是4日 value1=4時執行這段程式碼」
  * 在 05 日會印出「今天的日期是19941105。是5日 value1=5時執行這段程式碼」
  * 在 06 ~ 20 日會印出「今天的日期是19941107。是7日 value1=6~20時執行這段程式碼 」
  * 在 21 ~ 月底會印出「今天的日期是19941121。是21日 其他情形都執行這段程式碼 」
