from ..company.load_company import load_company
from ..connection.get_database import get_database
from ..connection.get_graph import get_graph
from ..indexes.create_indexes import create_indexes
from ..scan.load_scan import load_scan
from ..threat.load_actors import load_actors
from ..threat.load_countermeasures import load_countermeasures
from ..threat.load_detections import load_detections
from ..threat.load_mitigations import load_mitigations
from ..threat.load_techniques import load_techniques


def seed_graph():
    graph = get_graph()
    try:
        graph.delete()
    except Exception:
        pass

    create_indexes()
    load_techniques()
    load_actors()
    load_mitigations()
    load_countermeasures()
    load_company()
    load_detections()
    load_scan()


if __name__ == "__main__":
    seed_graph()

