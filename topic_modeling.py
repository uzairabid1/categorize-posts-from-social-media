import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


dataset_path = 'data/data_to_be_cleansed.csv'
output_file_path = 'backup_output/output.csv' 

df = pd.read_csv(dataset_path,encoding='ISO-8859-1')
df = df.dropna(subset=['title'])
print(df)

nltk.download('punkt')
nltk.download('stopwords')
def text_preprocessing(text):
    if isinstance(text, str):  
       
        tokens = word_tokenize(text)
        
 
        table = str.maketrans('', '', string.punctuation)
        tokens = [w.lower().translate(table) for w in tokens]
        
      
        tokens = [word for word in tokens if word.isalpha()]
        
        
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]
        
     
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(word) for word in tokens]
        
    
        preprocessed_text = ' '.join(tokens)
        
        return preprocessed_text
    else:
        return '' 


df['clean_title'] = df['title'].apply(text_preprocessing)

X = df['clean_title']
y = df['topic']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


vectorizer = TfidfVectorizer(max_features=5000)  
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

classifier = MultinomialNB()
classifier.fit(X_train_tfidf, y_train)

y_pred = classifier.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))




output_df = pd.read_csv(output_file_path)


rows_to_predict_type = output_df[output_df['Type of Post'] == 'Others'] 

for index, row in rows_to_predict_type.iterrows():
    post_text = row['Post Text']

    if isinstance(post_text, str):
        post_tokens = word_tokenize(post_text)
        post_tokens = [w.lower() for w in post_tokens if w.isalpha()]
        stop_words = set(stopwords.words('english'))
        post_tokens = [w for w in post_tokens if w not in stop_words]
        stemmer = PorterStemmer()
        post_tokens = [stemmer.stem(w) for w in post_tokens]
        preprocessed_post = ' '.join(post_tokens)
    else:
        preprocessed_post = ''

    post_tfidf = vectorizer.transform([preprocessed_post])

    predicted_probs = classifier.predict_proba(post_tfidf)[0] 
    predicted_type_of_post = classifier.classes_[predicted_probs.argmax()]  

    if predicted_probs.max() >= 0.2:
        output_df.at[index, 'Type of Post'] = predicted_type_of_post

output_df.to_csv(output_file_path, index=False)
