# A class constructor -> Takes an array and stores it in
# _elements
# Give Max diff possible in that array
'''
class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
'''   ## Non editable Backend Code
    def computeDifference(self):
        max_m = min_m = self.__elements[0]
        for i in self.__elements:
            if max_m < i :
                max_m = i
            if min_m > i:
                min_m = i
        self.maximumDifference = abs(max_m - min_m)

# End of Difference class
'''
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
'''
