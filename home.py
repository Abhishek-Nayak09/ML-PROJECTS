import streamlit as st

def main():
    st.title("Machine Learning Projects")
    st.write("Explore Our Machine Learning Model Showcase")

    model_details = {
        "Skin Disorder Prediction": {
            "Description": "Experience the intersection of AI and healthcare through our Skin Disorder Prediction project. Our cutting-edge machine learning models empower doctors to swiftly identify skin diseases, enabling prompt treatment and better patient care.",
            "Link": "https://skin-disorder-ml-project-abhi.streamlit.app/"
        },
        "Multi-Class Image Classification Model": {
            "Description": "Join us in building a greener future with our Multi-Class Image Classification project. Witness AI in action as we categorize and segment diverse types of bags, contributing to waste management and sustainable practices.",
            "Link": "https://bags-classification-ml-projects.streamlit.app/"
        },
        "Human Behavior Recognition": {
            "Description": "Delve into the world of computer vision with our Human Action Recognition project. Through the power of deep learning, we're deciphering human actions in real-time, propelling advancements in surveillance, robotics, and beyond.",
            "Link": "https://human-behavior-recognition-using-cnn-rnx6appynfv4z63ewppappbk.streamlit.app/"
        },
        "Movie Ratings Sentiment Analysis": {
            "Description": "Embark on a journey through cinematic emotions with our Sentiment Analysis model. Explore the AI-driven realm of movie reviews, where we analyze sentiments to enhance your movie-watching decisions.",
            "Link": "https://movie-ratings-sentiment-analysis-khzswamqze4a47u98rrnxb-abhi.streamlit.app/"
        }
    }

    st.sidebar.title("ML Projects")
    selected_project = st.sidebar.radio("Select a Project", list(model_details.keys()))

    st.sidebar.write("Click on a project in the sidebar to discover more.")

    st.markdown("---")

    st.write(f"## {selected_project}")
    st.write(model_details[selected_project]["Description"])
    st.write(f"**Link to Model:** [{selected_project}]({model_details[selected_project]['Link']})")

    st.markdown("---")

    st.write("### Other Projects")
    for project_name in model_details.keys():
        if project_name != selected_project:
            st.write(f"- [{project_name}]({model_details[project_name]['Link']})")


    st.markdown("---")

    st.subheader("Data Science Career Guidance")
    st.markdown("- [DataMites Team](https://datamites.com/)")

    st.subheader("External Resources:")
    st.write("The successful completion of this project was made possible by leveraging the following external resources:")
    st.markdown("- [Visual Studio Code](https://code.visualstudio.com/download)")
    st.markdown("- [Kaggle Data Science Community](https://www.kaggle.com/)")
    st.markdown("- [OpenAI ChatGPT](https://openai.com/)")
    st.markdown("- [GitHub](https://github.com/about)")
    st.markdown("- [streamlit](https://streamlit.io/cloud)")

    st.subheader("About creator:")
    st.markdown("- [LinkedIn](https://www.linkedin.com/in/abhishek-m-5495a91a3)")
    st.markdown("- [GitHub](https://github.com/Abhishek-Nayak09)")

if __name__ == "__main__":
    main()



