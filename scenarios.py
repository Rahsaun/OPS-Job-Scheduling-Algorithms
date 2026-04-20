from simulation import generate_process

def scenario_1():
    # Mostly CPU-bound
    return [generate_process(i, cpu_bound=True) for i in range(5)]

def scenario_2():
    # Mostly I/O-bound
    return [generate_process(i, cpu_bound=False) for i in range(5)]

def scenario_3():
    # Mixed workload
    return [generate_process(i, cpu_bound=(i % 2 == 0)) for i in range(6)]