#!/usr/bin/env python3

from __future__ import annotations

import base64
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "index.html"
QUESTIONS_PATH = ROOT / "questions.md"


def main() -> None:
    html = INDEX_PATH.read_text(encoding="utf-8")
    encoded = base64.b64encode(QUESTIONS_PATH.read_bytes()).decode("ascii")

    updated_html, count = re.subn(
        r"const EMBEDDED_QUESTIONS_MD_BASE64 = '.*?';",
        f"const EMBEDDED_QUESTIONS_MD_BASE64 = '{encoded}';",
        html,
        count=1,
        flags=re.DOTALL,
    )

    if count != 1:
        raise SystemExit("Impossible de localiser la constante EMBEDDED_QUESTIONS_MD_BASE64 dans index.html")

    INDEX_PATH.write_text(updated_html, encoding="utf-8")
    print("Copie embarquée de questions.md synchronisée dans index.html")


if __name__ == "__main__":
    main()
