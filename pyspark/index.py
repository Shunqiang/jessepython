from pyspark import  SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = r'C:\Users\admin\AppData\Local\Programs\Python\Python310\python.exe'
conf = SparkConf().setMaster("local[*]").setAppName("test_spaker")

sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([('男', 99), ('女', 99),('女', 99),('男', 99)])

rdd2 = rdd1.reduceByKey(lambda x, y: x + y)
# rdd2 = sc.textFile('C:/Users/admin/Desktop/data.txt')
print(rdd2.collect())
sc.stop()