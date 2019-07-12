import matplotlib as mpl
import matplotlib.pyplot as plt

# 生成数据
labels = ['A', 'B', 'C', 'D', '其他']
share = [0.45, 0.25, 0.15, 0.05, 0.10]

# 设置分裂属性
explode = [0, 0.1, 0, 0, 0]

# 分裂饼图
plt.pie(share, explode = explode,
        labels = labels, autopct = '%3.1f%%',
        startangle = 180, shadow = True,
        colors = ['c', 'r', 'gray', 'g', 'y'])

# 标题
plt.title('2017年笔记本电脑市场份额')

plt.show()