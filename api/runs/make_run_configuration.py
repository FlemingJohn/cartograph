from langchain_core.runnables import RunnableConfig

MODEL_CALLS_AT_ONCE = 4


def make_run_configuration(scan_id: str) -> RunnableConfig:
    return {"configurable": {"thread_id": scan_id}, "max_concurrency": MODEL_CALLS_AT_ONCE}
