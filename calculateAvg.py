class Student:
    def  __init__(self, name):
        self.name = name

    def calculateAvg(self,data):
        sum = 0

        for num in data:
            sum += num

        return sum/len(data)

    def jedge(self,avg):
        if avg >= 60:
            result = 'pass'
        else:
            result = 'failed'
        return result

studentS = Student('sata')
data = [98,92,85,96,100]
avg = studentS.calculateAvg(data)
print(avg)
print(studentS.name + ' ' + studentS.jedge(avg))