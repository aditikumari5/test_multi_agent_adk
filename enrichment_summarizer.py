class SummarizerAgent:
    def run(self, context):
        summary = (f"Launch: {context.get('launch_name')} on {context.get('launch_date')} at {context.get('launch_pad')}.
"
                   f"Weather: {context.get('weather')}, Temperature: {context.get('temp')}K.")
        status = "likely delayed" if "rain" in context.get("weather", "").lower() else "on schedule"
        return {"summary": summary, "status": status}
