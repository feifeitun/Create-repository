import streamlit as st
import pandas as pd
import random



# 定义数据,以便创建数据框
data = {
    '月份':['01月', '02月', '03月','04月','05月'],
    '廖哥土鲫鱼':[200, 150, 180, 200, 220],
    '蓝师傅柳州螺蛳粉':[120, 160, 123, 230, 210],
    '味千拉面':[110, 100, 160, 210, 240],
    '塔斯汀':[160, 260, 224, 250, 300],
    '肯德基':[140, 180, 200, 260,320],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series(['廖哥土鲫鱼', '蓝师傅柳州螺蛳粉', '味千拉面','塔斯汀','肯德基' ], name='店名')
# 将新索引应用到数据框上
st.header("地图🗺️")
df.index = index


map_data = {
    'latitude':[22.840397, 22.854321, 22.869240, 22.816112, 22.829863],
    'longitude':[108.245340, 108.222742, 108.292583, 108.319051, 108.290909],

    }
st.map(pd.DataFrame(map_data))


# 使用write()方法展示数据框
st.header("门店数据🥗")
st.write(df)
st.markdown('***')
st.header("折线图🍿")
st.markdown('***')

# 通过x指定月份所在这一列为折线图的x轴
st.line_chart(df, x='月份')
st.markdown('***')
st.header("面积图🍙")


# 通过x指定月份所在这一列为面积图的x轴
st.area_chart(df, x='月份')
st.markdown('***')
st.header("条形图🍝")



# 通过x指定月份所在这一列为折线图的x轴
st.bar_chart(df, x='月份')

# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('月份', inplace=True)


data2 = {
    '店铺':['廖哥土鲫鱼', '蓝师傅柳州螺蛳粉', '味千拉面','塔斯汀','肯德基'],
    '评分':[4.9,3.2,3.8,4.1,4.8]
} 
df2 = pd.DataFrame(data2)
index2 = pd.Series([1,2,3,4,5,], name='')
df2.index = index2

st.markdown('***')
st.header("⭐ 餐厅评分 ⭐")
st.bar_chart(df2, x='店铺')

st.markdown('***')

# 1. 配置本地图片路径列表
img_list = ["https://ts1.tc.mm.bing.net/th/id/R-C.9cabd5c52c7e154f547ba623f4c6da33?rik=W%2fulim8xKCgdWw&riu=http%3a%2f%2fwww.szquanli.com%2fuploads%2fallimg%2f181107%2f2-1Q10F92202.jpg&ehk=qgMzR%2f0Vyc%2fmRAPiVR7nFbpzAX4yb0ajoJntP5AaJE0%3d&risl=&pid=ImgRaw&r=0",
            "https://cf.dtcj.com/1756caf3-9b15-47ae-9ca8-3ec320e73203.jpg?imageslim",
            'https://ts1.tc.mm.bing.net/th/id/R-C.085070a026f817636729d175e90b3815?rik=QMZqI5TvuXbt7w&riu=http%3a%2f%2fwww.senn.com.cn%2fUploadFiles%2f2022%2f3%2f202203271533267149.jpg&ehk=hCEsINLjXFsR%2fPHVFcjauUlNdgpYxyKahGEE7GTTHcQ%3d&risl=&pid=ImgRaw&r=0',
            'https://32571698.s21i.faiusr.com/4/ABUIABAEGAAgraf8tQYoq4WU4AcwgAU4pgM!450x450.png'] # 示例：3张本地图片

# 2. 页面标题与核心功能
st.title("美食推荐")

# 3. 点击按钮触发随机选图
if st.button("今日吃什么"):
# 随机选一张图的路径
    random_img = random.choice(img_list)
# 展示选中的图片
    st.image(random_img, caption=f"1：{random_img}", use_column_width=True)
else:
# 初始未点击时，默认显示第一张图（可选）
    st.image(img_list[0], caption="初始展示：第一张图", use_column_width=True)

