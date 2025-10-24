import streamlit as st


st.set_page_config(page_title='音乐播放器', page_icon='🐒')
st.header("音乐播放里的瘤子🤏")
st.markdown('***')
# 读取音频URL
audio_file = [{
    'url': 'https://music.163.com/song/media/outer/url?id=2751381348.mp3',
    'parm': '林俊杰 / 胡彦斌',
    'photo': 'https://p2.music.126.net/lEpbaWjrZnJcLn1bLiZJ9A==/109951172085778809.jpg?param=180y180',
    '1': '黑夜问白天\n词：易家扬\n 曲：林俊杰\n 时长：4:31'},
              {
    'url': 'https://music.163.com/song/media/outer/url?id=2666095018.mp3',
    'parm': '孙燕姿',
    'photo': 'https://p1.music.126.net/Z6rUwSkXwS_cn8AB7KqBaw==/109951170378435887.jpg?param=180y180',
    '1': '日落\nLyricist 词 : 小寒\n Composer 曲 : 张简君伟/邵豪Shao Hao/Nay Shalom宁夏\n 时长：4:09'},
              {
    'url': 'https://music.163.com/song/media/outer/url?id=255294.mp3',
    'parm': '刘惜君',
    'photo':  'https://p1.music.126.net/gZ93OHvjWKwnvIwChuRTfA==/109951171315740884.jpg?param=180y180',
    '1': '我很快乐\n作词 : 祈合/张海\n 作曲 : 祈合\n 时长：3:33'},
              {
    'url': 'https://music.163.com/song/media/outer/url?id=423406145.mp3',
    'parm': '张信哲',
    'photo': 'https://p2.music.126.net/xt_oovsCzByJNCVOZLWgkA==/2946691201348447.jpg?param=180y180',
    '1': '过火\n作词 : 陈佳明\n作曲 : 曹俊鸿\n编曲 : 屠颖\n 时长：5:02'}
              
              ]


if 'a' not in st.session_state:
    st.session_state['a'] = 0
    
def nextimg():
    st.session_state['a'] =(st.session_state['a']+1) % len(audio_file)
    
  
def next2mg():
    st.session_state['a'] =(st.session_state['a']-1) % len(audio_file)


# st.image()总共两个参数，url：图片地址 caption:图片的备注

d1, d2 = st.columns([1, 2])
with d1:
    st.image(audio_file[st.session_state['a']]['photo'], caption = audio_file[st.session_state['a']]['parm'])
with d2:
    st.text(audio_file[st.session_state['a']]['1'])
    st.audio(audio_file[st.session_state['a']]['url'])
c1, c2 = st.columns(2)
with c1:
    st.button('⬅️上一首', on_click=next2mg, use_container_width=True)

with c2:
    st.button('下一首➡️', on_click=nextimg, use_container_width=True)
st.markdown('***')



st.header("留言板⬜")
aa = st.text_area('评论：', height = 150)






















