from setuptools import find_packages, setup

setup(
  name="multilingual assistant",
  version="1.0.1",
  author="ayush_jain",
  author_email="ja7ayush@gmail.com",
  packages=find_packages(),
  install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)