import math, collections

class LaplaceUnigramLanguageModel:

	def __init__(self, corpus):
		"""Initialize your data structures in the constructor."""
		self.unigrams = {}
		self.train(corpus)

	def train(self, corpus):
		""" Takes a corpus and trains your language model. 
		Compute any counts or other corpus statistics in this function.
		"""  
		for sentence in corpus.corpus:
			for datum in sentence.data:
				word = datum.word
				if word in self.unigrams:
					self.unigrams[word] = self.unigrams[word] + 1.0
				else:
					self.unigrams[word] = 1.0

	def score(self, sentence):
		""" Takes a list of strings as argument and returns the log-probability of the 
		sentence using your language model. Use whatever data you computed in train() here.
		"""
		score = 1.0
		vocabulary = len(self.unigrams) + 0.0
		for word in sentence:
			word_lookup = self.unigrams[word] if word in self.unigrams else 0.0
			probability = (word_lookup + 1.0) / (word_lookup + vocabulary)
			score += math.log(probability)
		return score
