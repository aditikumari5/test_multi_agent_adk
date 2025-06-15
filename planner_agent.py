class PlannerAgent:
    def plan(self, goal: str):
        steps = []
        if "SpaceX launch" in goal:
            steps = [
                {"agent": "spacex", "params": {}},
                {"agent": "weather", "params": {}},
                {"agent": "summarizer", "params": {"goal": goal}}
            ]
        return steps
