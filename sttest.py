import streamlit as st
from audiorecorder import audiorecorder
import demotest
from demotest import add_record

# st.title("speaker identifiyer")
# diarising=False
# placeholder = st.empty()
# logging_speaker = st.empty()
# # logging_textbox.write(demotest.diarise())

# col1, col2 = st.columns([1,1])
# def test():
#     # with placeholder2.container():
#         # placeholder2.empty()
#     placeholder.empty()
#     global diarising
#     diarising=True
#     while diarising:
#         logging_speaker.write(demotest.diarise())
#     # demotest.diarise_loop()
#     # st.write("pressed")
# def record():
#     global diarising
#     diarising=False

#     # audiorecorder(start_prompt="Start recording", stop_prompt="Stop recording", pause_prompt="", show_visualizer=True, key=None)

#     # with placeholder.container():
        
#     #     audio = audiorecorder("Add new recording", "Click to stop recording")
#     #     if len(audio) > 0:
#     #         # To play audio in frontend:
            
#     #         st.audio(audio.export().read())  

#     #         # To save audio to a file, use pydub export method:
            

#     #         # To get audio properties, use pydub AudioSegment properties:
#     #         st.write(f"Duration: {audio.duration_seconds} seconds")
            
#     #         title = st.text_input("Name", "name")
#     #         if st.button('add') and title != "name":
#     #             audio.export(f"{title}.wav", format="wav")
#     #             st.toast(f"Saved {title}.wav")
#     #             placeholder.empty()
#     #             # st.write(f"Saved {title}.wav")
#     #         # audio.export("audio.wav", format="wav")
# with col1:
#     st.button("Start identifiyer", on_click=test)
#         # st.write("pressed")
#         # st.write(demotest.diarise())
# with col2:
#     st.button("Add new recording", on_click=record)
    





# # st.write(f"Saved .wav")



# import streamlit as st
# import pandas as pd

# # if 'name' not in st.session_state:
# #     st.session_state['name'] = 'John Doe'

# # st.header(st.session_state['name'])
# # jane = st.button('Jane')
# # if jane:
# #     jane = st.button('john')
# #     st.session_state['name'] = 'Jane Doe'

# # # if st.button('John'):
# # #     st.session_state['name'] = 'John Doe'

# # st.header(st.session_state['name'])

# st.toggle("label", value=False, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False, label_visibility="visible")

# if st.session_state.get('clear'):
#     st.session_state['name'] = ''
# if st.session_state.get('streamlit'):
#     st.session_state['name'] = 'Streamlit'

# st.text_input('Name', key='name')

# st.button('Clear name', key='clear')
# st.button('Streamlit!', key='streamlit')
file_name = 'name'
audio = None
placeholder = st.empty()
train_directory = r"train_data/"

def call_record():
    record()
if 'start' not in st.session_state:
    st.session_state['start'] = 'start'

if 'name' not in st.session_state:
    st.session_state['name'] = 'name'

if 'recording' not in st.session_state:
    st.session_state['recording'] = 'true'
if 'placeholder' not in st.session_state:
    st.session_state.placeholder = ''


diarising = False

def change_button():
    # global st.session_state['start']
    # print(st.session_state['start'])
    if st.session_state['start'] == 'start':
        st.session_state['start'] = 'stop'
        # st.session_state['recording'] = 'false'
        # print(st.session_state['start'])
    else:
        st.session_state['start'] = 'start'
        # st.session_state['recording'] = 'true'
        # record()
    print("start", st.session_state['start'])

def add_name(audio, name):
    print("adding name")
    # st.session_state['recording'] = 'true'
    # # if file_name != "name":
    # title = st.session_state['name']
    # print("saved")
    # # st.session_state['recording'] = 'true'
    audio.export(f"{train_directory+name}.wav", format="wav")
    add_record(name)
    st.toast(f"Saved {name}.wav")
    placeholder.empty()
    # st.session_state['name'] = 'name'
    print("saved", name)

def record(audio):
    global diarising
    diarising=False
    print('adding record')
    # audiorecorder(start_prompt="Start recording", stop_prompt="Stop recording", pause_prompt="", show_visualizer=True, key=None)

    with placeholder.container():
        global file_name
        
        if len(audio) > 0:

            st.audio(audio.export().read())  

            st.write(f"Duration: {audio.duration_seconds} seconds")
            # file_name = st.text_input("Name", "name", key='name')
            # print(file_name)
            # # if st.button('add', on_click=add_name, key='stop recording'):
            # if st.session_state['name'] != 'name':
            #     print("sfg")
            #     add_name(st.session_state['name'])
            text_input = st.text_input(
                "Enter some text 👇",
                # label_visibility=st.session_state.visibility,
                # disabled=st.session_state.disabled,
                placeholder=st.session_state.placeholder,
                key='name'
            )
            
            st.button('add', on_click=add_name, key='stop recording')
                # print("sfg")
                # add_name(st.session_state['name'])

            if text_input:
                print("fveg")
                st.write("You entered: ", text_input)
            

def diarise():
    change_button()


# col1, col2 = st.columns([1,1])
# with col1:
#     # st.button("Start identifiyer", on_click=test)
#         # st.write("pressed")
#         # st.write(demotest.diarise())
#         st.button(st.session_state['start'], on_click=diarise)
# with col2:
#     # st.button("Add new recording", on_click=record)
    # audio = audiorecorder("Add new recording", "Stop recording",pause_prompt="", show_visualizer=True, key='start recording')



audio = audiorecorder("Add new recording", "Stop recording",pause_prompt="", show_visualizer=True, key='rec_button')
st.button(st.session_state['start'], on_click=diarise)

logging_speaker = st.empty()

if st.session_state.get('rec_button'):
    print("file name:",st.session_state['name'])
    print("clicked", st.session_state['recording'])
    if st.session_state['recording'] == 'true':
        print(st.session_state['recording'])
        print("got name")
        record(audio)
    st.session_state['recording'] = 'false'


if st.session_state.get('name'):
    print("file name1:",st.session_state['name'])
    if st.session_state['name'] != 'name':
        add_name(audio, st.session_state['name'])


if st.session_state.get('stop recording'):
    print("stopped recording")
    st.session_state['recording'] = 'true'
# # Store the initial value of widgets in session state
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

# col1, col2 = st.columns(2)

# with col1:
#     st.checkbox("Disable text input widget", key="disabled")
#     st.radio(
#         "Set text input label visibility 👉",
#         key="visibility",
#         options=["visible", "hidden", "collapsed"],
#     )
#     st.text_input(
#         "Placeholder for the other text input widget",
#         "This is a placeholder",
#         key="placeholder",
#     )

# with col2:
#     text_input = st.text_input(
#         "Enter some text 👇",
#         label_visibility=st.session_state.visibility,
#         disabled=st.session_state.disabled,
#         placeholder=st.session_state.placeholder,
#     )

#     if text_input:
#         st.write("You entered: ", text_input)

while st.session_state['start'] == 'stop':
    logging_speaker.write(demotest.diarise())