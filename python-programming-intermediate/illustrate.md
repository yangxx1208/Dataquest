# 说明

[TOC]



## Modules&Classes



​	Intermediate Course部分是对beginner部分的提升，这里详细介绍了python模块化编程和对象。同时，也介绍了一些十分有用的库及其函数，如在第一部分对csv文件处理的csv库:

~~~python
import csv
file = open("???.csv", 'r')
data = list(csv.reader(file))
~~~

这样就可以减少对csv文件的分割操作。

## Error handing

​	*Error handing*部分主要是对dataset中缺失数据的处理，这里引入了try/except语句，这个语句对于有脏数据的数据集有很好的作用，如在类型转换中能够使一些脏数据的出现不会影响程序的执行：

~~~python
try:
    float('hello')
except Exception:
    print("Error converting to float.")
#如果输出过多，可以用pass替代print部分

#也可以直接输出错误类型
try:
    int('')
except Exception as exc:
    print (type(exc))
    print(str(exc))
~~~

## List Comprehensions

​	*List Comprehensions*介绍了数据处理中非常有用的函数如：

~~~python
#带有下表信息的enumerate()函数
ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i, item in enumerate(ships):
    print(item)
    print(cars[i])
#压缩的loop循环
apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [item*2 for item in apple_prices]
apple_prices_lowered = [item-100 for item in apple_prices]
#方便取用key、value的dic循环形式
for item_key, item_value in name_counts.items():
    if item_value == 2:
        top_female_names.append(item_key)
print(top_female_names)
    
    
~~~

## Variable Scopes

​	这一部分主要是讲*Python*变量作用域的范围，主要记住下面的要点：

- Start with the *local scope*, if any.  If the variable is defined here, it will use that value.
- Look at any *enclosing scopes*, starting with the innermost.  These are "outside" *local scopes*.  If the variable is defined in any of them, it will use the value.
- Look in the *global scope*.  If the variable is there, it uses the value.
- Look in the built-in functions. 
- Throw an error if it doesn't find the variable.

A simple way to remember this is *LEGBE*, which stands for "Local, Enclosing, Global, Built-ins, Error".

## Regular Expressions

​	*Regular Expressions*作用还是比较大的，主要介绍了re库里面的函数。主要记住一下几个符号的作用：

~~~python
#  . ：通配符
#  ^ ：起始
#  $ ：结束
#  []: 可选
#  {}: 重复
#  \ : 转译
#还有一些re库的函数用法，如下:
re.search("of Reddit",item[0]) is not None #查找
？？ = re.sub("[\(\[][Ss]erious[\]\)]","[Serious]",？？)#替换
？？ = re.findall("？？",？？)#查找全部
~~~

## Dates In Python

​	这个部分实话说，开头很吸引人，但是后面感觉没啥意思，就是python中time&datetime两个库中函数的应用。不过用起来不是特别顺手。贴上函数的Python的[Api](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

## 证书:happy::

![pic](https://github.com/yangxx1208/Dataquest/blob/master/Picture/Cer-of-Immedia.png)     





