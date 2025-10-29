from virtual_lab.run_meeting import run_meeting
from virtual_lab.agent import Agent
from pathlib import Path

agent = Agent(
    title="Jednoduchý Test Agent",
    expertise="testování systému",
    goal="ověřit, že vše funguje",
    role="pomocník",
    model="gpt-4o"
)

run_meeting(
    meeting_type="individual",
    team_member=agent,
    agenda="Prosím zkontroluj, že asistent funguje správně.",
    save_dir=Path("test_output"),
    save_name="test_meeting",
    num_rounds=1,
    temperature=0.5,
)

