from snownlp import SnowNLP

from .senta import Senta


class SentaSnownlp(Senta):

    def sentiments(self, doc):
        senta_score = 0.5
        try:
            senta_score = SnowNLP(doc).sentiments
        except:
            # print("error")
            pass
        return senta_score
