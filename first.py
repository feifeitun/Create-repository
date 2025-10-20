import streamlit as st


st.markdown('# 🦥学生小何—数字档案')
st.markdown('## 🦆基础信息')
st.markdown('''### 学生ID：娃哈哈战士
注册时间: :green[2025-10-20]    |精神状态: :green[🤔耐人寻味]

当前教室: :yellow[实训楼204]     |安全等级: :red[绝密]''')
st.markdown('## 🥝技能矩阵')

c1, c2, c3 = st.columns(3)
c1.metric(label="c语言", value="1%", delta="-1.5℃")
c2.metric(label="python", value="50%", delta="6%")
c3.metric(label="jave", value="10%", delta="1%")


st.markdown('## streamlit课程进度')
st.progress(value=0.4, text=None)
import pandas as pd
import streamlit as st


data = {
    '地图':['巴克十', '航天', '大坝'],
    '人物':['红狼', '梁帅', '威龙'],
    '难度':['绝密', '绝密', '绝密'],
}

index = pd.Series(['01月', '02月', '03月'], name='月份')

df = pd.DataFrame(data, index=index)

st.subheader('默认显示')
st.dataframe(df)

st.subheader('Python代码块')

python_code = '''def matrix_breach():
    while True:
    if detect_vulnerability():
    exploit()
    return "ACCESS GRANTED"
    else:
    stealth_evade()'''


st.code(python_code)
st.markdown('''###

:red[>>SYSTEM MESSAGE:]下一个任务目标已解锁...

:red[>>TARGET:]课程管理系统

:red[>>COUNTDOWN:]2025-06-03

系统状态:在线  链接状态:已加密''')
