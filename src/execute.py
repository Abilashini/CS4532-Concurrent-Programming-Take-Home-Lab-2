import subprocess
import statistics
import math

# Number of samples used
NO_OF_SAMPLES = 100

# Compile all the source codes
def compileAll():
    subprocess.call(['gcc', '-g', '-Wall', '-o', 'linkedlist_serial', 'linkedlist_serial.c'])
    subprocess.call(['gcc', '-g', '-Wall', '-o', 'linkedlist_mutex', 'linkedlist_mutex.c', '-lm', '-lpthread'])
    subprocess.call(['gcc', '-g', '-Wall', '-o', 'linkedlist_rw', 'linkedlist_rw.c', '-lm', '-lpthread'])

# Execute a given process and calculate the average and standard deviation
def execute(command):
    elapsedTimes = []
    for i in range(NO_OF_SAMPLES):
        time = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
        elapsedTimes.append(float(time))

    average = statistics.mean(elapsedTimes)
    standardDeviation = statistics.stdev(elapsedTimes)
    samples = math.ceil(math.pow(((100 * 1.96 * standardDeviation) / (5 * average)), 2))
    print('Average: ' + str(average))
    print('Std.Dev: ' + str(standardDeviation))
    #print('Samples: ' + str(samples))

# Execute commands
def executeCommands(commands):
    for i in range(len(commands)):
        if(i is 0):
            print("No of Threads: 1")
        else:
            print("No of Threads: " + str(i * 2))
        execute(commands[i])
        print("")

# Commands that are to be executed
serial = [['./linkedlist_serial', '1000', '10000', '0.99', '0.005', '0.005'], ['./linkedlist_serial', '1000', '10000', '0.9', '0.05', '0.05'], ['./linkedlist_serial', '1000', '10000', '0.5', '0.25', '0.25']]

mutex1 = [['./linkedlist_mutex', '1000', '10000', '0.99', '0.005', '0.005', '1'], ['./linkedlist_mutex', '1000', '10000', '0.99', '0.005', '0.005', '2'], ['./linkedlist_mutex', '1000', '10000', '0.99', '0.005', '0.005', '4'], ['./linkedlist_mutex', '1000', '10000', '0.99', '0.005', '0.005', '8']]

mutex2 = [['./linkedlist_mutex', '1000', '10000', '0.9', '0.05', '0.05', '1'], ['./linkedlist_mutex', '1000', '10000', '0.9', '0.05', '0.05', '2'], ['./linkedlist_mutex', '1000', '10000', '0.9', '0.05', '0.05', '4'], ['./linkedlist_mutex', '1000', '10000', '0.9', '0.05', '0.05', '8']]

mutex3 = [['./linkedlist_mutex', '1000', '10000', '0.5', '0.25', '0.25', '1'], ['./linkedlist_mutex', '1000', '10000', '0.5', '0.25', '0.25', '2'], ['./linkedlist_mutex', '1000', '10000', '0.5', '0.25', '0.25', '4'], ['./linkedlist_mutex', '1000', '10000', '0.5', '0.25', '0.25', '8']]

rw1 = [['./linkedlist_rw', '1000', '10000', '0.99', '0.005', '0.005', '1'], ['./linkedlist_rw', '1000', '10000', '0.99', '0.005', '0.005', '2'], ['./linkedlist_rw', '1000', '10000', '0.99', '0.005', '0.005', '4'],['./linkedlist_rw', '1000', '10000', '0.99', '0.005', '0.005', '8']]

rw2 = [['./linkedlist_rw', '1000', '10000', '0.9', '0.05', '0.05', '1'], ['./linkedlist_rw', '1000', '10000', '0.9', '0.05', '0.05', '2'], ['./linkedlist_rw', '1000', '10000', '0.9', '0.05', '0.05', '4'], ['./linkedlist_rw', '1000', '10000', '0.9', '0.05', '0.05', '8']]

rw3 = [['./linkedlist_rw', '1000', '10000', '0.5', '0.25', '0.25', '1'], ['./linkedlist_rw', '1000', '10000', '0.5', '0.25', '0.25', '2'], ['./linkedlist_rw', '1000', '10000', '0.5', '0.25', '0.25', '4'], ['./linkedlist_rw', '1000', '10000', '0.5', '0.25', '0.25', '8']]


mutex = [mutex1, mutex2, mutex3]
rw = [rw1, rw2, rw3]

# Compile all the files
compileAll()

# Execute and print the output
for i in range(3):
    print('')
    print('                  Case ' + str(i + 1) + '')
    print('Serial:')
    print('')
    execute(serial[i])
    print('')
    print('Mutex:')
    print('')
    executeCommands(mutex[i])
    print('')
    print('ReadWrite:')
    print('      ')
    executeCommands(rw[i])

