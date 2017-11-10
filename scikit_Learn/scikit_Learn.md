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

### k—近邻

~~~python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1) #k近邻的k值
scores = cross_val_score(knn, data_feature, data_result, cv=10)
accuracy_knn = scores.mean()

#训练数据集
knn.fit(iris.data, iris.target)
#训练准确率
score = knn.score(iris.data, iris.target)
#预测
predict = knn.predict([[0.1,0.2,0.3,0.4]])
#预测，返回概率数组
predict2 = knn.predict_proba([[0.1,0.2,0.3,0.4]])
~~~

KNeighborsClassifier(n_neighbors=5, weights='uniform', 
​                      algorithm='auto', leaf_size=30, 
​                      p=2, metric='minkowski', 
​                      metric_params=None, n_jobs=1, **kwargs)
n_neighbors: 默认值为5，表示查询k个最近邻的数目
algorithm:   {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’},指定用于计算最近邻的算法，auto表示试图采用最适合的算法计算最近邻
leaf_size:   传递给‘ball_tree’或‘kd_tree’的叶子大小
metric:      用于树的距离度量。默认'minkowski与P = 2（即欧氏度量）
n_jobs:      并行工作的数量，如果设为-1，则作业的数量被设置为CPU内核的数量
查看官方 [api](http://scikit-learn.org/dev/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier)

### 决策树

~~~python
#普通
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=1) #random_state用于模型之后的再塑
scores = cross_val_score(clf, all_X, all_y, cv=10)
accuracy_rf = scores.mean()

#超参数选择
hyperparameters = {"criterion": ["entropy", "gini"], #标准
                   "max_depth": [5, 10],  #最大深度
                   "max_features": ["log2", "sqrt"], 
                   "min_samples_leaf": [1, 5],
                   "min_samples_split": [3, 5],
                   "n_estimators": [6, 9]
}

clf = RandomForestClassifier(random_state=1)
grid = GridSearchCV(clf,param_grid=hyperparameters,cv=10)

grid.fit(all_X, all_y)

best_params = grid.best_params_

~~~

[官方文档](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

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

## 模型超参数选择

~~~python
from sklearn.model_selection import GridSearchCV

hyperparameters = {
    "n_neighbors": range(1,20,2),
    "weights": ["distance", "uniform"],
    "algorithm": ['brute'],
    "p": [1,2]
}
knn = KNeighborsClassifier()
grid = GridSearchCV(knn,param_grid=hyperparameters,cv=10) #这里仅仅是超参数的选择，还可以对模型进行选择

grid.fit(all_X, all_y)
best_params = grid.best_params_ #精度最高时的超参数
best_score = grid.best_score_ #精度最高的值

grid.best_estimator_ #提取参数值
~~~



## others

这一章节告诉我必须要看原版帮助文档，网上的有参差不齐：[scikitLearn](http://scikit-learn.org/stable/index.html)

```python
sklearn.neighbors.KNeighborsRegressors
sklearn.linear_model.LinearRegression
```
