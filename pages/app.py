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
# if ani_list[0] in name:
#     st.image(img_list[0])
#     st.download_button("Download file", img_list[0])
# elif ani_list[1] in name:
#     st.image(img_list[1])
#     st.download_button("Download file", img_list[1])
# elif ani_list[2] in name:
#     st.image(img_list[2])
#     st.download_button("Download file", img_list[2])

# 입력화면 - HTML/CSS/JS 로 최종적으로 변환
val1 = st.button("짱구")
val2 = st.button("몬스터")
val3 = st.button("씨범")

# 동작 # 출력 - HTML/CSS/JS 로 최종적으로 변환
if val1:
    st.image("./data/jjangu.png")
elif val2:
    st.image("./data/monster.png")
elif val3:
    st.image("./data/image.png")

# 출력 - HTML/CSS/JS 로 최종적으로 변환
# st.write(val1)

# . : 현재 경로  \ :WINDOWS 폴더 경로 구분 / : MAC/LINUX
# st.image("./data/jjanggu.png")

# # st.download_button("Download file", data)
# st.link_button("Go to gallery", url)
# st.page_link("app.py", label="Home")
# # st.data_editor("Edit data", data)
# st.checkbox("I agree")
# st.toggle("Enable")
# st.radio("Pick one", ["cats", "dogs"])
# st.selectbox("Pick one", ["cats", "dogs"])
# st.multiselect("Buy", ["milk", "apples", "potatoes"])
# st.slider("Pick a number", 0, 100)
# st.select_slider("Pick a size", ["S", "M", "L"])
# st.text_input("First name")
# st.number_input("Pick a number", 0, 10)
# st.text_area("Text to translate")
# st.date_input("Your birthday")
# st.time_input("Meeting time")
# st.file_uploader("Upload a CSV")
# st.camera_input("Take a picture")
# st.color_picker("Pick a color")

# # Use widgets' returned values in variables:
# # for i in range(int(st.number_input("Num:"))):
# #     foo()
# # if st.sidebar.selectbox("I:",["f"]) == "f":
# #     b()
# my_slider_val = st.slider("Quinn Mallory", 1, 88)
# st.write('slider_val')

# # Disable widgets to remove interactivity:
# st.slider("Pick a number", 0, 100, disabled=True)


# # 함수, 변수 등을 통해 입력받은 값을 출력하기 위한 값으로 제어


# # 출력화면 - HTML/CSS/JS 로 최종적으로 변환 
# st.write("Most objects") # df, err, func, keras!
# st.write(["st", "is <", 3]) # see *
# # st.write_stream(my_generator)
# # st.write_stream(my_llm_stream)

# st.text("Fixed width text")
# st.markdown("_Markdown_") # see *
# st.latex(r""" e^{i\pi} + 1 = 0 """)
# st.title("My title")
# st.header("My header")
# st.subheader("My sub")
# st.code("for i in range(8): foo()")
# st.html("<p>Hi!</p>")