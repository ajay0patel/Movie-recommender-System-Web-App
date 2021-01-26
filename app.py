from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

df = pickle.load(open('dataframe', 'rb'))
similarity_score = pickle.load(open('simmilarity', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    input1 = [x for x in request.form.values()]

    movie_user_like = input1[0]

    #work on user input
    #change according to data set
    movie_user_like = movie_user_like.title()

    def get_index_from_title(title):
        return df[df.title==title]["index"].values[0]

    try:
        movie_index=get_index_from_title(movie_user_like)


        similer_movies = list(enumerate(similarity_score[movie_index]))
        sorted_similar_movies=sorted(similer_movies,key=lambda x:x[1],reverse=True)


        def get_title_from_index(index):
            return df[df.index==index]['title'].values[0]
        i=0
        output=[]
        for movie in sorted_similar_movies:
            output.append(get_title_from_index(movie[0]))
            if i>4:
                break
            else:
                i+=1

        return render_template('index.html', output_array=output )

    except:
        return render_template('index.html',out1='Sorry , No Movie Found',out2='Try With Different Movie Name')
        
    


app.run(debug=True)