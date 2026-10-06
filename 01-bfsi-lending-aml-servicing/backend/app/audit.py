import json, logging
logger = logging.getLogger("audit")

def audit(event: str, **fields):
    # Partial migration: callers are not yet consistently using this helper.
    logger.info(json.dumps({"event": event, **fields}, default=str))
