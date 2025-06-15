import os
from planner_agent import PlannerAgent
from enrichment_spacex import SpaceXAgent
from enrichment_weather import WeatherAgent
from enrichment_summarizer import SummarizerAgent

def load_agents():
    return {
        "spacex": SpaceXAgent(),
        "weather": WeatherAgent(),
        "summarizer": SummarizerAgent(),
    }

def main(goal):
    planner = PlannerAgent()
    plan = planner.plan(goal)
    context = {
        "api_url": os.getenv("SPACEX_API_URL"),
        "weather_key": os.getenv("OPENWEATHER_API_KEY")
    }
    agents = load_agents()
    for step in plan:
        agent = agents[step["agent"]]
        output = agent.run(context)
        context.update(output)
    print(context.get("summary", ""), "
Status:", context.get("status", ""))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--goal", required=True)
    args = parser.parse_args()
    main(args.goal)
