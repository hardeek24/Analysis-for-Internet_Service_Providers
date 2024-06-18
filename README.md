Project Overview

This project aims to analyze unstructured and noisy social media data collected from platforms like Reddit to derive insights for leading internet service providers. The analysis involves lemmatization, topic filtering, text classification, and sentiment analysis using state-of-the-art NLP models like BERT and RoBERTa. The ultimate goal is to perform customer segmentation for targeted marketing and increase revenue. The project utilized transfer learning and has evolved from training on datasets like IMDB and YELP.

Steps to follow:
1. Clone the repository
   
2. Create a virutal environment
   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Intall the reuqirmements using
    pip install -r requirements.txt

4.Run the praw.py script for scrapping the data

5. Run LDA.py for initial preprocessing

6. Run the Sentiment AnalysisFullSequence.pynb file which contains all the data preprocessing and model tunning and segmentation commands.

7. Follow the further steps to store the data in pincone vector db from Vectordb file

8. To deploy it futher on docker follow the steps in docker file .

Enjoy! Have fun
