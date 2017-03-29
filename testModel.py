import gensim

if __name__ == "__main__":
	one = raw_input("first : ")
	two = raw_input("second : ")
	M = gensim.models.Word2Vec.load("/home/alex/Documents/Wiki dump/wiki.en.word2vec.model")
	print M.wv.similarity(one, two)