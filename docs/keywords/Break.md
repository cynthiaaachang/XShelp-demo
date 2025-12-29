Break

Break 指令的用處是控制迴圈執行時跳出迴圈的時機點，一般是用在For 迴圈或是While 迴圈內。

以下是 For 迴圈的範例:

```xs
i = 0;
For i = 0 to 10
Begin
    If Close[i] < 20 Then Break;
End;

```

一般而言上面的迴圈會執行11次(從I = 0 到 10)。可是在執行過程內，如果某一期的Close欄位值比20小的話，就會馬上跳出 For 迴圈。
