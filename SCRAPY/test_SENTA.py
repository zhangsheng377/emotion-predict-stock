from SENTA import SentaFactory

senta = SentaFactory(model="snownlp")

print(senta.sentiments(doc="不考虑其他因素，肺炎疫情在印度大爆发的话，小米还要跌一波，印度爆发的概率很大！"))

print(senta.sentiments(doc=""))
