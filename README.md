# 🧠 Duplicate Question Detection App  
A Streamlit-based machine learning web application that predicts whether two questions are duplicates of each other.  
Built using NLP techniques, handcrafted similarity features, Bag-of-Words encoding, and an ML classification model trained on the **Quora Question Pairs dataset**.

---

## 🚀 Live Demo  
🔗 **Try the App:** _Add your Streamlit URL here after deployment_

---

## 📌 Project Overview  
This project identifies whether two given questions have the same meaning.  
It mirrors real-world scenarios like:

- Duplicate question detection on Quora  
- FAQ deduplication  
- Support ticket similarity checking  
- Chatbot question normalization  

The app extracts **linguistic, semantic, fuzzy, and token-level features** from the input text and feeds them into a trained model to predict if the questions are duplicates.

---

## 🧰 Tech Stack  
- **Python**
- **Streamlit** (for UI)
- **Scikit-learn**
- **BeautifulSoup**
- **FuzzyWuzzy**
- **Distance** (for longest common substring)
- **NumPy / pickle**

---

## 📀 Machine Learning Workflow  

### ### **1. Preprocessing**
- Lowercasing  
- Removing HTML tags  
- Removing punctuation  
- Expanding contractions (e.g., *"can't" → "cannot"*)  
- Handling currency, numbers, math expressions  
- Stopword removal  

### **2. Feature Engineering**

#### 🔹 Basic Features
- Sentence length  
- Number of words  
- Total/common word count  

#### 🔹 Token-Based Features  
Extracted using `test_fetch_token_features()`:
- Ratios of common words  
- Ratio of common stopwords  
- First/last word match indicators  
- Token similarity scores  

#### 🔹 Length-Based Features  
- Absolute difference in question lengths  
- Longest Common Substring (LCS) ratio  

#### 🔹 Fuzzy String Matching  
Using `FuzzyWuzzy` scores:
- `QRatio`
- `partial_ratio`
- `token_sort_ratio`
- `token_set_ratio`

#### 🔹 Bag-of-Words Features
Using a trained CountVectorizer (`cv.pkl`), we generate:
- `q1_bow`
- `q2_bow`

---


