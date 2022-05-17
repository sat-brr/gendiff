import json
import os


WORK_DIR = os.getcwd() + '/'

#f1 = '/home/sat/python-project-lvl2/tests/file1.json'
#f2 = '/home/sat/python-project-lvl2/tests/file2.json'


def to_str(val):
    if val == True:
        return 'true'
    elif val == False:
        return 'false'
    elif val == None:
        return 'none'
    else:
        return str(val)    


def generate_diff(path1, path2):
    file1 = json.load(open(WORK_DIR + path1))
    file2 = json.load(open(WORK_DIR + path2))
    file3 = file1.keys() | file2.keys()
    file3 = sorted(file3)
    result = '{' + '\n'
    for k in file3:
        if k in file1.keys() and k in file2.keys():
            if file1[k] == file2[k]:
                result = result + '    ' + str(k) +': ' + to_str(file1[k]) + '\n'
            else:
                result = result + '  - ' + str(k) + ': ' + to_str(file1[k]) + '\n'
                result = result + '  + ' + str(k) + ': ' + to_str(file2[k]) + '\n'
        elif k not in file1.keys():
            result = result + '  + ' + str(k) + ': ' + to_str(file2[k]) + '\n'
        elif k not in file2.keys():
            result = result + '  - ' + str(k) + ': ' + to_str(file1[k]) + '\n'
    result += '}'
    return result
    
#print(generate_diff('file1.json', 'file2.json'))

    # for k, v in file1.items():
    #     if k in file2:
    #         if v == file2[k]:
    #             result = result + '  ' + str(k) +': ' + to_str(v) + '\n'
    #         else:
    #             result = result + '- ' + str(k) + ': ' + to_str(v) + '\n'
    #             result = result + '+ ' + str(k) + ': ' + to_str(file2[k]) + '\n'
    #     else:
    #         result = result + '- ' + str(k) + ': ' + to_str(v) + '\n'
    # for k1, v1 in file2.items():
    #     if k1 not in file1.keys():
    #         result = result + '+ ' + str(k1) + ': ' + to_str(v1) + '\n'
    # result += '}'
    # return result



#print(generate_diff(f1, f2))
    
        
