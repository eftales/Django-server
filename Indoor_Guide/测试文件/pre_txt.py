str_data = ''
buff = ''
import numpy
def readtxt(path):
    buff = ''
    with open(path,'r') as f:
        return f.read()





def writetxt(path,buff):
    with open(path,'w') as f:
        print('**--**',buff,'**--**')
        das = buff.split(' ')
        print(das,len(das))
        temp = ''
        while das != [] and das != None:  
            i = 0

            while i<23:
                temp += das.pop(0)
                temp += ' '
                i += 1
            temp  += ';'
        f.write(temp)
        print(temp)
            
if __name__ == '__main__':
    buff = readtxt('mat2.txt')
    #print(buff)
    writetxt('mat2.txt',buff)


