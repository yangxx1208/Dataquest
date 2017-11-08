# scikit-Learn

[TOC]



## 数据标准化、正则化

### 标准化scale

#### 使用sklearn.preprocessing.scale()方法

~~~python
from sklearn import preprocessing
# standardize the data attributes
standardized_X = preprocessing.scale(X) #按列操作
standardized_X.mean(axis = 0) #均值（axis=0不能少，按列操作）
standardized_X.std(axis = 0) #标准差

~~~

#### 使用sklearn.preprocessing.StandardScaler类

~~~python
from sklearn import preprocessing
scaler = preprocessing.StandardScaler().fit(x) #构建类的实例
#可以选择不进行中心化或标准化，设置参数with_mean=False/with_std=False
#scaler = preprocessing.StandardScaler(with_mean = True, with_std = False).fit(x)
scaler.mean_ #保存原始均值
scaler.std_ #保存原始标准差
standardized_X = scaler.transform(x) #返回标准化之后的数据
scaler_data = scaler.transform(data) #对测试数据进行标准化（使用训练数据的均值、方差）
~~~

#### 使用sklearn.preprocessing.MinMaxScaler类缩放至范围，默认[0 ,1]

~~~python
min_max_scaler= preprocessing.MinMaxScaler() #构建类的实例
#可以设置范围feature_range=(min, max)
min_max_scaler.scale_ #缩放因子
min_max_scaler.min_ #数据乘以缩放因子之后，需要中心化的值
# 公式x*min_max_scaler.scale_ + min_max_scale.min_
data_minmax = min_max_scaler.fit_transform(x) #返回缩放后的数据
data_minmax = min_max_scaler.transform(x) #将相同的缩放应用到测试集数据中

~~~

### 正则化normalize

####使用sklearn.preprocessing.normalize()方法

```python
from sklearn import preprocessing
# normalize the data attributes
normalized_X = preprocessing.normalize(X) #可以设置参数norm，选择范数类型
#X_normalized = preprocessing.normalize(X, norm='l2') 
```

#### 使用sklearn.preprocessing.Normalizer类

~~~python
normalizer = preprocessing.Normalizer().fit(X) #返回关于数据X的实例
norm_x = normalizer.transform(X) #返回正则化后的数据
~~~



## 特征选取

### 随机数：

~~~python
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier() #选择的模型，决策树
model.fit(X, y) #feature ， label
# display the relative importance of each attribute
print(model.feature_importances_) #输出特征的重要程度
~~~

### 逻辑回归：

~~~python
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(train_feature,train_target)
coefficients = lr.coef_ #度量特征重要程度
feature_importance = pd.Series(coefficients[0],index=train_feature.columns)
feature_importance.plot.barh()
plt.show()
~~~

### 递归特征去除:

~~~python
from sklearn.feature_selection import RFECV
lr = LogisticRegression()
selector = RFECV(lr,cv=10)
selector.fit(all_X,all_y) #训练模型
optimized_columns = all_X.columns[selector.support_] #selector.support_将删选出来的特征置为true
~~~

### 热点图观察特征相关性

```python
#画图函数，用来查看相关性较大的属性
def plot_correlation_heatmap(df):
    corr = df.corr()
    
    sns.set(style="white")
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()

```

### 随机划分数据集

~~~python
from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(all_X, all_y, test_size=0.20,random_state=0) #test_size确定训练和测试数据的比列，random_state方便重复实验，得到不同结果，填1结果相同
~~~



## 模型

### 线性回归

```python
#首先计算协方差，查看适合线性回归的特征值
#也可以使用之前特征选择的方式，选择特征值
pandas.DataFrame.corr()

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train[["Gr Liv Area"]],train["SalePrice"])
print(lr.coef_)
print(lr.intercept_)

data_predic = lr.predict(data)
```

公式：

$$\hat{y}(w,x)=w_0+w_1x_1+...+w_px_p$$

$w=(w_1,...,w_p)$ as coef_ and $w_0$ as intercept_

线性回归运用最小二乘法，故而对误差尤其敏感（平方项会让系数偏向误差较大的方向）

### 逻辑回归

~~~python
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(train[columns], train["Survived"])
~~~



## 交叉验证

~~~python
from sklearn.model_selection import cross_val_score
lr = LogisticRegression()
scores = cross_val_score(lr, all_X, all_y, cv=10)
~~~

## 误差分析

### 残差

~~~python
from sklearn.metrics import mean_squared_error
data_rmse = mean_squared_error(data_predic,data_real)
~~~

### 查准率

~~~python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(data_real, predictions)
~~~



## others

这一章节告诉我必须要看原版帮助文档，网上的有参差不齐：[scikitLearn](http://scikit-learn.org/stable/index.html)

```python
sklearn.neighbors.KNeighborsRegressors
sklearn.linear_model.LinearRegression
```

