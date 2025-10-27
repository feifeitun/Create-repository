import streamlit as st
import pandas as pd
import random

# 页面配置必须放在所有其他Streamlit命令之前
st.set_page_config(
    page_title='Pyhon大舞台，有肝你就来', 
    page_icon='🐒',
    layout='wide'
)

st.title("Pyhon大舞台，有肝你就来🏳️🏳️🏳️")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["个人简历生成器", "音乐播放器", "视频播放器", "数字档案", "美食推荐", "动物相册"])

with tab1:
    st.header("个人简历生成器")
    st.text('使用Streamlit创建您的个性化简历')

    d1, d2 = st.columns([1, 2])

    with d1:
        st.subheader('个人信息表单')
        st.markdown('***')
        name = st.text_input('姓名：', '')
        position = st.text_input('职位', '')
        phone = st.text_input('电话', '')
        email = st.text_input('邮箱', '')
        birth = st.text_input('出生日期', '')

        st.text('性别')
        def format_func(option):
            return f'{option}'
        
        sex = st.radio(
            '性别：', 
            ['男', '女', '其他'], 
            format_func=format_func, 
            horizontal=True, 
            label_visibility='hidden'
        )
         
        st.subheader('学历')
        learn = st.selectbox(
            '学历：', 
            ['小学', '初中', '高中', '本科', '硕士', '博士'], 
            format_func=format_func
        )

        st.subheader('语言能力')
        language = st.selectbox(
            '语言能力：', 
            ['Chinese', 'Japanese', 'French', 'Malaysian', 'Russian', 'English'],
            format_func=format_func
        )

        st.subheader('技能')
        skills = st.multiselect(
            '技能（可多选）：', 
            ['Python编程', 'Excel数据分析', 'PPT制作', 'SQL查询', '英语读写', '团队协作'],
            default=['Python编程']
        )

        age = st.slider('工作经验（年）', 0, 50)

        salary_range = st.slider(
            '期望薪资：',
            1000, 30000, (4000, 10000)
        )

        comment = st.text_area(
            label='个人简介：', 
            placeholder='简要介绍一下自己'
        )

        work_time = st.time_input("最佳工作时间")

        uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "png", "jpeg"])

    with d2:
        st.subheader('简历实时预览')
        st.markdown('***')
        st.write(f'# {name}' if name else '# 姓名')
        
        if uploaded_file is not None:
            st.image(uploaded_file, caption="本人照片", width=250)

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
            st.write('期望薪资：', f'{salary_range[0]} - {salary_range[1]}')
            st.write("最佳工作时间:", work_time)

        st.markdown('***')
        st.write('## 个人简介')
        st.write(comment if comment else '请在左侧填写个人简介')

with tab2:
    st.header("音乐播放器")
    st.subheader("音乐播放里的瘤子🤏")

    music_files = [
        {
            'url': 'https://music.163.com/song/media/outer/url?id=2751381348.mp3',
            'artist': '林俊杰 / 胡彦斌',
            'cover': 'https://p2.music.126.net/lEpbaWjrZnJcLn1bLiZJ9A==/109951172085778809.jpg?param=180y180',
            'info': '黑夜问白天\n词：易家扬\n曲：林俊杰'
        },
        {
            'url': 'https://music.163.com/song/media/outer/url?id=2666095018.mp3',
            'artist': '孙燕姿',
            'cover': 'https://p1.music.126.net/Z6rUwSkXwS_cn8AB7KqBaw==/109951170378435887.jpg?param=180y180',
            'info': '日落\nLyricist 词 : 小寒\nComposer 曲 : 张简君伟/邵豪Shao Hao/Nay Shalom宁夏'
        },
        {
            'url': 'https://music.163.com/song/media/outer/url?id=255294.mp3',
            'artist': '刘惜君',
            'cover': 'https://p1.music.126.net/gZ93OHvjWKwnvIwChuRTfA==/109951171315740884.jpg?param=180y180',
            'info': '我很快乐\n作词 : 祈合/张海\n作曲 : 祈合'
        },
        {
            'url': 'https://music.163.com/song/media/outer/url?id=423406145.mp3',
            'artist': '张信哲',
            'cover': 'https://p2.music.126.net/xt_oovsCzByJNCVOZLWgkA==/2946691201348447.jpg?param=180y180',
            'info': '过火\n作词 : 陈佳明\n作曲 : 曹俊鸿\n编曲 : 屠颖'
        }
    ]

    if 'current_music' not in st.session_state:
        st.session_state.current_music = 0

    def next_music():
        st.session_state.current_music = (st.session_state.current_music + 1) % len(music_files)
    
    def prev_music():
        st.session_state.current_music = (st.session_state.current_music - 1) % len(music_files)

    current = music_files[st.session_state.current_music]
    st.audio(current['url'])

    d1, d2 = st.columns(2)
    with d1:
        st.image(current['cover'], caption=current['artist'], width=200)
    with d2:
        st.text(current['info'])

    c1, c2 = st.columns(2)
    with c1:
        st.button('上一首', on_click=prev_music, use_container_width=True)
    with c2:
        st.button('下一首', on_click=next_music, use_container_width=True)

with tab3:
    st.header('弄弄囔囔视频播放器🥽')

    # 替换为真实视频链接（示例为B站视频嵌入链接，需注意跨域权限）
    video_files = [
        {
            'url': 'https://player.bilibili.com/player.html?aid=170001&cid=200001&page=1',
            'title': '第一集'
        },
        {
            'url': 'https://player.bilibili.com/player.html?aid=170002&cid=200002&page=1',
            'title': '第二集'
        },
        {
            'url': 'https://player.bilibili.com/player.html?aid=170003&cid=200003&page=1',
            'title': '第三集'
        },
        {
            'url': 'https://player.bilibili.com/player.html?aid=170004&cid=200004&page=1',
            'title': '第四集'
        }
    ]

    if 'current_video' not in st.session_state:
        st.session_state.current_video = 0

    def switch_video(index):
        st.session_state.current_video = index

    current = video_files[st.session_state.current_video]
    # 用iframe嵌入视频（Streamlit的st.video对部分链接支持有限）
    st.components.v1.iframe(current['url'], width=800, height=450)

    st.caption(f'当前播放: {current["title"]}')

    cols = st.columns(len(video_files))
    for i, col in enumerate(cols):
        with col:
            st.button(
                video_files[i]['title'], 
                use_container_width=True, 
                on_click=switch_video,
                args=(i,)
            )

with tab4:  # 修复缩进：该标签页下代码全部缩进
    st.markdown('# 🦥学生小何—数字档案')
    st.markdown('## 🦆基础信息')
    st.markdown('''### 学生ID：娃哈哈战士
注册时间: :green[2025-10-20]    |精神状态: :green[🤔耐人寻味]

当前教室: :yellow[实训楼204]     |安全等级: :red[绝密]''')
    st.markdown('## 🥝技能矩阵')

    c1, c2, c3 = st.columns(3)
    c1.metric(label="C语言", value="1%", delta="-1.5%")  # 修正delta单位（原“℃”错误）
    c2.metric(label="Python", value="50%", delta="6%")
    c3.metric(label="Java", value="10%", delta="1%")  # 修正“jave”拼写错误

    st.markdown('## streamlit课程进度')
    st.progress(value=0.4, text="进度40%")  # 添加进度文本，提升可读性

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
    # 修复代码语法错误（缩进、缺少冒号）
    python_code = '''def matrix_breach():
    while True:
        if detect_vulnerability():
            exploit()
            return "ACCESS GRANTED"
        else:
            stealth_evade()'''

    st.code(python_code, language='python')  # 指定代码语言，优化高亮
    st.markdown('''###

:red[>>SYSTEM MESSAGE:]下一个任务目标已解锁...

:red[>>TARGET:]课程管理系统

:red[>>COUNTDOWN:]2025-06-03

系统状态:在线  链接状态:已加密''')

with tab5:
    # 配置美食图片链接（选用更稳定的外部链接）
    img_list = [
        "https://ts1.tc.mm.bing.net/th/id/R-C.9cabd5c52c7e154f547ba623f4c6da33?rik=W%2fulim8xKCgdWw&riu=http%3a%2f%2fwww.szquanli.com%2fuploads%2fallimg%2f181107%2f2-1Q10F92202.jpg&ehk=qgMzR%2f0Vyc%2fmRAPiVR7nFbpzAX4yb0ajoJntP5AaJE0%3d&risl=&pid=ImgRaw&r=0",
        "https://pic.nximg.cn/file/20230309/14773619_224017364109_2.jpg",
        "https://cf.dtcj.com/1756caf3-9b15-47ae-9ca8-3ec320e73203.jpg?imageslim",
        "https://ts1.tc.mm.bing.net/th/id/R-C.085070a026f817636729d175e90b3815?rik=QMZqI5TvuXbt7w&riu=http%3a%2f%2fwww.senn.com.cn%2fUploadFiles%2f2022%2f3%2f202203271533267149.jpg&ehk=hCEsINLjXFsR%2fPHVFcjauUlNdgpYxyKahGEE7GTTHcQ%3d&risl=&pid=ImgRaw&r=0",
        "https://32571698.s21i.faiusr.com/4/ABUIABAEGAAgraf8tQYoq4WU4AcwgAU4pgM!450x450.png"
    ]

    st.title("美食推荐")

    if st.button("今日吃什么"):
        random_img = random.choice(img_list)
        st.image(random_img, caption="今日推荐美食", use_column_width=True)
    else:
        st.image(img_list[0], caption="初始展示：第一张图", use_column_width=True)

with tab6:
    st.set_page_config(page_title='YAMI', page_icon='🐒')
    st.header("🤓震惊动物园运营只剩下最后三只动物......")
    
    images = ['https://cdn.pixabay.com/photo/2018/05/03/22/34/lion-3372720_1280.jpg',
              'https://dl0.creation.com/fpimages/11724.jpg',
              'https://breedingbusiness.com/wp-content/uploads/2021/07/cutest-small-white-dog-breeds.jpg']

    captions = ['狮子🦁', '虎子🐯', '狗子🐕']
    if 'a' not in st.session_state:
        st.session_state['a'] = 0
        
    def nextimg():
        st.session_state['a'] =(st.session_state['a']+1) % len(images)
    
      
    def next2mg():
        st.session_state['a'] =(st.session_state['a']-1) % len(images)


    # st.image()总共两个参数，url：图片地址 caption:图片的备注
    st.image(images[st.session_state['a']], captions[st.session_state['a']])



    c1, c2 = st.columns(2)
    with c1:
        st.button('上一张', on_click=next2mg, use_container_width=True)
    
    with c2:
        st.button('下一张', on_click=nextimg, use_container_width=True)
