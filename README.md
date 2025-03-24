# Social Media Data Analysis for ISPs

![starlink](https://github.com/hardeek24/StarLink-Project/assets/162917115/3fc5f003-122e-4870-89fe-dcbfbe0e2b13)


## Project Overview

This project showcases a BERT-based recommendation system developed to analyze and segment over 50K social media posts for customer profiling. By leveraging advanced NLP techniques, the system achieved 92.7% accuracy in predicting user interests, enabling precise customer segmentation.

## Key Features:
Customer Segmentation: Analyzed and categorized over 50,000 social media posts to identify key customer segments based on user-generated content.

Model Optimization: Reduced model inference latency from 250ms to 35ms using model distillation and TorchScript, improving real-time recommendation performance.

Transfer Learning with RoBERTa: Fine-tuned RoBERTa on a dataset of over 100 million tokens, optimizing its language understanding and enhancing recommendation accuracy.

Efficient Deployment: Deployed a lightweight version of the model on AWS EC2 with auto-scaling, ensuring high availability and dynamic resource allocation during traffic fluctuations.

## Highlights:
Trained on 100M+ tokens with 355M parameters (RoBERTa model) for robust language understanding.

Achieved 92.7% recommendation accuracy, significantly improving customer engagement.

Implemented model distillation to optimize deployment without compromising performance.

This repository includes the complete code for data preprocessing, model training, optimization, and cloud deployment. The system is designed for efficient scaling and seamless integration with existing infrastructure.

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
  


