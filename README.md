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
    ```
    輸入範例            輸出範例
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
    0 0
    ```
## 0-1 Knapsack
* n 項物品，每項物品各有不同價值及不同重量
* 目的是帶走總價值最高的物品，但背包 (Knapsack) 有重量的限制
* 試設計程式解決 0-1 背包問題 (即每項物品僅能帶走或不帶走，無法帶走部分)
* 須求得最佳解 (Optimal Solution)
#### 輸入
* 輸入物品 Knapsack 重量 W 與物品總數 n
* 接著分別是各項物品的重量與價值 (均為正整數，中間以空格隔開)。
#### 輸出
* 求出可能的最高總價值
* 列出帶走物件的編號
  
#### 輸入與輸出範例
 ```
    輸入範例            輸出範例
    50                 Total Value = 220
    3                  Take Items 2, 3
    10 60
    20 100
    30 120
 ```

## Texture Stitching
* 若使用動態規劃法 (Dynamic Programming)
* 設定影像重疊比例，則進行兩張數位影像的上下 (水平) 方向拼貼
* 設定重疊比例介於 20% ~ 30%之間
* 將重疊區域視為一個網路，網路架構如同演算法中介紹的組裝線排程(Assembly-Line Scheduling) 問題
* 每個像素 (節點) 根據 R、G、B 值的歐氏距離計算用來評估重疊區域像素間的相似度
* 參考 Assembly-Line Scheduling 的演算法，求得的最短路徑，即是理想的「接縫」(Seam)
#### 輸入
* 採讀檔方式進行，並輸入相關參數
* 原則上，輸入的紋理影像大小為 256 X 256 像素
#### 輸出
* 輸出拚貼好的結果影像檔
  
#### 輸入與輸出範例
 ```
    輸入範例                                    輸出範例
    請輸入影像檔：Texture_Rock.bmp [Enter]      輸出影像檔 Texture_Rock_result.bmp
    請輸入拼貼方向 (1)水平、(2)垂直：2 [Enter]   【註】原圖檔案名稱_result.bmp。
    請輸入重疊比例 (%)：20 [Enter]
 ```
