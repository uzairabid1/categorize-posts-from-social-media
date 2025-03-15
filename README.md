# Post Categorization and Analysis

## Overview
This project focuses on **web scraping, natural language processing (NLP), and text classification** to analyze and categorize online posts related to job discussions, workplace experiences, and personal challenges. By leveraging automated data extraction and machine learning techniques, the system predicts the category of new posts based on past data, providing insights into emerging trends.

## Features
- **Web Scraping with Selenium**: Extracts posts from online sources, capturing job-related discussions and personal experiences.
- **Text Preprocessing using NLTK**: Tokenization, stopword removal, stemming, and normalization of text data.
- **TF-IDF Vectorization**: Converts processed text into numerical features for machine learning.
- **Multinomial Naïve Bayes Classification**: Predicts the topic of posts based on training data.
- **Regex-based Extraction**: Identifies salary-related information (TC values) and timestamps.
- **Rule-Based Classification**: Uses predefined keyword lists to assign categories such as immigration, layoffs, mental health, and toxic workplace environments.
- **Data Storage with Pandas**: Organizes extracted and processed data into structured CSV files for further analysis.
- **Data Visualization with PowerBI**: To visualize better I also used PowerBI to then graphs for the output data.

## Implementation Details
### 1. Data Collection
- **Selenium WebDriver** automates the extraction of posts.
- Extracted text is cleaned and stored in a structured format.

### 2. Text Preprocessing
- **NLTK** is used for:
  - Tokenization
  - Stopword removal
  - Stemming (using PorterStemmer)
- The cleaned text is stored in a new column.

### 3. Feature Engineering
- **TF-IDF Vectorization** transforms textual data into numerical vectors with a max feature limit of 5000.

### 4. Classification Model
- **Multinomial Naïve Bayes (MNB)** is trained on labeled post data.
- The model predicts post categories with a confidence threshold.
- Performance is evaluated using **accuracy scores** and **classification reports**.

### 5. Additional Categorization
- **Regular Expressions (regex)** extract relevant numerical and date information.
- A **rule-based keyword matching system** categorizes posts into predefined topics when ML predictions are uncertain.

### 6. Data Storage and Export
- **Pandas** is used to store and update the processed posts in CSV format.
- A backup system ensures safe updates using temporary files to prevent data corruption.

## Usage
1. Run the web scraper to collect posts.
2. Preprocess the text using the NLP pipeline.
3. Train and evaluate the Naïve Bayes classifier.
4. Predict categories for new posts.
5. Export structured data for further analysis.

## Technologies Used
- **Python** (Core programming language)
- **Selenium** (Web scraping)
- **NLTK** (Text preprocessing)
- **Scikit-learn** (ML model and TF-IDF vectorization)
- **Pandas** (Data handling)
- **Regex** (Pattern matching for data extraction)
- **Power BI** (For Data Visualization)

## Future Improvements
- Implement deep learning models (e.g., **LSTMs or Transformers**) for improved classification accuracy.
- Expand the dataset to include a wider variety of post categories.
- Develop a web-based interface for real-time post categorization.

## Dashboard
![image](https://github.com/user-attachments/assets/7741e094-b111-40c2-923d-5ff076ccf012)

## Conclusion
This project demonstrates an end-to-end pipeline for extracting, processing, and categorizing textual data. By combining **rule-based heuristics** and **machine learning models**, it provides a structured approach to analyzing online discussions, offering valuable insights into workplace and personal experiences.
