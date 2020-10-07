import time

import matplotlib.pyplot as plt

from brute_force import brute_force
from DFA_match import DFA_match
from KMP import KMP_search
from BMH import BMH_search
from BM import BM_search

if __name__ == '__main__':

    with open('dna.50MB', 'r') as file:
        txt = file.read()
    pattern = "ATTCGGGTGGCATCCTCCGGAGAGAGAGAGAGGAAGGAG"

    lst_alg_for_plot = ["DFA", "brute force", "KMP", "BMH", "BM"]
    lst_time_for_plot = []

    #DFA
    start_time = time.time()
    DFA_match(pattern, txt)
    end_time = time.time()
    lst_time_for_plot.append(end_time-start_time)
    print(f"DFA done :{end_time-start_time}")

    #BRUTE FORCE
    start_time = time.time()
    brute_force(pattern, txt)
    end_time = time.time()
    lst_time_for_plot.append(end_time-start_time)
    print(f"BRUTE FORCE done :{end_time - start_time}")

    #KMP
    start_time = time.time()
    KMP_search(pattern, txt)
    end_time = time.time()
    lst_time_for_plot.append(end_time-start_time)
    print(f"KMP done :{end_time - start_time}")

    #BMH
    start_time = time.time()
    BMH_search(pattern, txt)
    end_time = time.time()
    lst_time_for_plot.append(end_time-start_time)
    print(f"BMH done :{end_time - start_time}")

    #BM
    start_time = time.time()
    BM_search(pattern, txt)
    end_time = time.time()
    lst_time_for_plot.append(end_time-start_time)
    print(f"BM done :{end_time - start_time}")


    plt.bar(lst_alg_for_plot, lst_time_for_plot)
    plt.ylabel("Time in seconds")
    plt.savefig('plots/performance_plot.png')
    plt.show()
