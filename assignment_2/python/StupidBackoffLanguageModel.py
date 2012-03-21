import math

class StupidBackoffLanguageModel:

	def __init__(self, corpus):
		"""Initialize your data structures in the constructor."""
		self.unigrams = {}
		self.bigrams = {}
		self.train(corpus)

	def train(self, corpus):
		""" Takes a corpus and trains your language model. 
		Compute any counts or other corpus statistics in this function.
		"""  
		for sentence in corpus.corpus:
			previous_word = ""
			for datum in sentence.data:
				word = datum.word
				if word in self.unigrams:
					self.unigrams[word] = self.unigrams[word] + 1.0
				else:
					self.unigrams[word] = 1.0
				if previous_word != "":
					bigram = previous_word + " | " + word
					if bigram in self.bigrams:
						self.bigrams[bigram] = self.bigrams[bigram] + 1.0
					else:
						self.bigrams[bigram] = 1.0
				previous_word = word

	def score(self, sentence):
		""" Takes a list of strings as argument and returns the log-probability of the 
		sentence using your language model. Use whatever data you computed in train() here.
		"""
		score = 1.0
		unigram_vocabulary = len(self.unigrams) + 0.0
		previous_word = ""
		for word in sentence:
			unigram_lookup = self.unigrams[word] if word in self.unigrams else 0.0
			bigram = previous_word + " | " + word
			bigram_lookup = self.bigrams[bigram] if bigram in self.bigrams else 0.0
			previous_word_lookup = self.unigrams[previous_word] if previous_word in self.unigrams else 0.0
			
			if bigram_lookup == 0.0 or previous_word_lookup == 0.0:
				probability = 0.4 * (unigram_lookup + 1.0) / (unigram_lookup + unigram_vocabulary)
			else:
				probability = bigram_lookup / previous_word_lookup
			
			score += math.log(probability)
			previous_word = word
		return score
