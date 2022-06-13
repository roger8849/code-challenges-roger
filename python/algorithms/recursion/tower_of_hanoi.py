from timeit import default_timer as timer
def toh(n:int) -> int:
    '''
        The number of movements to move N disk from Tower A to Tower C using a helper B is:
        The number of steps to move N-1 disk from A to B + 1 (move Nth disk) + the number of steps
        to move N-1 disks from B-C.
        
        The mathematical formula is 2^n - 1
    '''
    # base case
    if n==0:
        return 0

    return toh(n-1) + 1 + toh(n-1)

def printStepsTOH(n, source, destination ,helper):
    if n == 0:
        return
    printStepsTOH(n-1, source, helper, destination)
    print(f'Moving disk {n} from {source} to {destination}')
    printStepsTOH(n-1, helper, destination, source)
    

def main():
    n = int(input('Enter a number: '))

    print('--- Normal method ---')
    start=timer()
    print(f'number of steps to move N = {n} disks is {toh(n)}')
    end=timer()
    print(f'Time in seconds {(end-start):.10f}')


    print('--- Normal method ---')
    start=timer()
    print(f'Steps to move N = {n} disks ')
    printStepsTOH(n, "A", "C", "B")
    end=timer()
    print(f'Time in seconds {(end-start):.10f}')


if __name__ == "__main__":
    main()