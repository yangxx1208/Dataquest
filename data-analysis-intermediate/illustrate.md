# 说明

[TOC]



## Getting Started With Numpy&Computation With Numpy

​	向量、矩阵的构建：

~~~python
vector = np.array([10,20,30])
matrix = np.array([[5,10,15],[20,25,30],[35,40,45]])
~~~

​	numpy读数据:

~~~python
world_alcohol = np.genfromtxt("world_alcohol.csv",delimiter = ",")
world_alcohol = np.genfromtxt("world_alcohol.csv", dtype = "U75", skip_header = 1 , delimiter = ",")#编码为U75，分隔符为“,”，去掉开头skip_header置1
~~~

# Introduction To Pandas

​	pandas读数据：

~~~python
food_info = pandas.read_csv("food_info.csv")
~~~

​	DataFrame属性：

~~~
dataframe.shape
~~~



fadskflkasdlkfjkasdkjhfdasklj

