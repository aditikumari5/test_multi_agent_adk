<<<<<<< HEAD
# test_multi_agent_adk
=======
# Multi-Agent AI System Using Google ADK

## Overview
This project is a multi-agent AI system that takes a user goal, plans a route using different agents, and executes those agents in a chain. Each agent builds on the output of the previous one.

### Example Goal:
> "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."

### Agents Involved:
- **Planner Agent**: Decides the sequence of actions.
- **SpaceX Agent**: Finds the next SpaceX launch details.
- **Weather Agent**: Fetches weather information for the launch location.
- **Summarizer Agent**: Summarizes findings and checks if weather might cause delays.

## Setup Instructions
1. Clone this repo or unzip the folder.
2. Create a `.env` file with the following content:
```
SPACEX_API_URL=https://api.spacexdata.com/v4/launches/next
OPENWEATHER_API_KEY=your_openweather_key
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run the system with:
```
python run_system.py --goal "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."
```

## Folder Structure
- `planner_agent.py`: Plans which agents to use
- `enrichment_spacex.py`: Gets launch data
- `enrichment_weather.py`: Gets weather data
- `enrichment_summarizer.py`: Summarizes and decides
- `run_system.py`: Runs the whole chain
- `tests/`: Evaluation and testing scripts
>>>>>>> 3cdc5f2 (adding file)
