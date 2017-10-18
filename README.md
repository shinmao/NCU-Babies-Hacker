# NCU-Babies-Hacker
來自中央大學的一個小型資安讀書會  
聯絡人信箱  
:sparkles: rafaelchen@protonmail.com  
:sparkles: bhgs1908@gmail.com  

## About our schedule
我們打算從pwn開始走入這條修煉之路。  
內容將取自HITCON,AIS3,bamboofox社課,甚至來自世界各地的CTF writeup。  
希望大家都能有耐心以及動力持續下去,也是我對自己的期許！  
以下將會把每次會議的進度以及共筆連結放上,有興趣歡迎參考！  

### 9/27 club course
***
教材：[HITCON pwn training 2016](https://github.com/scwuaptx/HITCON-Training)  
進度：完成LAB1~LAB6,目前內容皆為Linux Binary Exploitation  
(因為當時訓練的伺服器都已經關閉,我們將以在本地取得shell作為成功基準  
相關write-up會一同放在教材的資料夾內,講解用的ppt為keynote格式,有需要可以下載轉檔  
下堂社課會開始提供共筆:+1:  
學習內容：Buffer overflow,shellcode,ret2text技巧,stack protection的繞過,Lazy-binding的機制,ROP,stack migration技巧  

### 10/08 club course
***
教材：[Bamboofox 106年下學期 format string的部分](https://bamboofox.github.io/tutorial/2016/09/27/106-club-course.html)  
進度：檔案已經置放到github中，請將壓縮檔解壓縮即可得到題目  
今天進度主要是了解Format String的漏洞是如何產生的？  
上課期間實作了用Format String的攻擊方式*更動了Ｃ語言前面宣告的變數*以及用它*leak出canary*！:+1:    
共筆：[Format String筆記](https://paper.dropbox.com/doc/Format-String-Vulnerability-Nnjj2yR5J59RFyq081ehi)  
由於這是上課時邊趕出的筆記，格式及內容還沒有相對的完善，我們還會繼續進行補齊，*請隨時更新*！  
下次讀書會時間以及繳交進度會在trello或者telegram中公布～  

### 10/18 club course
***
分享內容：[誰在幫我們malloc](https://rafaelchen.wordpress.com/2017/10/16/heap-malloc-or-free/)
         [怎麼malloc](https://rafaelchen.wordpress.com/2017/10/17/heap-come-to-my-size/)
進度：概述wannacry流程，細部介紹加密細節
講解heap如何透過malloc和free在內存中分配空間
大致上內容有：arena的介紹，chunk的介紹，bin的介紹，最後流程圖會在做補上
備註：heap的內容真的比stack還要複雜很多:sweat_smile::sweat_smile:，回去可以搭配我上面的分享筆記閱讀，如果過程中有發現任何錯誤，歡迎留言糾正！



