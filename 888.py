import streamlit as st

st.set_page_config(page_title='个人简历', page_icon='🐒',layout='wide')
st.title("个人简历生成器")

st.text('使用seamlit创建您的个性化简历')

d1, d2 = st.columns([1, 2])

with d1:

    st.subheader('个人信息表单')
    st.markdown('***')
    name = st.text_input('姓名：', '')

    position = st.text_input('职位', autocomplete='')

    phone = st.text_input('电话', autocomplete='name')

    email = st.text_input('邮箱', autocomplete='name')

    birth = st.text_input('出生日期', autocomplete='name')

    def my_format_func(option):
        return f'{option}'

    st.text('性别')
    sex = st.radio('性别：', ['男', '女','其他'], format_func=my_format_func, horizontal=True, label_visibility='hidden')
     
    

    def my_format_func(option):
        return f'{option}'

    st.header('下拉按钮示例')
    learn = st.selectbox('学历：', ['小学', '初中', '高中', '本科', '硕士', '博士'], format_func=my_format_func)

    def my_format_func(option):
        return f'{option}'

    st.header('下拉按钮示例')
    language = st.selectbox('语言能力：', ['Chinese', 'Jaanese', 'Franch', 'Malaysian', 'Russian', 'English'], format_func=my_format_func)

    def my_format_func(option):
        return f'{option}'

    st.header('下拉按钮示例')
    city = st.selectbox('技能（可多选）：', ['倒立吃泡面', '胸口碎大石', '叶问拉屎', '林黛玉倒拔垂杨柳', '厕所无掩体干拉', '母猪无痛分娩'], format_func=my_format_func, index=3)

    from datetime import datetime, time

    age = st.slider('工作经验', 0, 50)

    values = st.slider(
    '牛马劳务费：',
    1000, 30000, (4000, 10000))

    g1= st.text_area(label='建议或意见：', placeholder='简要说说您的牛马人生')

    from datetime import datetime, time

    w1 = st.time_input("工作时间")

    uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
    

with d2:
    st.subheader('简历实时预览')
    st.markdown('***')
    st.write('#', name)
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        st.image(bytes_data, caption="本人照片", width=250)

    c1, c2 = st.columns(2)

    with c1:
        st.write('职位：', position)
        st.write('电话：', phone)
        st.write('邮箱：', email)
        st.write('出生日期：', birth)
    with c2:
        st.write('性别：', sex)
        st.write('学历：', learn)
        st.write('语言能力：', language)
        st.write("工作经验：", age, '年')
        st.write('牛马劳务费：', values)
        st.write("最佳牛马工作时间:", w1)

    st.markdown('***')
    st.write('##', '个人简介')
    st.write(g1)
    
