# 流程控制

在腳本撰寫的過程當中，我們可能會使用到一些比較複雜的邏輯進行運算。簡單的條列陳述沒有辦法達到這個需求，這時候我們就會需要一些流程控制的語法來幫忙。

### 條件判斷

條件判斷是最常使用的一種流程控制，會依執行的順序依序判斷，符合後即條出。XSscript提供以下三種條件判斷式：

* [If Then Else](IF%20THEN%20ELSE.md)
* [Switch Case Default](Switch%20-%20Case%20-%20Default.md)
* [Once](Once.md)

### 迴圈

另一種流程控制是迴圈，迴圈用在計算或比較需要重複執行的情況，例如計算過去10期的值，就可以利用迴圈來完成。XSscript提供以下三種條件判斷式：

* [For To (DownTo)](For%20To%20-%20DownTo.md)
* [While](While.md)
* [Repeat Until](Repeat%20-%20Until.md)

### 中斷

在執行的過程中，為了提升效率，可以控制電腦跳過某些計算不執行。就可以用中斷語法來達成。

* [Break](Break.md) : 跳出迴圈
* [Return](Return.md) : 跳出腳本
* [Ret ( `RetVal` )](retval.md)

### 多行語法

* [Begin End]

XSscript的執行是一行為單位 ( 用分號";"結尾 ) 。所以在流程控制中，通常都會搭配Begin...End使用。Begin...End可以讓我們用多行的陳述式進行運算，而非原先僅能使用單行陳述式。

### 數列關係

* [Cross Over ( `Cross Above` )](Cross%20Above%20-%20Cross%20Below.md) ：判斷是否黃金交叉
* [Cross Under ( `Cross Below` )](Cross%20Above%20-%20Cross%20Below.md) ：判斷是否死亡交叉

### 邏輯判斷

* [Not](NOT.md) ：取得相反值
* [And](AND.md) ：判斷條件是否同時成立
* [Or](OR.md) ：判斷是否有任一條件成立
* [XOR](XOR.md) ：計算差集