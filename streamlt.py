import streamlit as st
from audiorecorder import audiorecorder
import demotest

st.title("speaker identifiyer")
diarising=False
placeholder = st.empty()
logging_speaker = st.empty()
# logging_textbox.write(demotest.diarise())

col1, col2 = st.columns([1,1])
def test():
    # with placeholder2.container():
        # placeholder2.empty()
    placeholder.empty()
    global diarising
    diarising=True
    while diarising:
        logging_speaker.write(demotest.diarise())
    # demotest.diarise_loop()
    # st.write("pressed")
def record():
    global diarising
    diarising=False

    # audiorecorder(start_prompt="Start recording", stop_prompt="Stop recording", pause_prompt="", show_visualizer=True, key=None)

    # with placeholder.container():
        
    #     audio = audiorecorder("Add new recording", "Click to stop recording")
    #     if len(audio) > 0:
    #         # To play audio in frontend:
            
    #         st.audio(audio.export().read())  

    #         # To save audio to a file, use pydub export method:
            

    #         # To get audio properties, use pydub AudioSegment properties:
    #         st.write(f"Duration: {audio.duration_seconds} seconds")
            
    #         title = st.text_input("Name", "name")
    #         if st.button('add') and title != "name":
    #             audio.export(f"{title}.wav", format="wav")
    #             st.toast(f"Saved {title}.wav")
    #             placeholder.empty()
    #             # st.write(f"Saved {title}.wav")
    #         # audio.export("audio.wav", format="wav")
with col1:
    st.button("Start identifiyer", on_click=test)
        # st.write("pressed")
        # st.write(demotest.diarise())
with col2:
    st.button("Add new recording", on_click=record)
    





# st.write(f"Saved .wav")


