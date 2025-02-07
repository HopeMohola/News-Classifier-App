# News Classifier App

# What is Streamlit?
Streamlit is a framework that acts as a web server with dynamic visuals, multiple responsive pages, and robust deployment of your models.

The easiest way for data scientists and machine learning engineers to create beautiful, performant apps in only a few hours! All in pure Python. All for free.

It’s a simple and powerful app model that lets you build rich UIs incredibly quickly.

Streamlit takes away much of the background work needed in order to get a platform which can deploy your models to clients and end users. Meaning that you get to focus on the important stuff (related to the data), and can largely ignore the rest. This will allow you to become a lot more productive.

# Description of files
For this repository, we are only concerned with a single file:

# File Name	Description
app.py	Streamlit application definition.
6.1 Running the Streamlit web app on your local machine
As a first step to becoming familiar with our web app's functioning, we recommend setting up a running instance on your own local machine. To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

Ensure that you have the prerequisite Python libraries installed on your local machine:
pip install -U streamlit numpy pandas scikit-learn
Navigate to the base of your repo where your base_app.py is stored, and start the Streamlit app.
cd 2401FTDS_Classification_Project/Streamlit/
streamlit run base_app.py
If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.43.41:8501
You should also be automatically directed to the base page of your web app.


