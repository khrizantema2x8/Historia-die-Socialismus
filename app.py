import streamlit as st
from groq import Groq
import json
import base64

# Khởi tạo client với GROQ_API_KEY từ secrets.toml
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Load câu hỏi mẫu từ data.json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Custom font-face CSS (using NE-Light.otf)
def local_font_css():
    font_path = "NE-Light.otf"
    try:
        with open(font_path, "rb") as font_file:
            font_data = font_file.read()
            font_base64 = base64.b64encode(font_data).decode()
            return f"""
            <style>
            @font-face {{
                font-family: 'Neue Einstellung';
                src: url(data:font/otf;base64,{font_base64}) format('opentype');
                font-weight: 300;
                font-style: normal;
            }}
            /* Apply font to ALL elements */
            body, body *, [class*="st-"], [class*="css"], .stApp, div, p, h1, h2, h3, h4, h5, h6, span, button, input, textarea, select, option, label, a {{
                font-family: 'Neue Einstellung', 'Segoe UI', Arial, sans-serif !important;
            }}
            body, .stApp {{
                height: 100vh !important;
                min-height: 100vh !important;
                margin: 0 !important;
                padding: 20px !important;
                background-color: #edeced !important;
            }}
            .stApp > header {{
                display: none !important;
            }}
            /* Main two-column layout */
            .main-container {{
                display: flex !important;
                width: 100% !important;
                height: calc(100vh - 40px) !important;
                gap: 20px !important;
            }}
            /* Left column - T12 group */
            .left-column {{
                width: 30% !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: flex-start !important;
                padding-top: 50px !important;
            }}
            /* Right column - Response area */
            .right-column {{
                width: 70% !important;
                border: 3px solid #000 !important;
                padding: 20px !important;
                background: transparent !important;
                overflow: hidden !important;
                height: calc(100vh - 80px) !important;
                position: relative !important;
            }}
            
            /* Inner response box - curved dashed border */
            .inner-response-box {{
                width: 100% !important;
                height: 100% !important;
                border: 3px dashed #000 !important;
                border-radius: 15px !important;
                padding: 20px !important;
                background: transparent !important;
                overflow-y: auto !important;
                box-sizing: border-box !important;
            }}
            
            /* Input field styling with full dotted border */
            .question-input {{
                width: 100% !important;
                height: 48px !important;
                border: 3px dotted #504f4f !important;
                background: transparent !important;
                font-size: 1.2rem !important;
                color: #222 !important;
                outline: none !important;
                padding: 12px 48px 12px 12px !important;
                font-family: 'Neue Einstellung', 'Segoe UI', Arial, sans-serif !important;
                font-weight: 300 !important;
                transition: border-color 0.2s ease !important;
                resize: none !important;
                overflow: hidden !important;
                line-height: 1.5 !important;
                box-sizing: border-box !important;
                border-radius: 0 !important;
            }}
            
            /* Hide Streamlit input styling */
            div[data-testid="stTextInput"] > div > div > input {{
                border: 3px dotted #504f4f !important;
                border-radius: 0 !important;
                background: transparent !important;
                font-family: 'Neue Einstellung', 'Segoe UI', Arial, sans-serif !important;
                font-size: 1.2rem !important;
                color: #222 !important;
                padding: 12px 48px 12px 12px !important;
                height: 48px !important;
                box-sizing: border-box !important;
            }}
            
            div[data-testid="stTextInput"] > div > div > input:focus {{
                border: 3px solid #222 !important;
                outline: none !important;
                box-shadow: none !important;
            }}
            
            div[data-testid="stTextInput"] > div > div {{
                border: none !important;
                background: transparent !important;
            }}
            
            div[data-testid="stTextInput"] > div {{
                border: none !important;
                background: transparent !important;
            }}
            /* Title styling - left aligned */
            .title {{
                font-size: 3.2rem !important;
                font-weight: 300 !important;
                color: #222 !important;
                letter-spacing: -1px !important;
                text-align: left !important;
                font-family: 'Neue Einstellung', 'Segoe UI', Arial, sans-serif !important;
                line-height: 1.1 !important;
                margin: 0 0 32px 0 !important;
                padding: 0 !important;
                word-break: break-word !important;
            }}
            .title .break {{ 
                display: block !important;
            }}
            /* Input container */
            .input-container {{
                position: relative !important;
                margin-bottom: 16px !important;
                width: 100% !important;
            }}
            /* Send arrow button - positioned inside input field */
            .send-arrow {{
                position: absolute !important;
                right: 12px !important;
                top: 50% !important;
                transform: translateY(-50%) !important;
                width: 32px !important;
                height: 32px !important;
                background: none !important;
                border: none !important;
                cursor: pointer !important;
                padding: 0 !important;
                z-index: 2 !important;
                transition: transform 0.1s ease !important;
            }}
            .send-arrow:active {{
                transform: translateY(-50%) scale(0.95) !important;
            }}
            .send-arrow svg {{
                width: 32px !important;
                height: 32px !important;
                display: block !important;
            }}
            /* Instructions - left aligned */
            .instructions {{
                margin-top: 8px !important;
            }}
            .instruction {{
                font-size: 0.98rem !important;
                color: #aaa !important;
                margin-bottom: 4px !important;
                text-align: left !important;
                font-weight: 300 !important;
                user-select: none !important;
            }}
            /* Response area styling */
            .response-question {{
                font-size: 1.1rem !important;
                color: #222 !important;
                margin-bottom: 10px !important;
                font-weight: 400 !important;
            }}
            .response-separator {{
                border-bottom: 2px dashed #666 !important;
                margin: 15px 0 !important;
                height: 1px !important;
            }}
            .response-content {{
                font-size: 1rem !important;
                color: #222 !important;
                line-height: 1.6 !important;
                font-weight: 300 !important;
                white-space: pre-wrap !important;
            }}
            /* Settings link - top right */
            .settings-link {{
                position: fixed !important;
                top: 32px !important;
                right: 48px !important;
                font-size: 1rem !important;
                color: #222 !important;
                text-decoration: underline !important;
                background: none !important;
                border: none !important;
                cursor: pointer !important;
                z-index: 1000 !important;
                font-weight: 300 !important;
            }}
            /* Hide Streamlit elements */
            div[data-testid="stVerticalBlock"] > div:first-child {{
                padding: 0 !important;
            }}
            </style>
            """
    except Exception:
        return ""  # fallback if font not found

st.set_page_config(page_title="Chatbot Lịch Sử", page_icon="📜", layout="wide")
st.markdown(local_font_css(), unsafe_allow_html=True)

# Settings link
st.markdown('<a href="#" class="settings-link">Thiết lập</a>', unsafe_allow_html=True)

# Initialize session state for conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Left column - T12 group
col1, col2 = st.columns([0.3, 0.7], gap="medium")

with col1:
    st.markdown('<div class="left-column">', unsafe_allow_html=True)
    
    # Title - left aligned
    st.markdown(
        '<h1 class="title">hãy để lịch sử kể<span class="break"></span>bạn nghe</h1>',
        unsafe_allow_html=True
    )
    
    # Input container with form for submission
    with st.form(key="chat_form", clear_on_submit=True):
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        user_input = st.text_input(
            "",
            placeholder="nói đi đang nghe nè",
            key="questionBox",
            label_visibility="collapsed"
        )
        st.markdown(
            '<button type="submit" class="send-arrow"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="4" y1="16" x2="26" y2="16" stroke="#000" stroke-width="3" stroke-linecap="round"/><polyline points="20,10 26,16 20,22" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg></button>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Submit button (hidden)
        submitted = st.form_submit_button("Submit", type="primary")
    
    # Instructions
    st.markdown('<div class="instructions">', unsafe_allow_html=True)
    st.markdown('<div class="instruction">ấn Enter để chạy lệnh</div>', unsafe_allow_html=True)
    st.markdown('<div class="instruction">ấn Shift+Enter để xuống dòng</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Handle form submission
if submitted and user_input.strip():
    with st.spinner("⏳ Đang suy nghĩ..."):
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "Bạn là một trợ lý lịch sử Việt Nam, trả lời ngắn gọn, chính xác, thân thiện và dễ hiểu bằng tiếng Việt."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=600
            )
            ai_response = response.choices[0].message.content
            
            # Add to conversation history
            st.session_state.conversation.append({
                "question": user_input,
                "answer": ai_response
            })
        except Exception as e:
            st.session_state.conversation.append({
                "question": user_input,
                "answer": f"Xin lỗi, đã có lỗi xảy ra: {str(e)}"
            })

# Right column - Response area
with col2:
    st.markdown('<div class="right-column">', unsafe_allow_html=True)
    st.markdown('<div class="inner-response-box">', unsafe_allow_html=True)
    
    if st.session_state.conversation:
        # Show the latest conversation
        latest = st.session_state.conversation[-1]
        
        # Display question
        st.markdown(f'<div class="response-question">{latest["question"]}</div>', unsafe_allow_html=True)
        
        # Separator line
        st.markdown('<div class="response-separator"></div>', unsafe_allow_html=True)
        
        # Display answer
        st.markdown(f'<div class="response-content">{latest["answer"]}</div>', unsafe_allow_html=True)
    else:
        # Empty state
        st.markdown('<div class="response-content" style="color: #aaa; font-style: italic;">Hãy đặt câu hỏi để bắt đầu cuộc trò chuyện...</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close inner-response-box
    st.markdown('</div>', unsafe_allow_html=True)  # Close right-column

st.markdown('</div>', unsafe_allow_html=True)