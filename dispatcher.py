from service.load_balancer import LoadBalancer

manager = LoadBalancer()

def dispatch_task(task):
    if manager.assign_task(task):
        print(f"Task '{task}' has been dispatched successfully.")
    else:
        print(f"Failed to dispatch task '{task}'. No available agents.")

dispatch_task("Task 1")
dispatch_task("Task 2")
dispatch_task("Task 3")
dispatch_task("Task 4")
dispatch_task("Task 5")
dispatch_task("Task 6")
dispatch_task("Task 7")
dispatch_task("Task 8")
manager.agents_status()