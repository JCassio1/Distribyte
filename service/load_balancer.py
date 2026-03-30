import time
import threading
from agent.agent import Agent

class LoadBalancer:
    def __init__(self):
        self._agents = []
        self._max_agents = 10
        self._running = False
        self._lock = threading.Lock()

    def run(self, poll_interval: float = 1.0):
        self._running = True

        try:
            while self._running:
                self._health_check()
                time.sleep(poll_interval)
        except KeyboardInterrupt:
            self.stop()
    
    def add_agent(self):
        with self._lock:
            if len(self._agents) < self._max_agents:
                new_agent = Agent(f"Agent-{len(self._agents) + 1}", 5)
                if new_agent not in self._agents:
                    self._agents.append(new_agent)
                    return True
        return False
    
    def remove_agent(self, agent):
        with self._lock:
            if agent in self._agents:
                self._agents.remove(agent)
                return True
        return False
    
    def assign_task(self, task):
        if not self._agents:
            self.add_agent()

        if not self._agents:
            return False
        
        # Least connections strategy.
        least_loaded_agent = None
        for agent in self._agents:
            if agent.is_available:
                if least_loaded_agent is None or len(agent.tasks) < len(least_loaded_agent.tasks):
                    least_loaded_agent = agent

        if least_loaded_agent:
            return least_loaded_agent.add_task(task)
        return False
    
    def stop(self):
        self._running = False
        print("Load balancer stopped.")

    def _health_check(self):
        with self._lock:

            self._agents = [a for a in self._agents if a.is_available or len(a.tasks) > 0]

            if not self._agents:
                print("No agents available. Spawning one.")
                self.add_agent()


if __name__ == "__main__":
    load_balancer = LoadBalancer()
    load_balancer.run()