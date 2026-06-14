# SPDX-License-Identifier: MIT
import json
import unittest
from pathlib import Path
from bois_sima_boris.sima import analyze_object, validate_object


class TestSIMA(unittest.TestCase):
    def test_example_ai_workflow_passes(self):
        obj = json.loads(Path("examples/example_local_workflow.json").read_text(encoding="utf-8"))
        ok, findings = validate_object(obj)
        self.assertTrue(ok, [f.__dict__ for f in findings])
        result = analyze_object(obj)
        self.assertGreaterEqual(result["operome"]["count"], 3)
        self.assertTrue(result["candidate_machines"][0]["M"]["C_closure_rule"])

    def test_incomplete_object_fails(self):
        ok, findings = validate_object({"object_id": "bad"})
        self.assertFalse(ok)
        self.assertTrue(any(f.severity == "high" for f in findings))

if __name__ == "__main__":
    unittest.main()
