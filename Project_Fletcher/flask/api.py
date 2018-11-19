import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import LatentDirichletAllocation

lda = pickle.load(open('./pkl_files/lda.pkl', 'rb'))
cv  = pickle.load(open('./pkl_files/vectorizer.pkl', 'rb'))
X_cv_lda  = pickle.load(open('./pkl_files/X_cv_lda.pkl', 'rb'))
df = pickle.load(open('./pkl_files/df.pkl', 'rb'))

def cosine_sim(transformed_resume):
    similarities = []
    for job in X_cv_lda:
        cs = cosine_similarity(job.reshape(-1,1).T, transformed_resume.reshape(-1,1).T)
        similarities.append(cs[0][0])
    return similarities

def compare_resume_lda(resume_as_txt):
    string_resume = str(resume_as_txt)
    list_resume=[]
    list_resume.append(string_resume)
    transformed_resume = lda.transform(cv.transform(list_resume))
    similarities_to_my_resume = cosine_sim(transformed_resume)
    df_you = df
    df_you['similarity'] = similarities_to_my_resume
    return df_you

def return_rec(resume_as_txt, company='', location='', job_title=''):
    df_ranked = compare_resume_lda(resume_as_txt)
    if company == "":
        df_company = df_ranked
    else:
        df_company = df_ranked[df_ranked['Company'].str.contains(company)]
    if location == "":
        df_ranked_filtered = df_company
    else:
        df_ranked_filtered = df_company[df_company['Location'].str.contains(location)]
    if job_title == "":
        df_1 = df_ranked_filtered
    else:
        df_1 = df_ranked_filtered[df_ranked_filtered['Job_title'].str.contains(job_title)]
    top_match = df_ranked_filtered.sort_values('similarity', ascending=False).head(1)
    return top_match['Link'].iloc[0]

location = 'Seattle, WA'
company = 'Amazon'
example = 'Python Sql Data Science Machine Learning'

if __name__ == '__main__':
    print(return_rec(location, company, example))