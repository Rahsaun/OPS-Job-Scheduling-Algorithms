# OPS-Job-Scheduling-Algorithms

## Overview
This project simulates a single-core CPU scheduling environment. It models how different scheduling algorithms handle processes with varying CPU and I/O demands.

The simulation includes both CPU-bound and I/O-bound processes, along with realistic process state transitions such as READY, RUNNING, WAITING, and TERMINATED.

---

## How to Run
1. Make sure you have all 3 files downloaded onto your device ( simulation.py, scenarios.py, run_experiments.py)
2. Run the simulation:
   run_experiments.py

   The output should look something like this 

   --- Scenario 1 ---

   FCFS: {'avg_wait': 147.8}
 
   SJF: {'avg_wait': 85.8}
 
   RR: {'avg_wait': 153.6}

   --- Scenario 2 ---

   FCFS: {'avg_wait': 12.4}

   SJF: {'avg_wait': 15.4}

   RR: {'avg_wait': 18.8}

   --- Scenario 3 ---

   FCFS: {'avg_wait': 122.30}

   SJF: {'avg_wait': 55.0}

   RR: {'avg_wait': 79.30}

   ---

## Project Structure

- `simulation.py`  
  Contains the core simulation logic, process class, and scheduling algorithms.

- `scenarios.py`  
  Defines three different workload scenarios:
  - CPU-bound processes
  - I/O-bound processes
  - Mixed workload

- `run_experiments.py`  
  Main file that runs all scenarios using each scheduling algorithm.

---

## Scheduling Algorithms Implemented

- **First Come First Serve (FCFS)**  
  Processes are executed in the order they arrive.

- **Shortest Job First (SJF)**  
  Processes with the shortest CPU burst are executed first.

- **Round Robin (RR)**  
  Each process gets a fixed time slice (quantum) before being preempted.

---

## Scenarios

1. **CPU-Bound Scenario**  
   Processes have long CPU bursts and short I/O times.

2. **I/O-Bound Scenario**  
   Processes frequently perform I/O and have short CPU bursts.

3. **Mixed Scenario**  
   A combination of both CPU-bound and I/O-bound processes.

---

## Metrics

The simulation evaluates performance using:

- **Average Waiting Time**  
  The average time processes spend waiting in the ready queue.

---

## Write-up

- **SJF** worked best when most processes were CPU-bound because it runs shorter tasks first, which reduces overall                  waiting time.
- **Round Robin** worked better in mixed workloads because it gives each process a turn using the CPU, so no single                          process has to wait too long before getting time to run.
- **FCFS** was the easiest to understand, but it often performed the worst because long processes can hold the CPU for a              long time, making other processes wait.

---

## Conclusion

This project demonstrates how different scheduling algorithms behave under different workloads. While SJF minimizes waiting time, it can lead to unfairness. Round Robin offers a better balance between fairness and responsiveness, making it more suitable for general-purpose systems.

---



