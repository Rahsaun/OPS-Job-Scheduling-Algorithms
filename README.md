# OPS-Job-Scheduling-Algorithms

## Overview
This project simulates a single-core CPU scheduling environment. It models how different scheduling algorithms handle processes with varying CPU and I/O demands.

The simulation includes both CPU-bound and I/O-bound processes, along with realistic process state transitions such as READY, RUNNING, WAITING, and TERMINATED.

---

## How to Run

1. Clone the repository:
   git clone https://github.com/Rahsaun/-OPS-Job-Scheduling-Algorithms.git

2. Navigate into the project folder:
   cd -OPS-Job-Scheduling-Algorithms

3. Run the simulation:
   python run_experiments.py

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
   Combination of both CPU-bound and I/O-bound processes.

---

## Metrics

The simulation evaluates performance using:

- **Average Waiting Time**  
  The average time processes spend waiting in the ready queue.

---

## Results & Observations

- **SJF** performed best in CPU-bound scenarios because it prioritizes shorter jobs.
- **Round Robin** provided better fairness, especially in mixed workloads.
- **FCFS** was the simplest but often performed the worst due to long waiting times.

---

## Conclusion

This project demonstrates how different scheduling algorithms behave under different workloads. While SJF minimizes waiting time, it can lead to unfairness. Round Robin offers a better balance between fairness and responsiveness, making it more suitable for general-purpose systems.

---



