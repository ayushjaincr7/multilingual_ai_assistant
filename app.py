import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

# Custom Styling
st.set_page_config(page_title="Multilingual AI Assistant", page_icon="🤖")
st.markdown(
    """
    <style>
    .big-font { font-size:18px !important; font-weight: bold; }
    .stButton button { background-color: #4CAF50; color: white; }
    </style>
    """, 
    unsafe_allow_html=True
)

def main():
    st.title("🤖 Multilingual AI Assistant")
    st.markdown("### Ask questions in any language and get AI-powered responses with voice output!")
    
    # Button for voice input
    if st.button("🎙️ Speak Now"):
        with st.spinner("🔄 Listening..."):
            text = voice_input()
            st.success(f"📝 You said: **{text}**")

            with st.spinner("🤖 Generating response..."):
                response = llm_model_object(text)
                text_to_speech(response)

                # Read the generated speech file
                audio_file = open("speech.mp3", "rb")
                audio_bytes = audio_file.read()
                
                # Display response text
                st.markdown("### 📢 AI Response:")
                st.text_area(label="Response:", value=response, height=250)

                # Display audio controls
                st.audio(audio_bytes)
                
                # Download button
                st.download_button(
                    label="📥 Download Speech",
                    data=audio_bytes,
                    file_name="speech.mp3",
                    mime="audio/mp3"
                )

if __name__ == '__main__':
    main()