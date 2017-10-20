# pandas数据处理知识点整理

[TOC]



## Getting Started With Numpy&Computation With Numpy

	### 向量、矩阵的构建：

~~~python
vector = np.array([10,20,30])
matrix = np.array([[5,10,15],[20,25,30],[35,40,45]])
~~~

	### numpy数据读、选取、替换:

~~~python
world_alcohol = np.genfromtxt("world_alcohol.csv",delimiter = ",")
world_alcohol = np.genfromtxt("world_alcohol.csv", dtype = "U75", skip_header = 1 , delimiter = ",")#编码为U75，分隔符为“,”，去掉开头skip_header置1
#对于Martix中的数据，list使用
num = date[row][col];
#array使用
num = array[row,col]; row = array[:,?]
#array类型数据替换：
bool_state = (date[:,?] == "")
date[bool_state,?] = "#"
~~~

	### array数据类型转换：

~~~python
date = date.astype(float)
~~~

### array内置函数调用：

~~~python
total_date = date.sum()
average_date = date.mean()
~~~



## Introduction to Pandas&Date Manipulation with pandas

### Pandas数据格式

- Series

- DataFrame：每个column就是一个Series

  基础属性shape,index,columns,values，dtypes，describe(),head(),tail() 
  统计属性Series： count(),value_counts()，前者是统计总数，后者统计各自value的总数

  ### pandas读数据：

~~~python
date = pandas.read_csv("date.csv")
~~~

### pandas数据选取：

~~~python
#label值的选取
1. date_row/column = date.loc["label1","label2"]#label可以为list数组，如col[2,5,10],label为数字时代表row的index
2. date_row/column = date["label"]#label或者row的index
3. date_row = date.iloc[i]#i为行号

first_row_first_column = date.iloc[0,0]
all_rows_first_three_columns = date.iloc[:,0:3]
row_index_83_age = date.loc[83,"age"]
row_index_766_pclass = date.loc[766,"pclass"]
row_index_1100_age = date.loc[1100, "age"]
row_index_25_survived = date.loc[25, "survived"]
five_rows_three_cols = date.iloc[0:5,0:3]
#讲columns所有的label取出来
date.columns.tolist()#先抽出的是class类型，之后经过tolist()转化为list类型
~~~

## Working with Missing Date

### 判断空值/非空值函数

~~~python
#vector
bool_state = pd.isnull(date["label"])#非空值pd.notnull()
date_full = date[bool_state]#讲label为空值的行删除

#matrix
DataFrame.dropna(axis = 0, subset = [])#axis用于选row/column，0为row，1为column,subset为可选表示指定的labels有空值才删除，how = "all"当且仅当row/column全为控制才删除，thresh = num, 表示每行至少3个非空值才保留。

#丢弃column或row
date.drop(labels, axis = 0)
~~~

### 缺失值填充

~~~python
df.fillna(0)
df.fillna({1:0,2:0.5}) #对第一列nan值赋0，第二列赋值0.5
df.fillna(method='ffill') #在列方向上以前一个值作为值赋给NaN
~~~

### 值替换

~~~python
# 将df的A列中 -999 全部替换成空值
df['A'].replace(-999, np.nan)
#-999和1000 均替换成空值
obj.replace([-999,1000],  np.nan)
# -999替换成空值，1000替换成0
obj.replace([-999,1000],  [np.nan, 0])
# 同上，写法不同，更清晰
obj.replace({-999:np.nan, 1000:0})
~~~

### 重复值处理

~~~python
df.duplicated()#两行每列完全一样才算重复，后面重复的为True，第一个和不重复的为false，返回true
               #和false组成的Series类型
df.duplicated('key')#两行key这一列一样就算重复

df['A'].unique()# 返回唯一值的数组（类型为array）

df.drop_duplicates(['k1'])# 保留k1列中的唯一值的行，默认保留第一行
df.drop_duplicates(['k1','k2'], take_last=True)# 保留 k1和k2 组合的唯一值的行，take_last=True 保留最后一行
~~~

### 排序

+ 索引排序

  ~~~python
  # 默认axis=0，按行索引对行进行排序；ascending=True，升序排序
  df.sort_index()
  # 按列名对列进行排序，ascending=False 降序
  df.sort_index(axis=1, ascending=False) 
  ~~~


+ 值排序

  ~~~python
  # 按值对Series进行排序，使用order()，默认空值会置于尾部
  s = pd.Series([4, 6, np.nan, 2, np.nan])
  s.order()

  df.sort_values(by=['a','b'])#按列进行排序
  ~~~


+ 排名

  ~~~python
  a=Series([7,-5,7,4,2,0,4])
  a.rank()#默认method='average'，升序排名（ascending=True），按行（axis=0）
  #average 值相等时，取排名的平均值
  #min 值相等时，取排名最小值
  #max 值相等时，取排名最大值
  #first值相等时，按原始数据出现顺序排名
  ~~~

### 索引设置

- reindex() 
   更新index或者columns， 
   默认：更新index，返回一个新的DataFrame

  ~~~python
  # 返回一个新的DataFrame，更新index，原来的index会被替代消失
  # 如果dataframe中某个索引值不存在，会自动补上NaN，不在reindex中出现的rows会删除
  df2 = df1.reindex(['a','b','c','d','e'])

  # fill_valuse为原先不存在的索引补上默认值，不在是NaN
  df2 = df1.reindex(['a','b','c','d','e'],  fill_value=0)

  # inplace=Ture，在DataFrame上修改数据，而不是返回一个新的DataFrame
  df1.reindex(['a','b','c','d','e'],  inplace=Ture)

  # reindex不仅可以修改 索引(行)，也可以修改列
  states = ["Texas","Utah","California"]
  df2 = df1.reindex( columns=states )
  ~~~


- set_index() 
   将DataFrame中的列columns设置成索引index 
   打造层次化索引的方法

  ~~~python
  # 将columns中的其中两列：race和sex的值设置索引，race为一级，sex为二级
  # inplace=True 在原数据集上修改的
  adult.set_index(['race','sex'], inplace = True) 

  # 默认情况下，设置成索引的列会从DataFrame中移除
  # drop=False将其保留下来
  adult.set_index(['race','sex'], inplace = True) 
  ~~~

- reset_index() 
   将使用set_index()打造的层次化逆向操作 
   既是取消层次化索引，将索引变回列，并补上最常规的数字索引

  ~~~python
  df.reset_index()#参数drop为true时舍弃原索引，否则将原索引生产一列插入数据中
  ~~~

  ​

### 数据透视表

~~~python
pivot_tabel = date.pivot_table(index="label1", values="label2",aggfunc=numpy.sum)
~~~

### 数据选取

- [] 
   只能对行进 行（row/index） 切片，前闭后开df[0:3]，df[:4]，df[4:]
- where 布尔查找 

```python
 df[df["A"]>7]1
```

- isin

```python
# 返回布尔值
s.isin([1,2,3])
df['A'].isin([1,2,3])
df.loc[df['A'].isin([5.8,5.1])]选取列A中值为5.8，5.1的所有行组成dataframe1234
```

- query 
   多个where整合切片，&：于，|：或　

```python
 df.query(" A>5.0 & (B>3.5 | C<1.0) ")　1
```

- loc ：根据名称Label切片

```python
# df.loc[A,B] A是行范围，B是列范围
df.loc[1:4,['petal_length','petal_width']]

# 需求1：创建一个新的变量 test
# 如果sepal_length > 3 test = 1 否则 test = 0
df.loc[df['sepal_length'] > 6, 'test'] = 1
df.loc[df['sepal_length'] <=6, 'test'] = 0

# 需求2：创建一个新变量test2 
# 1.petal_length>2 and petal_width>0.3 = 1 
# 2.sepeal_length>6 and sepal_width>3 = 2 3.其他 = 0
df['test2'] = 0
df.loc[(df['petal_length']>2)&(df['petal_width']>0.3), 'test2'] = 1
df.loc[(df['sepal_length']>6)&(df['sepal_width']>3), 'test2'] = 21234567891011121314
```

- iloc：切位置

```python
df.iloc[1:4,:]1
```

- ix：混切 
   名称和位置混切，但效率低，少用

```python
df1.ix[0:3,['sepal_length','petal_width']]1
```

- map与lambda

```python
alist = [1,2,3,4]
map(lambda s : s+1, alist)#map就是将自定义函数应用于Series每个元素

df['sepal_length'].map(lambda s:s*2+1)[0:3]1234
```

- apply和applymap 
   apply和applymap是对dataframe的操作，前者操作一行或者一列，后者操作每个元素

```python
#These are techniques to apply function to element, column or dataframe.
#Map: It iterates over each element of a series. 
df[‘column1’].map(lambda x: 10+x), this will add 10 to each element of column1.
df[‘column2’].map(lambda x: ‘AV’+x), this will concatenate “AV“ at the beginning of each element of column2 (column format is string).

#Apply: As the name suggests, applies a function along any axis of the DataFrame.
df[[‘column1’,’column2’]].apply(sum), it will returns the sum of all the values of column1 and column2.
df0[['data1']].apply(lambda s:s+1)

#ApplyMap: 对dataframe的每一个元素施加一个函数
func = lambda x: x+2
df.applymap(func), dataframe每个元素加2 (所有列必须数字类型)12345678910111213
```

- contains

```python
# 使用DataFrame模糊筛选数据(类似SQL中的LIKE)
# 使用正则表达式进行模糊匹配,*匹配0或无限次,?匹配0或1次
df_obj[df_obj['套餐'].str.contains(r'.*?语音CDMA.*')] 

# 下面两句效果一致
df[df['商品名称'].str.contains("四件套")]
df[df['商品名称'].str.contains(r".*四件套.*")]
```

### 函数调用apply

~~~python
series = date.apply(fuction,axis = 1)#function为函数，axis = 1 为每次传一个row，axis = 0 传一个column
~~~

## Series

### 构建一个Series

~~~python
film_names = series_film.values
rt_scores = series_rt.values
series_custom = Series(rt_scores, index = film_names)#返回一个Series
print(series_custom[["Minions (2015)","Leviathan (2014)"]])
~~~

### Series排序

~~~python
#按index排序
date = date.sort_index()
#按value排序
date = date.sort_values()
~~~

## Others

### 选取Dateframe中column为float类型的数据

~~~python
# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))
print(deviations)
~~~

### 将string类型转化为Datetime类型

~~~python
date["DATE"] = pd.to_datetime(date["DATE"])
~~~

