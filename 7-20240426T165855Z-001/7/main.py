from mrjob.job import MRJob
import re

WORD_REGEXP = re.compile(r"[\w']+")
class MRWordCount(MRJob):
    def mapper(self, _, line):
        for word in WORD_REGEXP.findall(line):
            yield word, 1
    def combiner(self, word, counts):
        yield word, sum(counts)
    
    def reducer(self, word, counts):
        # Emitting only the count of unique words
        yield "Unique Words Count", 1
    
    def reducer_final(self):
        # Final reducer to sum up the counts of unique words
        yield "Total Unique Words Count", sum(1 for _ in self)
if __name__ == '__main__':
    MRWordCount.run()
