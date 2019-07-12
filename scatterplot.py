from matplotlib import pyplot as plt
from matplotlib import font_manager

# 使得中文可以显示出来
my_font = font_manager.FontProperties(fname="/Library/Fonts/Arial Unicode.ttf")
y_3 = [11, 15, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 19, 21, 22, 22,
       22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12,
        13, 6]
x = range(0, 31)
# print(len(y_3))
plt.figure(figsize=(20, 8), dpi=80)
# 使用scatter绘制散点图和绘制折线图的唯一区别
# x,y两个字段的个数应该要能够对应得上
plt.scatter(x, y_3,label="3月份")
x_2 = range(38, 69)
# lable字段可以为图表添加图例
plt.scatter(x_2, y_10,label="10月份")

# 调整x轴刻度
_x = list(x) + list(x_2)
_xtick_labels = ["3月{}日".format(i) for i in x]
_xtick_labels += ["10月{}日".format(i - 37) for i in x_2]
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)

# 添加坐标轴描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)
# 设置图表title
plt.title("三月份与十月份温度对比", fontproperties=my_font)
# 添加图例
plt.legend(loc="upper left",prop=my_font)
plt.show()