#!/usr/bin/env python3
"""Check test coverage, protected source text, and the T12 JSON contract.

This does not evaluate naturalness or semantic equivalence of prose.
Run from any directory: python3 check_outputs.py
Optionally pass one or more answer JSON files to check instead of the defaults.
"""

import json
import sys
from pathlib import Path


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def check(path, expected_ids, protected):
    answers = read_json(path)
    if not isinstance(answers, dict) or set(answers) != expected_ids:
        raise ValueError("Answer IDs do not match the case IDs")
    if any(not isinstance(v, str) or not v.strip() for v in answers.values()):
        raise ValueError("Each case needs a nonempty answer string")

    for case_id, literals in protected.items():
        for literal in literals:
            if literal not in answers[case_id]:
                raise ValueError(f"{case_id}: protected text changed or missing: {literal}")

    machine = json.loads(answers["T12"], object_pairs_hook=unique_object)
    if not isinstance(machine, dict) or set(machine) != {
        "status", "retryable", "attempts", "message"
    }:
        raise ValueError("T12: JSON object fields changed")
    if machine["status"] != "unknown" or machine["retryable"] is not False:
        raise ValueError("T12: status or retryable changed")
    if type(machine["attempts"]) is not int or machine["attempts"] != 0:
        raise ValueError("T12: attempts value or type changed")
    if not isinstance(machine["message"], str) or not machine["message"].strip():
        raise ValueError("T12: message is not a nonempty string")


def main():
    here = Path(__file__).resolve().parent
    cases = read_json(here / "cases.json")
    criteria = read_json(here / "criteria.json")
    expected_ids = {case["id"] for case in cases}
    paths = [Path(arg) for arg in sys.argv[1:]] or [
        here / "answers.json"
    ]
    failed = False
    for path in paths:
        try:
            check(path, expected_ids, criteria["protected_literals"])
        except (OSError, ValueError, TypeError, KeyError) as exc:
            print(f"FAIL {path.name}: {exc}")
            failed = True
        else:
            print(f"PASS {path.name}: complete cases; protected text; JSON contract")
    print("Prose meaning and readability require a separate review.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
