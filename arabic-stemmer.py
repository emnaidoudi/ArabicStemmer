from nltk.stem import SnowballStemmer
#print(" ".join(SnowballStemmer.languages))

stemmer = SnowballStemmer("arabic")
print(stemmer.stem("فسميتموها"))