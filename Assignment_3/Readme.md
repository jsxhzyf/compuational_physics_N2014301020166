##计算物理 第三次作业
>2014301020166 仲逸飞
## 摘要  

* 在课程主页上复习这两次课程的内容，初步掌握python和matplotlib的语法规则，为接下来的课程做好准备
* L1在屏幕上让你的英文名字水平移动起来
* L2在80*80点阵上用字符拼出你想画的东西，并让它旋转起来，希望脑洞大开！（比如字符、火柴人、火箭等等）

## 背景  
* 利用字符串阵列显示字符功能可以广泛应用于各种显示器，因而具有广泛的前景。本次作业即利用此原理显示一些目标字母或图形，从而为实现更复杂的功能打下基础。

## 正文  
L1
* We finally make it moving,but somehow a problem arises with the command"i=os.system('cls')".Here we can not clear the command in the shell and I have tried many times but it doesn't work fine on my mac.So laterly,I find another way as ''sys.stderr.write("\x1b[2J\x1b[H")'' 
* [代码此在](https://github.com/jsxhzyf/compuational_physics_N2014301020166/blob/master/Assignment_3/code.py) 

L2
* 在屏幕上用字符阵列画出自己想画出的东西，并可以让"图形"动起来。其基本原理和显示字母是类似的，将图形以"像素点"的形式储存于字符阵列即可。另外，根据老师的提示，使用指令`import os`，`i = os.system('cls')`即可清空屏幕上已经显示的"图形"，再输出另外的"帧",即可让图形动起来。再者，使用指令`import time`，`time.sleep(sometime)`即可让计算机输出每帧的间隔拉长，避免动画太快。其基本步骤是：  
    1. 制造一个空的矩形阵列，每个阵列元都是空格(此时若直接输出，得到的将是一个空阵列)；
    2. 利用一个循环，将阵列中类似正弦曲线的点位替换成字符“#”；
    3. 再通过一个循环，输出阵列的每一行即可得到一条静止的正弦曲线；
    4. 若再通过一个循环，结合清空屏幕的命令`i = os.system('cls')`和延迟命令`time.sleep(sometime)`即可输出动态的曲线。
    * [代码此在](https://github.com/jsxhzyf/compuational_physics_N2014301020166/blob/master/Assignment_3/code.py)  (运行程序时注意把python的命令窗口调大一点，不然可能显示不全)
    ![code](https://github.com/jsxhzyf/compuational_physics_N2014301020166/blob/master/Assignment_3/code.PNG) 
    * 结果如图，成功在屏幕上输出一条"正弦曲线"(至少看起来有点像)，并且，该曲线可以随着时间推移逐渐向左移动(这里只把其中一"帧"截图放了上来)。该图形模拟了一束向-x方向传输的正弦波。
    ![效果图](https://github.com/jsxhzyf/compuational_physics_N2014301020166/blob/master/Assignment_3/%E6%95%88%E6%9E%9C.PNG)  
    * 值的改进的地方：该图形的点过于分散，不够密，因为每个字符本来就有那么大，所以暂时没想到改善的方法。
    
## 结论  
本次作业实验了利用字符串阵列输出字母或简单图形的功能，但编程过程较复杂，期待利用python的画图功能进一步改善。

## 致谢 
* 感谢陈洋遥学长的指导   


