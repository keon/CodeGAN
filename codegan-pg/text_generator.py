# -*- coding: utf-8 -*-

import string
import re
import nltk
import cPickle as pickle
from random import randint

caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

wordsToIgnore = ["\n", "''", '``']



class TextGenerator:
    def __init__(self, index2WordFile, word2IndexFile, corpus, sentenceLengthLimit = 20):
        self.index2WordFile = index2WordFile
        self.word2IndexFile = word2IndexFile
        self.sequenceOfIndices = []
        self.word2Index = {}
        self.index2Word = {}
        self.corpusWordsCount = None

        with open(corpus, 'r') as f:
            content = ' '.join(f.readlines())
            for wordToIgnore in wordsToIgnore:
                content = content.replace(wordToIgnore, '')
            self.sentences = [nltk.word_tokenize(sentence) for sentence in self.splitIntoSentences(content) if len(sentence) <= sentenceLengthLimit]
            self.sentencesCount = len(self.sentences)
            words = nltk.word_tokenize(content)
            self.tokens = [word.lower() for word in words]
            #add blank space
            self.word2Index[''] = [0]
            self.index2Word[0] = ''
            for word in self.tokens:
                if word in self.word2Index:
                    index = self.word2Index[word]
                else:
                    index = len(self.word2Index)
                    self.word2Index[word] = index
                    self.index2Word[index] = word
                self.sequenceOfIndices.append(index)

            with open(index2WordFile, 'wb') as handle:
                pickle.dump(self.index2Word, handle)

            with open(word2IndexFile, 'wb') as handle:
                pickle.dump(self.word2Index, handle)

        self.corpusWordsCount = len(self.tokens)

    def splitIntoSentences(self, text):
        text = " " + text + "  "
        text = text.replace("\n", " ")
        text = re.sub(prefixes, "\\1<prd>", text)
        text = re.sub(websites, "<prd>\\1", text)
        if "Ph.D" in text: text = text.replace("Ph.D.", "Ph<prd>D<prd>")
        text = re.sub("\s" + caps + "[.] ", " \\1<prd> ", text)
        text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
        text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
        text = re.sub(caps + "[.]" + caps + "[.]", "\\1<prd>\\2<prd>", text)
        text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
        text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
        text = re.sub(" " + caps + "[.]", " \\1<prd>", text)
        if "”" in text: text = text.replace(".”", "”.")
        if "\"" in text: text = text.replace(".\"", "\".")
        if "!" in text: text = text.replace("!\"", "\"!")
        if "?" in text: text = text.replace("?\"", "\"?")
        text = text.replace(".", ".<stop>")
        text = text.replace("?", "?<stop>")
        text = text.replace("!", "!<stop>")
        text = text.replace("<prd>", ".")
        sentences = text.split("<stop>")
        sentences = sentences[:-1]
        sentences = [s.strip() for s in sentences]
        return sentences

    def generateSequence(self, length):
        if self.sentencesCount == 0:
            maxIndex = self.corpusWordsCount - length
            startIndex = randint(0, maxIndex)
            return self.sequenceOfIndices[startIndex: startIndex + length]
        else:
            sentenceIndex = randint(0, self.sentencesCount - 1)
            wordsSequence = self.sentences[sentenceIndex]
            tokensSequence = [self.word2Index[word.lower()] for word in wordsSequence if word in self.word2Index]
            spacesToAppend = length - len(tokensSequence)
            if spacesToAppend > 0:
                tokensSequence += [0] * spacesToAppend
            return tokensSequence


    def saveSamplesToFile(self, length, samplesCount, fileToSave):
        samples = [self.generateSequence(length) for _ in range(samplesCount)]
        with open(fileToSave, "w+") as text_file:
            for sample in samples:
                strSentence = " ".join([str(index) for index in sample]) + "\n"
                text_file.write(strSentence)

    def getTextFromTokenSequence(self, lineOfTokens):
        endOfSentenceSigns = ['.', '?', '!']
        sentenceSigns = [':', ';', ',', '\'', '\'s']
        sequencesToSkip = ["''", "``"]
        isEndOfSentence = False
        strWords = ""
        indices = [int(strIndex) for strIndex in lineOfTokens.split(" ")]
        words = [self.index2Word[index] for index in indices if index in self.index2Word]
        for word in words:
            if word in sequencesToSkip:
                continue
            if word in sentenceSigns:
                strWords += word
                continue
            if word in endOfSentenceSigns:
                strWords += word
                isEndOfSentence = True
            else:
                if isEndOfSentence:
                    word = word.title()
                    isEndOfSentence = False
                strWords += " %s" % word
        return strWords.lstrip()


        #strWords = " ".join(words)
if __name__ == "__main__":
    testInput = "./target_generate/generator_sample.txt"
    generator = TextGenerator('index2word.pickle', 'word2index.pickle', '../corpus_tools/data/source/Charles Dickens - Oliver Twist.txt')

    for _ in range(20):
        testSequenceIndices = generator.generateSequence(20)
        testSequenceWords = [generator.index2Word[index] for index in testSequenceIndices if index in generator.index2Word]
        print " ".join(testSequenceWords)


    with open(testInput, 'r') as f:
        sentences = f.readlines()

    for strSentence in sentences:
        strWords = generator.getTextFromTokenSequence(strSentence)
        #indices = [int(strIndex) for strIndex in strSentence.split(" ")]
        #words = [generator.index2Word[index] for index in indices if index in generator.index2Word]
        #strWords = " ".join(words)
        print strWords

