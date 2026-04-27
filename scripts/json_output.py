from __future__ import annotations

import json
from typing import Any


def dumps_compact_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
