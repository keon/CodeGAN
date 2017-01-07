# -*- coding: utf-8 -*-

import re
import nltk
import cPickle as pickle
from random import randint



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
            self.sentences = []
            self.sentencesCount = 0
            # TODO process blocks instead of lines
            self.sentences, self.sentencesCount = self.splitBlocks(f)
            words = nltk.word_tokenize(self.spacer(content))
            self.tokens = [word.lower() for word in words]
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

    def spacer(self, line, postprocess=False):
        line = line.replace('\n', ' _enter ')
        line = line.replace('    ', ' _tab ')
        line = line.replace('=', ' = ')
        line = line.replace('+ =', '+=')
        line = line.replace('- =', '-=')
        line = line.replace('> =', '>=')
        line = line.replace('< =', '<=')
        line = line.replace('! =', '!=')
        line = line.replace('=  =', '==')
        line = line.replace('("', '( "')
        line = line.replace('",', '" ,')
        line = line.replace('(', ' ( ')
        line = line.replace(')', ' ) ')
        line = line.replace('[', ' [ ')
        line = line.replace(']', ' ] ')
        line = line.replace(',', ' , ')
        line = line.replace('.', ' . ')
        line = " ".join(line.split())
        if postprocess == True:
            line = line.replace('_enter','\n')
            line = line.replace('_tab', '\t')
            line = " ".join(line.split())
        line = line.strip()
        return line

    def  splitBlocks(self, f):
        blocks = []
        block = []
        count = 0
        for i, line in enumerate(f):
            block += nltk.word_tokenize(self.spacer(line))
            if len(line) == 1 and line == '\n':
                blocks.append(block)
                count += 1
                block = []
        return blocks, count

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
        strWords = []
        indices = [int(strIndex) for strIndex in lineOfTokens.split(" ")]
        words = [self.index2Word[index] for index in indices if index in self.index2Word]
        for word in words:
            if word.strip() == "_enter":
                strWords.append('\n')
            elif word.strip() == "_tab":
                strWords.append('\t')
            else:
                strWords.append(word)
        return " ".join(strWords)


        #strWords = " ".join(words)
if __name__ == "__main__":
    testInput = "./target_generate/generator_sample.txt"
    generator = TextGenerator('../corpus/index2word.pickle', '../corpus/word2index.pickle', '../corpus/all.code')

    for _ in range(20):
        testSequenceIndices = generator.generateSequence(20)
        testSequenceWords = [generator.index2Word[index] for index in testSequenceIndices if index in generator.index2Word]
        print(" ".join(testSequenceWords))


    with open(testInput, 'r') as f:
        sentences = f.readlines()

    for strSentence in sentences:
        strWords = generator.getTextFromTokenSequence(strSentence)
        print(strWords)

