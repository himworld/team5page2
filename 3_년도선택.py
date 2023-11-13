import streamlit as st

def main():
    st.title('껄무새 탈출 작전')

    if st.button('1980년대'):
        st.write("1980년대 페이지입니다.")

    if st.button('1990년대'):
        st.write("1990년대 페이지입니다.")

    if st.button('IMF시대'):
        st.write("IMF시대 페이지입니다.")

    if st.button('2000년대'):
        st.write("2000년대 페이지입니다.")

if __name__ == '__main__':
    main()

# 사이드바에 버튼 생성
if st.sidebar.button("다른 페이지로 이동"):
    # 다른 Streamlit 웹 페이지의 URL
    new_page_url = "https://team5page2.streamlit.app/"

    # 페이지를 새 URL로 리다이렉트
    st.experimental_rerun()
