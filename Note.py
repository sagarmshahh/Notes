import time

note=' '
note_file=''
while note!='':
    note=input()
    note_file+=note+'\n'

Time=['created on ',time.asctime(),' \n']

fo=open('file.doc','a')  
fo.writelines(Time)
fo.writelines(note_file)
fo.close()

f=open('file.doc','r')
File_info=f.read()
print(File_info)
f.close()
