# Social Media Data Analysis for ISPs

## Project Overview

This project analyzes unstructured and noisy social media data from platforms like Reddit to derive insights for leading internet service providers (ISPs). The analysis process includes lemmatization, topic filtering, text classification, and sentiment analysis using advanced NLP models like BERT and RoBERTa. The ultimate goal is to perform customer segmentation for targeted marketing to increase revenue. This project utilizes transfer learning techniques, building upon training datasets like IMDB and Yelp.

## Project Summary

In this project, we leverage the power of Natural Language Processing (NLP) and advanced machine learning techniques to analyze social media data and extract actionable insights for ISPs. The data is collected from Reddit, preprocessed through various NLP techniques, and analyzed using state-of-the-art models like BERT and RoBERTa. We perform sentiment analysis and topic modeling to understand customer sentiments and preferences. The insights are then used to segment customers for targeted marketing, ultimately aiming to enhance customer engagement and drive revenue growth. The project also includes a robust end-to-end pipeline for data ingestion, processing, analysis, and deployment, ensuring a scalable and efficient solution.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Summary](#project-summary)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Data Scraping:** Collects data from Reddit using the PRAW library.
- **Text Preprocessing:** Involves lemmatization, topic filtering, and tokenization.
- **Sentiment Analysis:** Uses BERT and RoBERTa models for sentiment analysis.
- **Customer Segmentation:** Analyzes data to segment customers for targeted marketing.
- **Deployment:** Instructions for deploying the solution using Docker.

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.8+
- Git
- Docker (optional, for deployment)
- Access to the internet for installing packages and scraping data

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/social-media-analysis-isp.git
    cd social-media-analysis-isp
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Follow these steps to run the analysis:

1. **Scrape Data from Reddit:**

    ```bash
    python scripts/praw.py
    ```

2. **Initial Preprocessing:**

    ```bash
    python scripts/LDA.py
    ```

3. **Run Sentiment Analysis and Customer Segmentation:**

    Open and run all cells in `notebooks/Sentiment_AnalysisFullSequence.ipynb` using Jupyter Notebook or JupyterLab.

4. **Store Data in Pinecone Vector DB:**

    ```bash
    python scripts/Vectordb.py
    ```

5. **Deploy Using Docker:**

    Follow the steps provided in the `Dockerfile` to build and run the Docker container.


## Future Work

- **Expand Data Sources:** Incorporate data from other social media platforms.
- **Enhanced Modeling:** Experiment with more advanced models and fine-tuning strategies.
- **Real-Time Analysis:** Implement real-time data streaming and analysis.
- **User Interface:** Develop a user interface for visualizing results.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, feel free to open an issue or contact me at:

- **Email:** agarwaalh@asu.edu
  


