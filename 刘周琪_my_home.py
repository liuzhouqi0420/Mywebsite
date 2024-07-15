'''
工作室名字：……
根据地用户：个人使用、只有几个人知道的秘密基地、分享后所有人可见……
根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站……
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区
现有模块改进灵感：……
原创模块：……
原创模块一句话功能介绍：……
'''

import streamlit as st
import PIL as image

page = st.sidebar.radio('我的首页', ['我的个人资料','我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区','我的问题'])

def page_1():
    '''我的个人资料'''
    st.subheader('个人资料')
    st.markdown('<h3 style="font-size:20px;">兴趣爱好</h3>', unsafe_allow_html=True)  
    st.write(':fireworks:舞蹈:fireworks:')
    st.image('舞蹈.jpg')
    st.write(':fireworks:书法:fireworks:')
    st.image('背景图片.jpeg')

def page_2():
    '''我的兴趣推荐'''
    with open('春池嫣韵.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('背景图片.jpeg')
    st.write('我的书法作品推荐')
    st.write('东方朔画像赞、行书千字文、洛神赋、祭侄文稿等')
    st.write('-----------------------------------------------------')
    st.write('我的书法字帖推荐')
    st.write('曹全碑、张迁碑、雁塔圣教序、九成宫、智永等')
    st.write('-----------------------------------------------------')

def page_3():
    '''我的图片处理工具'''
    st.write(':sunglasses:图片换色小程序:sunglasses:')
    uploaded_file = st.file_uploader("上传图片", type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.toggle('增强对比度')
            bw = st.toggle('黑白滤镜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                img = img_change_ch(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            st.write('右键"另存为"保存图片')
            st.image(img)

def page_4():
    '''我的智慧词典'''
    st.write('智能词典')
    with open('words_space.txt','r',encoding='utf-8')as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt','r',encoding='utf-8')as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        #        if word == 'python':
        #            st.code('''
        #                    # 恭喜你触发彩蛋，这是一行python代码
        #                    print('hello world')''')
        #        elif word == 'balloon':
        #            st.balloons()
        #        elif word == 'snow':
        #            st.snow()
        n = words_dict[word][0]
        st.write('查询次数：', times_dict[n])
        if n in times_dict:
            times_dict[n] += 1
        else :
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8')as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)

def page_5():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫' :
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str((int(messages_list[-1][0]) + 1)), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list():
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page_6():
    '''我的问题'''
    cb = st.checkbox('勾选选项')
    if cb:
        st.write('选项被勾选', cb)
    st.write('----')
    st.write('你知道书法有哪些主要字体吗？(5个)')
    cb1 = st.checkbox('楷书')
    cb2 = st.checkbox('篆书')
    cb3 = st.checkbox('隶书')
    cb4 = st.checkbox('草书')
    cb5 = st.checkbox('行书')
    cb6 = st.checkbox('金文')
    cb7 = st.checkbox('甲骨文')
    cb8 = st.checkbox('小篆')
    l = [cb1, cb2, cb3, cb4, cb5]
    m = [cb6, cb7, cb8]
    if st.button('确认答案'):
        if True in l and True not in m:
            st.write('好厉害哦！答案选对了！')
        elif True in m:
            st.write('不对哦！再看一看题目哦！')

def img_change_ch(img):
    '''图片反色滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img

if page == '我的个人资料':
    page_1()
elif page == '我的兴趣推荐':
    page_2()
elif page == '我的图片处理工具':
    page_3()
elif page == '我的智慧词典':
    page_4()
elif page == '我的留言区':
    page_5()
elif page == '我的问题':
    page_6()

