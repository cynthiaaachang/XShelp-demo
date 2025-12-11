# CloseY – （系統函數） <kbd>價格取得</kbd>

## 語法
> 取得年線的收盤價。  
> 僅限使用於年線以下之頻率。  
> **回傳數值=CloseY(期別)**  
> 傳入一個參數:  
> - 第一個參數是期別，和序列引用定義相同，0表當期、1表前一期...依此類推。  

---

## 說明
當使用頻率小於年線時，用CloseY可以找到某期的年收盤價。

範例：

```pascal
plot1(CloseY(0)); //繪製當年收盤價的連線
plot2(CloseY(1)); //繪製前一年收盤價的連線
```

相關的函數包含:
- [OpenD](api.aspx?a=opend&b=sys), [OpenW](api.aspx?a=openw&b=sys), [OpenM](api.aspx?a=openm&b=sys), [OpenQ](api.aspx?a=openq&b=sys), [OpenH](api.aspx?a=openh&b=sys), [OpenY](api.aspx?a=openy&b=sys)
- [HighD](api.aspx?a=highd&b=sys), [HighW](api.aspx?a=highw&b=sys), [HighM](api.aspx?a=highm&b=sys), [HighQ](api.aspx?a=highq&b=sys), [HighH](api.aspx?a=highh&b=sys), [HighY](api.aspx?a-highy&b=sys)
- [LowD](api.aspx?a=lowd&b=sys), [LowW](api.aspx?a=loww&b=sys), [LowM](api.aspx?a=lowm&b=sys), [LowQ](api.aspx?a=lowq&b=sys), [LowH](api.aspx?a=lowh&b=sys), [LowY](api.aspx?a=lowy&b=sys)
- [CloseD](api.aspx?a=closed&b=sys), [CloseW](api.aspx?a=closew&b=sys), [CloseM](api.aspx?a=closem&b=sys), [CloseQ](api.aspx?a=closeq&b=sys), [CloseH](api.aspx?a=closeh&b=sys), [CloseY](api.aspx?a=closey&b=sys)
