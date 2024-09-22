# MarkDown学习笔记  

## 这是我展示的二级标题
### 这是我展示的三级标题
这是我展示的四级标题  

---

_斜体_
__粗体__
___粗斜体___  
*斜体*
**粗体**
***粗斜体***  
***
---
* * *
~~删除线~~  
<u>下划线</u>
<b>粗体</b>

创建脚注[^RUNOOB]

---
无序列表 *+-加空格  

* 
+ 
-  
***

有序列表 数字+.   

1.
2. 
3.    
---
列表嵌套  
1. 第一项
  - 第一个元素
  + 第二个元素
2.   
---
区块引用  > 加空格  
> 第一行
> 第二行  
> 第三行   
>> 二级嵌套
>>> 三级嵌套
---
函数用``     
 `print("Hello, World!")`   
代码块用``````
```
    $(document).ready(function () {
        alert('RUNOOB');
    });
```  
---
链接：<http：//www.baidu.com>  

---


# Python学习笔记  
1. #！/user/bin/env python3  与 #!/usr/bin/python3 区别    
#!/usr/bin/python3采用了绝对路径的写法，而#!/user/bin/env python3采用了环境变量PATH的写法。  
两者是指定解释器来执行脚本；通过命令行指定解释器执行文件是不必写Shebang, 只有被直接执行的文件才有必要加入Shebang。  
2. 数字型：int、float、complex、bool  
   数据类型：number、string、list、tuple、dict、set、bool、None,number、string、tuple为不可变数据
   list[]——可变数据、tuple()——不可变数据、set{}——不可重复、dict{key:value}——键值对,key唯一
   整除：//，乘方：**  
   f-string：字符串中嵌入变量，格式化输出，f"{变量名}"
3. 注释： #、''' '''、""" """  
4. 函数的表达：  
  def 函数名（参数列表）:  
    函数体  
>Assignment01:二分查找，时间复杂度：O(logn)  
>Assignment02:归并排序，时间复杂度：O()  
>Assignment03:快速排序，时间复杂度：O(nlogn)  
>Assignment04:单源最短路径，采用BFS,时间复杂度：O(N²+E)  
---
5. 面向对象编程  
6. Python GUI编程(tkinter)  
  + >生成窗口：  
        import tkinter as tk  
        root = tk.Tk()  
        root.title('标题名')  
        root.geometry('宽x高')  
        root.mainloop()  
  + >常用控件：   
        Label(父容器, text='文本内容')  标签控件  
        Button(父容器, text='按钮文本', command=函数名)  按钮控件  
        Entry(父容器, textvariable=变量名)  输入框控件  
        Text(父容器)  文本框控件  
        Checkbutton(父容器, text='选项文本', variable=变量名)  复选框控件  
        Frame(父容器)  创建一个容器控件  
        Menu(父容器)  创建一个菜单控件  
  + >事件绑定：  
        控件.bind('<事件类型>', 函数名)  绑定事件到控件上  
        < KeyRelease >  
        < ButtonRelease-1 >  
  + >布局管理：  
        Grid(父容器)  网格布局  
        pack(父容器)  自动布局  
        place(父容器)  绝对布局  
7. Python 图像处理库PIL
> Image模块：  open、save  
8. squish游戏


---
# Git的使用 
利用git与SSH
>git init 初始化仓库  
>git add 文件名  添加文件到暂存区  
>git commit -m "提交说明"  提交到本地仓库    
>git remote rm origin  删除远程仓库  
>git remote add origin URL  远程上传仓库地址  
>git branch 分支名 创建分支  
>git checkout  分支名  切换分支  
>git push -u origin 分支名  推送到远程仓库某分支  
>git pull 从远程仓库拉取最新代码  
>git push origin --delete 分支名 删除远程分支  
>git push  -u origin 分支名  --force 强制推送到远程仓库某分支  
---
# CS231N计算机视觉
1. KNN K最近邻算法 （懒惰学习，效率低）————推荐算法
> 计算距离  
>>二层循环  
>>一层循环：利用一次numpy的广播机制  
>>无循环：展开公式，利用两次numpy的广播机制，进行矩阵乘法
2. 线性分类、损失函数与梯度下降  
+ 线性分类：  
+ 损失函数：  
>SVM分类器 ———— 最大间隔分离超平面 （中庸的思想）
>Hinge Loss 铰链损失函数 ———— 惩罚与比真实标签相差很小和错误标签  
>L2正则化
>softmax分类器(多项式逻辑回归） ———— 指数化、归一化
>交叉熵(对数似然、负对数)损失函数 ———— 衡量模型预测的不确定性，越大越不确定

+ 梯度下降：  


