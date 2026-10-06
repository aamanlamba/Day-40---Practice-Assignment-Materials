import os

# Mixed configuration approach inherited from multiple generations.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./brownfield.db")
LEGACY_TIMEOUT_SECONDS = int(os.getenv("LEGACY_TIMEOUT_SECONDS", "30"))
# Deliberately poor default retained from legacy dev setup; should be discovered and remediated.
PARTNER_SHARED_TOKEN = os.getenv("PARTNER_SHARED_TOKEN", "dev-shared-token-123")
ENABLE_EXPERIMENTAL_SCORING = os.getenv("ENABLE_EXPERIMENTAL_SCORING", "true").lower() == "true"
