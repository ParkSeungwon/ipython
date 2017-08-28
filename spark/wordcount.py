from pyspark import SparkContext, SparkConf
import sys

class WordCount :
    def getSparkContext(self, appName, master):
        conf = SparkConf().setAppName(appName).setMater(master)
        conf.set("spark.local.ip", "127.0.0.1");
        conf.set("spark.driver.host", "127/0.0.1");
        return SparkContext(conf=conf)

    def getInputRDD(self, sc, input):
        return sc.textFile(input)

    def process(self, inputRDD):
        words = inputRDD.flatMap(lambda s : s.split(" "))
        wcPair = words.map(lambda s : (s,1))
        return wcPair.reduceByKey(lambda x, y : x + y)

    if __name__ == "__main__":
        wc = WordCount()
        sc = wc.getSparkContext("appName", sys.argv[1])
        inputRDD = wc.getInputRDD(sc, sys.argv[2])
        resultRDD = wc.process(inputRDD)
        resultRDD.saveAsTextFile(sys.argv[3])
        sc.stop()
