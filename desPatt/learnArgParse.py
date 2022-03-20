import sys
import getopt

comment = '''

print("The name of the current script is - {}".format(sys.argv[0]))

Output -
$ python learnArgParse.py
The name of the current script is - learnArgParse.py


filename = sys.argv[1]
print("The name of the file is - {}".format(sys.argv[1]))

Output:
$ python learnArgParse.py abc.csv
The name of the file is - abc.csv
'''
# The options go into the opts variable. It is a list of tuples.
# Each item in opts is a tuple which contains the option name and the option value.
# args is a list which contains the arguments (not options)

opts,args = getopt.getopt(sys.argv[1:],"s:e:",['startnum','endnum'])

print(opts)
print(args)

'''
$ python learnArgParse.py abc.csv
[]
['abc.csv']

$ python learnArgParse.py -s 100 -e 200
[('-s', '100'), ('-e', '200')]
[]

'''
## Loooping through the list of tuples

for opt,arg in opts:
    if opt == '-s':
        startNum = arg
    if opt == '-e':
        endNum = arg

print(startNum)
print(endNum)

'''
$ python learnArgParse.py -s 100 -e 200
[('-s', '100'), ('-e', '200')]
[]
100
200
'''
