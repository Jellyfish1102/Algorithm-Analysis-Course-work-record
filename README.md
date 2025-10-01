# Algorithm-Analysis-Course-work-record
## Connected Component Labeling
* 連通元標記的結果是對影像中每一連通元像素給予特定標籤 (Label)，依 1、2、3…等順序安排。
* 連通元標記後可決定影像中連通元的個數。標記之標籤原則上依由左而右、由上而下依序排列，且沒有跳號現象。
* 依每個連通元計算其面積 (即總像素個數)
* #### 輸入
  * 每組輸入資料代表一張二值影像，首先為影像的大小，依高 × 寬安排(最大為 100 × 100)
  * 影像大小為 0 × 0 代表結束
  * 接著為二值影像，像素值僅含 0 或 1，但影像中可能含有多個連通元。
* #### 輸出
  * 輸出包含下列資訊
    * 輸入影像編號
    * 連通元個數
    * 各連通元面積
      
* #### 輸入與輸出範例
    ```輸入範例            輸出範例
    10 10              Image #1
    0000000000         Number of Connected Components = 2
    0010001100         Connected Component #1 Area = 10
    0110010010         Connected Component #2 Area = 12
    0010000010
    0010000100         Image #2
    0010001000         Number of Connected Components = 3
    0010010000         Connected Component #1 Area = 6
    0111011110         Connected Component #2 Area = 5
    0000000000         Connected Component #3 Area = 2
    0000000000
    8 5
    00001
    00011
    00111
    00000
    11001
    11001
    10000
    00000
    0 0```
