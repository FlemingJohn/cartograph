from langchain_core.tools import BaseTool

from agents.fakes.fake_actors_for import fake_actors_for
from agents.fakes.fake_attack_paths import fake_attack_paths
from agents.fakes.fake_blast_radius import fake_blast_radius
from agents.fakes.fake_detection_gap import fake_detection_gap
from agents.fakes.fake_list_findings import fake_list_findings
from agents.fakes.fake_record_decision import fake_record_decision


def make_fake_tools() -> list[BaseTool]:
    return [
        fake_list_findings,
        fake_attack_paths,
        fake_blast_radius,
        fake_actors_for,
        fake_detection_gap,
        fake_record_decision,
    ]
