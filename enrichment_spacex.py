import requests

class SpaceXAgent:
    def run(self, context):
        resp = requests.get(context["api_url"]).json()
        return {
            "launch_name": resp.get("name", "N/A"),
            "launch_date": resp.get("date_utc", "N/A"),
            "launch_pad": resp.get("launchpad", "N/A")
        }
