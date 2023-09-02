import os
pid = []
sub = os.popen('ps -ef | grep python').readlines()
#   sub = os.popen('ps -ef | grep gunicorn').readlines()
for i in sub:
    if 'manage.py runserver' in i:
        pid.append(i.split()[1])
for i in sub:
    if '8000' in i:
        pid.append(i.split()[1])
if len(pid) > 0:
#     print(f'django process is:{len(pid)},do you want to kill,y or n')
#     yes = input('input:')
#     if yes == 'n':
#         ...
#     else:
    for i in pid:
        print(f'kill {i} process')
        os.system(f'kill -9 {i}')
else:
    print('did not find django process')