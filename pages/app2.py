import streamlit as st

ani_list = ['짱구', '몬스터','씨범']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']
data = [1, 2, 3]

# url = 'https://naver.com'

# 입력창에서 데이터를 받아서
# 해당 문자열이 일치하는 이미지를 화면에 출력
name = st.text_input("검색하실 애니메이션을 입력")
img_idx=0
for ani_ in ani_list:
    if name in ani_:    
        # ani_list에서 특정 문자열을 포함한 인덱스
        img_idx = ani_list.index(ani_)

if (img_idx == -1):
    st.write('찾는 애니메이션의 이미지가 없습니다.')
else:
    st.image(img_list[img_idx])