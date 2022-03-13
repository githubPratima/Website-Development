def mean(L):
    total = 0
    for x in L:
        total += x #total = total +x
    mean = total / len(L)
    return mean


def median(L):
    L.sort()
    if len(L)%2 != 0:
        median = L[int(len(L)/2)]
    else:
        median = L[(int(len(L)/2)) - 1] +  L[int(len(L)/2)]
        median = median/2
    return median


def mode(L):
    counter = 0
    num = L[0]

    for i in L:
        curr_frequency = L.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
        if len(set(L)) == len(L):
            return 'there is no mode'

    return num


def variance(data):
    n = len(data)

    mean = sum(data) / n

    deviations = [(x - mean) ** 2 for x in data]

    variance = sum(deviations) / n
    return variance

def std_dev(ls):
    n = len(ls)
    mean = sum(ls) / n
    var = sum((x - mean)**2 for x in ls) / n
    std_dev = var ** 0.5
    return std_dev






number_list = []

while(True):
    ask = input('enter a number and say "stop" to end: ')

    if ask == 'stop':
        break
    number_list.append(int(ask))

mean = str(mean(number_list))
median = str(median(number_list))
mode = str(mode(number_list))
variance = str(variance(number_list))
std_dev = str(std_dev(number_list))

print('mean: '+ mean + '\n' + 'median: ' + median + '\n' + 'mode: ' + mode + 'variance: ' + variance + '\n' + 'std_dev: '+ std_dev + '\n')



 # square

        # Take the number as input
        number = int(input('Enter a number to get its square '))

        # Define a function to calculate Square
        def calculateSquare(num):
            return num * num

        while (True):
            ask = input('enter a number and say "stop" to end: ')

            if ask == 'stop':
                break

        # print the output
        print("Square of ", number, "is ", calculateSquare(number))
#square

    # Take the number as input
    number = int(input('Enter a number to get its square '))

    # Define a function to calculate Square
    def calculateSquare(num):
        return num * num

    while (True):
        ask = input('enter a number and say "stop" to end: ')

        if ask == 'stop':
            break

    # print the output
    print("Square of ", number, "is ", calculateSquare(number))

#square root
    # Take the number as input
    number = int(input('Enter a number to get its square root '))

    # Define a function to calculate Square
    def calculateSqrt(num):
        return num ** 0.5

    while (True):
        ask = input('enter a number and say "stop" to end: ')

        if ask == 'stop':
            break
    # print the output
    print("Square root of ", number, "is ", calculateSqrt(number))


