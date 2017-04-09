import subprocess
import statistics

samples = 100

def compileAll():
    subprocess.call(['gcc', '-g', '-Wall', '-o', 'LinkedListSerial', 'LinkedListSerial.c'])
    subprocess.call(['gcc', '-g', '-Wall', '-o', 'LinkedListMutex', 'LinkedListMutex.c', '-lm', '-lpthread'])
    subprocess.call(['gcc', '-g', '-Wall', '-o', 'LinkedListRW', 'LinkedListRW.c', '-lm', '-lpthread'])

def execute(command):
    elapsedTimes = []
    for i in range(samples):
        time = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
        elapsedTimes.append(float(time))


    average = statistics.mean(elapsedTimes)
    standardDeviation = statistics.stdev(elapsedTimes)
    print('     Average Execution Time  = ' + str(average))
    print('     Standard Deviation      = ' + str(standardDeviation))

def executeCommands(commands):
    for i in range(len(commands)):
        command = commands[i];
        print('     Number of Threads       =  ' + command[6])
        execute(commands[i])
        print('')

# different cases to be executed
serial = [['./linkedlist_serial', '1000', '10000', '0.99', '0.005', '0.005'], ['./linkedlist_serial', '1000', '10000', '0.9', '0.05', '0.05'], ['./linkedlist_serial', '1000', '10000', '0.5', '0.25', '0.25']]
M1 = [['./linkedlist_mutex', '1000', '10000', '0.99', '0.005', '0.005', '1'], ['./linkedlist_mutex', '1000', '10000', '0.99', '0.005', '0.005', '2'], ['./linkedlist_mutex', '1000', '10000', '0.99', '0.005', '0.005', '4'], ['./linkedlist_mutex', '1000', '10000', '0.99', '0.005', '0.005', '8']]
M2 = [['./linkedlist_mutex', '1000', '10000', '0.9', '0.05', '0.05', '1'], ['./linkedlist_mutex', '1000', '10000', '0.9', '0.05', '0.05', '2'], ['./linkedlist_mutex', '1000', '10000', '0.9', '0.05', '0.05', '4'], ['./linkedlist_mutex', '1000', '10000', '0.9', '0.05', '0.05', '8']]
M3 = [['./linkedlist_mutex', '1000', '10000', '0.5', '0.25', '0.25', '1'], ['./linkedlist_mutex', '1000', '10000', '0.5', '0.25', '0.25', '2'], ['./linkedlist_mutex', '1000', '10000', '0.5', '0.25', '0.25', '4'], ['./linkedlist_mutex', '1000', '10000', '0.5', '0.25', '0.25', '8']]
RW1 = [['./linkedlist_rw', '1000', '10000', '0.99', '0.005', '0.005', '1'], ['./linkedlist_rw', '1000', '10000', '0.99', '0.005', '0.005', '2'], ['./linkedlist_rw', '1000', '10000', '0.99', '0.005', '0.005', '4'],['./linkedlist_rw', '1000', '10000', '0.99', '0.005', '0.005', '8']]
RW2 = [['./linkedlist_rw', '1000', '10000', '0.9', '0.05', '0.05', '1'], ['./linkedlist_rw', '1000', '10000', '0.9', '0.05', '0.05', '2'], ['./linkedlist_rw', '1000', '10000', '0.9', '0.05', '0.05', '4'], ['./linkedlist_rw', '1000', '10000', '0.9', '0.05', '0.05', '8']]
RW3 = [['./linkedlist_rw', '1000', '10000', '0.5', '0.25', '0.25', '1'], ['./linkedlist_rw', '1000', '10000', '0.5', '0.25', '0.25', '2'], ['./linkedlist_rw', '1000', '10000', '0.5', '0.25', '0.25', '4'], ['./linkedlist_rw', '1000', '10000', '0.5', '0.25', '0.25', '8']]

M = [M1, M2, M3]
RW = [RW1, RW2, RW3]

compileAll()

print('')
print('**************************************************')
print('                   Test Cases')
print('**************************************************')

for i in range(3):
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                     Case ' + str(i + 1))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('')
    print('Serial program :')
    print('')
    execute(serial[i])
    print('')
    print('Parallel program (based on Pthreads) with one mutex :')
    print('')
    executeCommands(M[i])
    print('')
    print('Parallel program (based on Pthreads) with read-write locks :')
    print('')
    executeCommands(RW[i])
