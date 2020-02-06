#-*- coding:utf-8 -*-
import sys
import nltk
from statistics import mean
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import operator

# 처음 실행할 때는 다운로드 필요
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

def tops(bag_of_words, n=None): # 빈도순 최고 n순위 
	term_list = list(vectorizer.vocabulary_.keys()) 
	sum_words = bag_of_words.sum(axis=0) # 코퍼스 내 용어별 빈도
	top_words = []
	top_sums = []
	i = 0
	for i in range(len(term_list)):
		top_words.append(term_list[i])
		top_sums.append(sum_words[0,i])
	pairing = dict(map(lambda x,y:[x,y], top_words, top_sums)) # 용어와 빈도를 사전으로 묶기
	reverse_sorted = sorted(pairing.items(), key=lambda x: x[1], reverse=True) # 빈도순 정렬
	return reverse_sorted[:n] # 최빈 n 순위까지의 용어 반환

if __name__ == "__main__":
	file_name = "twitter_stream2.txt" # 특수기호 거르는 전처리를 끝낸 파일
	docs = []
	with open(file_name, "r") as f:
		for line in f.read().splitlines(): # 한 줄을 하나의 문헌으로 취급
			docs.append(line) # 문헌들의 목록을 만듦
	print("Total number of documents is " + str(len(docs)) + ".") # 문헌의 개수(문헌 목록의 길이)를 확인
	corpus = []
	parsed = []
	for document in docs:
		splits = document.split() # 띄어쓰기 파싱
		parsed.append(len(splits))
		tokendoc = nltk.word_tokenize(' '.join(document.split()).lower()) # 소문자화, 토크나이징
		posdoc = nltk.pos_tag(tokendoc) # 품사 태깅
		ndoc = [word for word,pos in posdoc if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')] # 명사 추출
		wordnet_lemmatizer = WordNetLemmatizer() 
		ldoc = [wordnet_lemmatizer.lemmatize(nouns) for nouns in ndoc] # 단어 원형 복원
		ldocs = []
		ldocs.append(ldoc)
		doc = " ".join(ldoc) # 문헌별로 단어들을 하나의 문자열로 이어줌. 같은 단어가 여러 번 나올 수 있음.
		corpus.append(doc) # vectorizer가 읽을 수 있는 형태로 문자열들의 목록으로 다시 이어줌.
	print("Mean of numbers of words per document: "+str(mean(parsed))) # 평균 문헌 당 어절 수
	vectorizer = CountVectorizer(stop_words='english') # 영어 불용어 처리
	bag_of_words = vectorizer.fit_transform(corpus)
	dtmatrix = bag_of_words.toarray() # 빈도수로 문헌 용어 행렬 만들기
	
	n = 100 # 출력할 순위 제한
	with open("tfidf_desc.txt", "a", encoding='utf-8') as f: # 출력 파일
		topfq = tops(bag_of_words, n)
		f.write("빈도순 최고 "+str(n)+"위 용어")
		f.write("\n")
		for key, value in topfq:	
			f.write(str(key)+"\t"+str(value))
			f.write("\n")	
