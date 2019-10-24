# coding=utf8

'''
add data (arff format), Weka 
version: October 24, 2019 02:15 PM
Last revision: October 24, 2019 03:15 PM
  
Author : Chao-Hsuan Ke
'''

allArffData = '';


def Attributes():
    tmpStr = '@ATTRIBUTE sepallength  NUMERIC' + '\n'
    tmpStr = tmpStr + '@ATTRIBUTE sepalwidth   NUMERIC' + '\n'
    tmpStr = tmpStr + '@ATTRIBUTE petallength  NUMERIC' + '\n'
    tmpStr = tmpStr + '@ATTRIBUTE petalwidth   NUMERIC' + '\n'
    tmpStr = tmpStr + '@ATTRIBUTE class        {Iris-setosa,Iris-versicolor,Iris-virginica}' + '\n'
    return tmpStr 


def Data():
    dataStr = '@DATA' + '\n'
    dataStr = dataStr + '5.1,3.5,1.4,0.2,Iris-setosa' + '\n'
    dataStr = dataStr + '4.9,3.0,1.4,0.2,Iris-setosa' + '\n'
    dataStr = dataStr + '4.7,3.2,1.3,0.2,Iris-setosa' + '\n'
    dataStr = dataStr + '4.6,3.1,1.5,0.2,Iris-versicolor' + '\n'
    dataStr = dataStr + '5.0,3.6,1.4,0.2,Iris-virginica' + '\n'
    return dataStr 

    

attributeStr = Attributes()
dataStr = Data();

allArffData = attributeStr + dataStr  

#print(attributeStr)
#print(dataStr)

print(allArffData)