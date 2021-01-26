import pandas as pd
import pickle


df=pd.read_csv("movie_data.csv")
df['original_title']=df['original_title'].apply(lambda x: x.title())
df['title']=df['title'].apply(lambda x: x.title())

features=['keywords','cast','genres', 'director']

for feature in features:
    df[feature]=df[feature].fillna('')



def combine(row):
    return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']



df["combined_features"]=df.apply(combine,axis=1)


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])



from sklearn.metrics.pairwise import cosine_similarity
similarity_score = cosine_similarity(count_matrix)


filename = 'simmilarity'
outfile = open(filename,'wb')
pickle.dump(similarity_score,outfile)
outfile.close()



filename = 'dataframe'
outfile = open(filename,'wb')
pickle.dump(df,outfile)
outfile.close()










