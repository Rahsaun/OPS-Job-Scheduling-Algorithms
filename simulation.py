import random
from collections import deque

# -----------------------------
# Process Class
# -----------------------------
class Process:
    def __init__(self, pid, bursts):
        self.pid = pid
        self.bursts = bursts  # [(cpu, io), ...]
        self.current_burst = 0

        self.remaining_cpu = bursts[0][0] if bursts else 0
        self.state = "READY"

        self.wait_time = 0
        self.turnaround_time = 0
        self.response_time = None

        self.arrival_time = 0
        self.completion_time = None

    def is_done(self):
        return self.current_burst >= len(self.bursts)


# -----------------------------
# Workload Generator (OPTION 2)
# -----------------------------
def generate_process(pid, cpu_bound=True):
    num_bursts = random.randint(3, 6)

    bursts = []

    for _ in range(num_bursts):
        if cpu_bound:
            cpu_time = random.randint(6, 12)
            io_time = random.randint(1, 3)
        else:
            cpu_time = random.randint(1, 4)
            io_time = random.randint(5, 10)

        bursts.append((cpu_time, io_time))

    return Process(pid, bursts)


# -----------------------------
# Scheduling Algorithms
# -----------------------------
def fcfs(ready_queue):
    return ready_queue[0]


def sjf(ready_queue):
    return min(ready_queue, key=lambda p: p.remaining_cpu)


# -----------------------------
# Simulation Engine
# -----------------------------
def simulate(processes, scheduler="FCFS", quantum=4, max_time=1000):

    time = 0
    ready_queue = deque(processes)
    io_wait = []
    current = None
    time_slice = 0
    completed = []

    for p in processes:
        p.arrival_time = 0

    while time < max_time and len(completed) < len(processes):

        # -----------------------------
        # I/O handling
        # -----------------------------
        for p in io_wait[:]:
            p.remaining_cpu -= 1

            if p.remaining_cpu <= 0:
                io_wait.remove(p)
                p.current_burst += 1

                if not p.is_done():
                    p.remaining_cpu = p.bursts[p.current_burst][0]
                    p.state = "READY"
                    ready_queue.append(p)
                else:
                    p.state = "TERMINATED"
                    p.completion_time = time
                    completed.append(p)

        # -----------------------------
        # Pick process
        # -----------------------------
        if current is None and ready_queue:
            if scheduler == "FCFS":
                current = fcfs(ready_queue)
            elif scheduler == "SJF":
                current = sjf(ready_queue)
            elif scheduler == "RR":
                current = ready_queue[0]

            ready_queue.remove(current)
            current.state = "RUNNING"

            if current.response_time is None:
                current.response_time = time

            time_slice = 0

        # -----------------------------
        # Execute
        # -----------------------------
        if current:
            current.remaining_cpu -= 1
            time_slice += 1

            if current.remaining_cpu <= 0:
                cpu, io = current.bursts[current.current_burst]
                current.current_burst += 1

                if current.is_done():
                    current.state = "TERMINATED"
                    current.completion_time = time
                    completed.append(current)
                    current = None
                else:
                    current.remaining_cpu = io
                    current.state = "WAITING"
                    io_wait.append(current)
                    current = None

            elif scheduler == "RR" and time_slice >= quantum:
                current.state = "READY"
                ready_queue.append(current)
                current = None

        # -----------------------------
        # Waiting time update
        # -----------------------------
        for p in ready_queue:
            p.wait_time += 1

        time += 1

    # -----------------------------
    # METRICS
    # -----------------------------
    total_wait = sum(p.wait_time for p in processes)
    avg_wait = total_wait / len(processes)

    total_turnaround = 0
    total_cpu_time = 0

    for p in processes:
        if p.completion_time is None:
            p.completion_time = time

        turnaround = p.completion_time - p.arrival_time
        total_turnaround += turnaround

        for cpu, _ in p.bursts:
            total_cpu_time += cpu

    avg_turnaround = total_turnaround / len(processes)

    lifespan_ratio = total_turnaround / total_cpu_time

    return {
        "avg_wait": avg_wait,
        "avg_turnaround": avg_turnaround,
        "lifespan_ratio": lifespan_ratio
    }
