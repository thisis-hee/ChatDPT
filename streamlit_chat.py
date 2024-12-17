import streamlit as st
from streamlit_llm import get_ai_response

# 페이지 설정: 새로운 아이콘으로 변경
st.set_page_config(
    page_title="동국대학교 챗봇 - Chat DPT",
    page_icon="https://yt3.googleusercontent.com/SlLCncyFzGYTyA08zX7lWAzrFWQ3nx9SshKnc7ZqQda4Np0TomWsvMT7V9yswQ49h39GdUUqRg=s900-c-k-c0x00ffffff-no-rj"  # 원하는 이모지나 이미지 URL로 변경
)

# 외부 이미지 URL 사용
image_url = "https://github.com/jssoleey/prac/blob/main/dongguk.png?raw=true"  # 동국대학교 로고 이미지 예시

# 외부 이미지 표시
st.image(image_url, use_column_width=True)

# 제목 변경
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <img src="https://yt3.googleusercontent.com/SlLCncyFzGYTyA08zX7lWAzrFWQ3nx9SshKnc7ZqQda4Np0TomWsvMT7V9yswQ49h39GdUUqRg=s900-c-k-c0x00ffffff-no-rj" alt="Title Image" style="height:50px; margin-right:10px;">
        <h1 style="margin: 0;">Chat DPT</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.caption("동국대에 관련된 모든 것을 답해드립니다!")

# 나머지 문장들을 작게 표시하고 줄 간격을 조절하기 위해 CSS 스타일 적용
st.markdown(
    """
    <style>
    .small-text {
        font-size: 9px; /* 원하는 크기로 조절 가능 */
        color: gray; /* 텍스트 색상 조절 가능 */
        line-height: 1.2; /* 줄 간격 조절 */
        margin-top: 2px; /* 문장 사이의 간격 최소화 */
        margin-bottom: 2px; /* 문장 사이의 간격 최소화 */
    }

    /* 모든 소제목의 폰트 크기 조절 */
    .section-title {
        font-size: 12px !important; /* 폰트 크기를 줄임 */
        font-weight: bold !important; /* 폰트 굵기 유지 */
        color: #333; /* 폰트 색상 */
        margin-bottom: 4px; /* 소제목과 내용 간의 간격 조절 */
    }

    </style>
    """,
    unsafe_allow_html=True
)

# 줄 간격을 최소화하여 문장 표시
st.markdown('<p class="small-text">단어가 아닌 대화형 문장으로 질문해주세요.</p>', unsafe_allow_html=True)
st.markdown('<p class="small-text">저는 우리 학교의 공식 홈페이지를 실시간으로 학습해 답변하고 있어요.</p>', unsafe_allow_html=True)
st.markdown('<p class="small-text">제가 제공하는 정보는 부정확할 수 있어요. 정확한 정보는 답변의 출처 및 해당 페이지 링크를 통해 직접 확인하세요.</p>', unsafe_allow_html=True)
st.markdown('<p class="small-text">저는 개인정보를 수집하지 않습니다.</p>', unsafe_allow_html=True)

# 세션 상태 초기화
if 'message_list' not in st.session_state:
    st.session_state.message_list = []

# 사용자와 AI의 아바타 설정
user_avatar = "https://github.com/jssoleey/prac/blob/main/aaaa.png?raw=true"
ai_avatar = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsGUwV1HhDWzRFK5QCYGC-7FmrWkCfJA-0Y05AlpVn7GRItix1mzkPD-9k9cP5_naDTLU&usqp=CAU"

# CSS 스타일 추가
st.markdown(
    """
    <style>
    .user-message {
        background-color: #FFA500; /* 주황색 배경 */
        color: white; /* 흰색 텍스트 */
        padding: 10px;
        border-radius: 10px;
        max-width: 70%;
        text-align: left; /* 텍스트 정렬 */
        word-wrap: break-word; /* 긴 단어 줄바꿈 */
    }
    .ai-message {
        background-color: #f0f0f0; /* 회색 배경 */
        color: black; /* 검정색 텍스트 */
        padding: 10px;
        border-radius: 10px;
        max-width: 70%;
        text-align: left; /* 텍스트 정렬 */
        word-wrap: break-word; /* 긴 단어 줄바꿈 */
    }
    .message-container {
        display: flex;
        align-items: flex-start;
        margin-bottom: 10px;
    }
    .message-container.user {
        justify-content: flex-end; /* 사용자 메시지를 오른쪽 정렬 */
    }
    .message-container.ai {
        justify-content: flex-start; /* AI 메시지를 왼쪽 정렬 */
    }
    .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin: 0 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def display_message(role, content, avatar_url):
    """
    역할(role)에 따라 메시지를 좌측 또는 우측에 표시하고 스타일을 적용합니다.
    """
    if role == "user":
        alignment = "user"
        message_class = "user-message"
        avatar_html = f'<img src="{avatar_url}" class="avatar">'  # 아바타 이미지 HTML
        message_html = f'<div class="{message_class}">{content}</div>'
        display_html = f"""
        <div class="message-container {alignment}">
            {message_html}
            {avatar_html}
        </div>
        """
    else:
        alignment = "ai"
        message_class = "ai-message"
        avatar_html = f'<img src="{avatar_url}" class="avatar">'  # 아바타 이미지 HTML
        message_html = f'<div class="{message_class}">{content}</div>'
        display_html = f"""
        <div class="message-container {alignment}">
            {avatar_html}
            {message_html}
        </div>
        """

    # HTML 표시
    st.markdown(display_html, unsafe_allow_html=True)

# AI의 환영 메시지
welcome_message = """
GPT-4 기반의 동국대학교 챗봇 ‘Chat DPT’입니다.😄 
우리 대학에 대해 궁금한 사항이 있으시다고요?
저는 질문이 구체적일수록 더 잘 대답해요! 😉
무엇이든 물어보세요. 제가 안내해드릴게요!
📣 한국어, 영어, 중국어, 일본어로 질문하시면 같은 언어로 답변해 드려요.
"""

# 처음 대화 시작 시 환영 메시지 표시
if 'first_time' not in st.session_state:
    st.session_state.first_time = True
    # 환영 메시지를 첫 대화에 추가
    st.session_state.message_list.append({"role": "ai", "content": welcome_message})

# 기존 메시지 표시
for message in st.session_state.message_list:
    role = message["role"]
    content = message["content"]
    avatar = user_avatar if role == "user" else ai_avatar
    display_message(role, content, avatar)

# 사용자 입력 처리
if user_question := st.chat_input(placeholder="동국대에 관련된 궁금한 내용들을 말씀해주세요!"):
    # 사용자 메시지 추가 및 표시
    st.session_state.message_list.append({"role": "user", "content": user_question})
    display_message("user", user_question, user_avatar)
    
    # AI 응답 생성 및 표시
    response_placeholder = st.empty()  # AI 응답을 표시할 자리 확보
    with st.spinner("답변을 생성하는 중입니다"):
        ai_response = get_ai_response(user_question)

        # 제너레이터를 이용해 실시간으로 타이핑 효과 구현
        ai_response_text = ""
        for chunk in ai_response:  # 제너레이터의 각 부분을 받아와서
            ai_response_text += chunk  # 응답 텍스트에 추가
            response_placeholder.markdown(  # 현재까지의 응답을 업데이트
                f'<div class="message-container ai"><img src="{ai_avatar}" class="avatar"><div class="ai-message">{ai_response_text}</div></div>', 
                unsafe_allow_html=True
            )
        
        if ai_response_text:  # 응답이 정상적으로 생성되었을 경우
            st.session_state.message_list.append({"role": "ai", "content": ai_response_text})