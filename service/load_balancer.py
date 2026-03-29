from agent.agent import Agent

class LoadBalancer:
    def __init__(self):
        self._agents = []
        self._max_agents = 10
    
    def add_agent(self):
        if len(self._agents) < self._max_agents:
            new_agent = Agent(f"Agent-{len(self._agents) + 1}", 5)
            if new_agent not in self._agents:
                self._agents.append(new_agent)
                return True
        return False
    
    def remove_agent(self, agent):
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