import json
import pathlib
import sys
import unittest


SCRIPTS_DIR = pathlib.Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from json_output import dumps_compact_json


class CompactJsonOutputTest(unittest.TestCase):
    def test_dumps_compact_json_round_trips_without_padding(self):
        payload = {
            "generated_at_utc": "2026-04-27T00:00:00Z",
            "managers": [
                {
                    "id": "buffett",
                    "name": "巴菲特",
                    "filings": [
                        {
                            "quarter": "2025Q4",
                            "holdings": [
                                {
                                    "issuer": "APPLE INC",
                                    "value_usd": 61961735283,
                                    "weight": 0.22600567438022331,
                                }
                            ],
                        }
                    ],
                }
            ],
        }

        output = dumps_compact_json(payload)

        self.assertEqual(json.loads(output), payload)
        self.assertNotIn("\n", output)
        self.assertNotIn(": ", output)
        self.assertIn("巴菲特", output)


if __name__ == "__main__":
    unittest.main()
