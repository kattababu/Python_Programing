import argparse
import pdb
import numpy as np
import time

def main():
    args = parser.parse_args()
    display_list = []
    if args.Number:
        in_ = int(args.Number)
        if int(args.Number) % 2 != 0:
            for i in np.arange(0, in_ / 2, 1):
                display_list.append(int((i + 1) * -1))
            display_list.pop()
            for i in np.arange(in_ / 2, in_, 1):
                display_list.append(int(i - (in_ / 2)))
        else:
            for i in np.arange(0, in_ / 2, 1):
                display_list.append(int((i + 1) * -1))
            for i in np.arange(in_/2, in_, 1):
                display_list.append(int(i - ((in_ / 2) - 1)))
        print("Given Input: %s Output Resultant List: %s and Result: %s"%(args.Number, display_list, int(sum(display_list))))
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", "--Number", help = "Show Output")
    start_time = time.time()
    main()
    print ("Time Takens: %s Seconds"%(time.time() - start_time))

