# 可视化知识点整理

[TOC]



## 显示中文

~~~python
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
~~~

## 图片嵌入显示

~~~python
%matplotlib inline  #notebook模式下
%pylab inline    #ipython模式下
~~~

## 引入多个子图

~~~python
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)#第一个参数是行数，第二个参数是列数，第三个是子图标号
ax2 = fig.add_subplot(2,1,2)
~~~

## matplotlab绘图

### 折线图

~~~python
plt.plot(data["DATE"],data["VALUE"],c = colors,label = subline_name,linewidth = 3)#第一个元素为x轴，第二个为y轴,c代表折线的颜色,如:["red","blue","green","orange","black"],label主要是在legend中标记线段的名字,linewidth刻画线条的宽度
plt.xticks(rotation = 90)#将x轴各个刻度的label旋转90°
plt.xlabel('Date')#设置x轴label
plt.ylabel('Value')#设置y轴label
plt.title('Draw Picture')#设置图的名称
plt.legend(loc = "upper left")#图例，loc参数主要用来标记legend位置
plt.show()

#简图
ax.tick_params(bottom="off", top="off", left="off", right="off")#将刻度线隐藏
for key,spine in ax.spines.items():#隐藏边界线
    spine.set_visible(False)
ax.spines["right"].set_visible(False)#同上
#例子1
major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))
for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])#设置y轴可取0和100两个值
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off"，labelbottom='off')#labelbottom为刻度显示的label
    if (sp == 0):
        ax.text(2005,87,"Men")
        ax.text(2002,8,"Women")
    if (sp == 4):
        ax.text(2005,62,"Men")
        ax.text(2001,35,"Women")
        ax.tick_params(labelbottom='on')#最后一行显示刻度的label
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)#设置中位线，alpha为透明度，第一个参数为y轴位置
plt.legend(loc='upper right')
plt.show()
~~~

### 盒状图

~~~python
import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = date[num_cols].iloc[0].values#Heights of the bars，只接受list
tick_positions = range(1,6)#刻度的位置
ax.set_yticks(tick_positions)#设置刻度
ax.set_yticklabels(num_cols)#刻度的label
bar_positions = arange(5) + 0.75#Positions of the left sides of the bars.
fig, ax = plt.subplots()
ax.bar(bar_positions,bar_heights,0.5)#第三个参数是单个bar的宽度
plt.show()
~~~

### 散点图

~~~python
fig, ax = plt.subplots()
ax.scatter(date["x"],date["y"])
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
~~~

### 条形图

~~~python
#hooding的操作
fandango_count = norm_reviews["Fandango_Ratingvalue"].value_counts()#统计每个value出现的频率，返回series：index = 原值，value = 原值统计个数 
fandango_distribution = fandango_count.sort_index()#按照index排序
#histogram 
fig, ax = plt.subplots()
ax.hist(norm_reviews["Fandango_Ratingvalue"],bins = 20，range =(0,5))#bins参数为设置的条的个数，range为默认条形图的刻度分布，可以不设置
ax。set_ylim(0,50)#设置y轴取值的范围
~~~

###盒图（四分位图IQR）

~~~python
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig, ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols, rotation =90)
ax.set_ylim(0,5)
plt.show()
~~~

## pandas快速制图

### 散点图

~~~python
#%matplotlib inline
recent_grads.plot(x = "Sample_size" , y = "Median",kind = "scatter")
~~~

### 直方图

~~~python
recent_grads["Sample_size"].plot(kind='hist', rot=40)
recent_grads['Sample_size'].hist(bins=25, range=(0,5000))
~~~

### 散点&直方图组合（scatter_matrix）

~~~python
from pandas.tools.plotting import scatter_matrix 
scatter_matrix(recent_grads[['Sample_size','Median','Unemployment_rate']],figsize = (10,10))#对角线为直方图，其他散点
~~~

![](                                                                                                                                                                      [Dataquest](https://github.com/yangxx1208/Dataquest)/[Picture](https://github.com/yangxx1208/Dataquest/tree/master/Picture)/**scatter_matrix.png**     )

## Color Blind

~~~python
color = (R/255,G/255,B/255)
~~~

![](                                                                                                                                                                      [Dataquest](https://github.com/yangxx1208/Dataquest)/[Picture](https://github.com/yangxx1208/Dataquest/tree/master/Picture)/**color_blind.png**     )

## 保存图片

~~~python
plt.savefig('biology_degrees.png')
~~~

## seaborn制图

###KDE核密度估计分布图

~~~python
#绘制具有直方图的kde分布图
import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(date["Age"])
#绘制kde曲线分布图
sns.set_style("white")#设置风格
sns.kdeplot(date["Age"],shade = True)#shade参数控制曲线下方是否为阴影
sns.despine(left =True , bottom = True)#左，右边界线隐藏，默认上，右边界线隐藏
plt.xlabel("Age")
~~~

sns.set_style()参数风格：

![](                                                                                                                                                                      [Dataquest](https://github.com/yangxx1208/Dataquest)/[Picture](https://github.com/yangxx1208/Dataquest/tree/master/Picture)/**sns_setstyle.png**     )

###FacetGrid()

~~~python
g = sns.FacetGrid(titanic , col = "Pclass", hue = "Sex",size = 6)#size参数控制plot高度大小
g.map(sns.kdeplot , "Age",shade = True)
g.add_legend()#用来区别hue的legend
g.despine(bottom = True,left = True)
plt.show()
~~~

![](                                                                                                                                                                      [Dataquest](https://github.com/yangxx1208/Dataquest)/[Picture](https://github.com/yangxx1208/Dataquest/tree/master/Picture)/**FacetGrid.png**     )

## basemap绘制二维地图

~~~python
#绘制散点图
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
fig,ax = plt.subplots(figsize = (15,20))#设置图片大小，仅可在此设置
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180)#projection参数是投影方式，llcrnrlat纬度左下边界，urcrnrlat纬度右上，llcrnrlon经度左下，urcrnrlon经度右上
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()#仅接受list()类型
x, y = m(longitudes, latitudes)#将经纬度转化为二维平面坐标
m.scatter(x,y,s = 1)#绘制散点图，s为点的大小
m.drawcoastlines()#绘制海岸线
#绘制路线图
fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()
def create_great_circles(df):
    for index, row in df.iterrows():
        end_lat, start_lat = row['end_lat'], row['start_lat']
        end_lon, start_lon = row['end_lon'], row['start_lon']
        
        if abs(end_lat - start_lat) < 180:#绘制路线，经纬度差不超过180
            if abs(end_lon - start_lon) < 180:
                m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat)#绘制路线

dfw = geo_routes[geo_routes['source'] == "DFW"]#出发点为“source”
create_great_circles(dfw)
plt.show()
~~~

## 参考其他

### [seaborn简介和实例](http://blog.csdn.net/qq_34264472/article/details/53814653)  

###Python绘图精简实例附代码

- [引自知乎如何在论文中画出漂亮的插图](http://blog.csdn.net/golden1314521/article/details/44700551#1引自知乎如何在论文中画出漂亮的插图)
- [正态曲线图](http://blog.csdn.net/golden1314521/article/details/44700551#2正态曲线图)
- [云模型示意图](http://blog.csdn.net/golden1314521/article/details/44700551#3云模型示意图)
- [scatter-hist图](http://blog.csdn.net/golden1314521/article/details/44700551#4-scatter-hist图)
- [若干类型的图例](http://blog.csdn.net/golden1314521/article/details/44700551#5若干类型的图例)
- [热图](http://blog.csdn.net/golden1314521/article/details/44700551#6热图)
- [为点加标签](http://blog.csdn.net/golden1314521/article/details/44700551#7为点加标签)
- [导入已有图片并进行修饰](http://blog.csdn.net/golden1314521/article/details/44700551#8导入已有图片并进行修饰)
- [热度方格图](http://blog.csdn.net/golden1314521/article/details/44700551#９热度方格图)
- [箱线图](http://blog.csdn.net/golden1314521/article/details/44700551#10-箱线图)
- 双纵坐标
  - [legend不在一块](http://blog.csdn.net/golden1314521/article/details/44700551#legend不在一块)
  - [legend放一块儿](http://blog.csdn.net/golden1314521/article/details/44700551#legend放一块儿)
  - [多个子图共用一个legend](http://blog.csdn.net/golden1314521/article/details/44700551#多个子图共用一个legend)

## 提升学习

In this mission, we learned how to visualize geographic data using basemap.  This is the last mission in the **Storytelling Through Data Visualization** course.  You should now have a solid foundation in data visualization for exploring data and communicating insights.  We encourage you to keep exploring data visualization on your own.  Here are some suggestions for what to do next:

- Plotting tools:

  - [Creating 3D plots using Plotly](https://plot.ly/python/3d-scatter-plots/)
  - [Creating interactive visualizations using bokeh](http://bokeh.pydata.org/en/latest/)
  - [Creating interactive map visualizations using folium](https://folium.readthedocs.io/en/latest/)

- The art and science of data visualization:

  - [Visual Display of Quantitative Information](https://www.amazon.com/Visual-Display-Quantitative-Information/dp/0961392142)

  - [Visual Explanations: Images and Quantities, Evidence and Narrative](https://www.amazon.com/Visual-Explanations-Quantities-Evidence-Narrative/dp/0961392126)

    ​

