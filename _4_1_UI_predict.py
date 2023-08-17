import time
import random
import plotly.graph_objects as go
import streamlit as st
from _3_2_predict import run 

def feedback():
    st.title("Student's Feedback") 
    predict_label()

def predict_label(): # Bước nhập text và bắt đầu chạy
    global sentence
    sentence = st.text_input("Input **The Feedback** ( You can **Enter** the **Text Bar** or **Click** the **Button** 'Predict' to **Run** )")
    check_sentence = sentence.split()
    click = st.button("Predict")
    placeholder_error = st.empty()
    if click:
        if len(check_sentence) != 0:
            placeholder_error.empty()
            run_process()
        else:
            with st.spinner("Running..."):
                time.sleep(1)
            placeholder_error.error('The **Text Bar** is **Empty** ! Please **Input** !')

    elif len(check_sentence) != 0:
        placeholder_error.empty()
        with open('feedback.txt','a+',encoding='utf-8') as file:
            file.write(f"{sentence}\n")
        run_process()

    else:
        with st.spinner("Running..."):
            time.sleep(1)
        placeholder_error.error('The **Text Bar** is **Empty** ! Please **Input** !')

def run_process():  # Chạy thanh % progress, predict label, in ra cảm xúc và topic
    percent = 0
    first_run = True
    placeholder_progress = st.empty()
    placeholder_percent = st.empty()
    placeholder_predict_sentiment = st.empty()
    placeholder_predict_topic = st.empty()
    while percent <= 99:
        if first_run == True:
            time.sleep(1)
            placeholder_predict_sentiment.empty()
            placeholder_predict_topic.empty()
            placeholder_progress.empty()
            placeholder_percent.empty()
            first_run = False
        
        placeholder_percent.write(f"{percent}% Loading...")
        placeholder_progress.progress(percent)
        
        time.sleep(0.1)
        
        if percent >= 90 and percent < 100:
            percent = 100
            placeholder_progress.progress(percent)
            placeholder_percent.write(f"100% Loaded successfully.")
            # #(
            # random_topic()
            # while lecturer == training_program or lecturer == facility  or lecturer == other or training_program == facility or training_program == other or facility == other:
            #     random_topic()
            # #)
            time.sleep(0.5)
            placeholder_percent.empty()         
            values_sentiments = run(sentence)
            for standard in range(len(values_sentiments)-1):
                values_sentiments[standard] = round(values_sentiments[standard]*100,2)
            values_sentiments[2] = round(100 - values_sentiments[0] - values_sentiments[1],2)
            # sizes_topics = [lecturer, training_program, facility, other]
            
            col1, col2, col3, col4, col5 = st.columns(5)
            list_col = [col1, col2, col3, col4, col5]
            if max(values_sentiments) == values_sentiments[2]:
                placeholder_predict_sentiment.write(f" Sentiment: **Positive**")
                for i in list_col:
                    with i:
                        st.image('UI_positive.png')
                
            if max(values_sentiments) == values_sentiments[1]:
                placeholder_predict_sentiment.write(f" Sentiment: **Neutral**")
                for i in list_col:
                    with i:
                        st.image('UI_neutral.png')
            if max(values_sentiments) == values_sentiments[0]:
                placeholder_predict_sentiment.write(f" Sentiment: **Negative**")
                for i in list_col:
                    with i:
                        st.image('UI_negative.png')

            # if max(sizes_topics) == lecturer:
            #     placeholder_predict_topic.write(f" Topic: **Lecturer**")

            # if max(sizes_topics) == training_program:
            #     placeholder_predict_topic.write(f" Topic: **Training Program**")

            # if max(sizes_topics) == facility:
            #     placeholder_predict_topic.write(f" Topic: **Facility**")

            # if max(sizes_topics) == other:
            #     placeholder_predict_topic.write(f" Topic: **Other**")

            labels = ['Negative', 'Neutral', 'Positive']
            # Create the horizontal bar chart
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=values_sentiments,  # Use the values for the horizontal axis
                y= labels,  # Use the categories for the vertical axis
                orientation='h',  # Set the orientation to horizontal
                width=0.5,
                marker=dict(color=['red', 'yellow', 'lime']),
                    text=values_sentiments,
                    textposition='outside',
            ))
            # Customize the layout (optional)
            fig.update_layout(
                title='Predict Sentiment Chart',
                xaxis_title='Confidence',
                yaxis_title='Sentiments',
                paper_bgcolor = 'rgba(0, 0, 0, 0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(
                family='Arial, sans-serif',  # Set the font family
                size=11,  # Set the font size for the entire chart
                color='black'  # Set the font color
                )   
                )
            st.plotly_chart(fig, use_container_width=True)

            break
        else:      
            bonus_percent = random.randint(8,10)
            percent += bonus_percent
        
        if percent < 100:
            placeholder_percent.empty()