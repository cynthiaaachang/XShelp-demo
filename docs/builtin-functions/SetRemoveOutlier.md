## SetRemoveOutlier（排除離群值）

**回傳類型**: 1\
**參數數量**: 0

### 說明

排除Rank語法中的離群值商品，被排除的商品不會進入排行。
SetRemoveOutlier("zscore", value:=3) 傳入兩個參數： -
第一個參數為排除離群值的方式，有 "zscore" 和 "IQR"。 -
第二個參數為排除離群值的範圍，zscore預設為3，IQR預設為1.5，此數值需大於0。