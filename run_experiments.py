from simulation import simulate
from scenarios import scenario_1, scenario_2, scenario_3

def run():
    scenarios = [scenario_1, scenario_2, scenario_3]
    schedulers = ["FCFS", "SJF", "RR"]

    for i, scen in enumerate(scenarios):
        print(f"\n--- Scenario {i+1} ---")
        for sched in schedulers:
            processes = scen()
            result = simulate(processes, scheduler=sched)
            print(f"{sched}: {result}")

if __name__ == "__main__":
    run()