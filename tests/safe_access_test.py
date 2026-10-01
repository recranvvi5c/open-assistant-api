import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.utils.safe_access import is_stream_entry, vector_store_file_ids  # noqa: E402


class VectorStoreTests(unittest.TestCase):
    def test_none_and_empty(self):
        self.assertEqual(vector_store_file_ids(None), [])
        self.assertEqual(vector_store_file_ids({}), [])
        self.assertEqual(vector_store_file_ids({"file_search": None}), [])
        self.assertEqual(vector_store_file_ids({"file_search": {}}), [])
        self.assertEqual(vector_store_file_ids({"file_search": {"vector_stores": []}}), [])

    def test_populated(self):
        resources = {"file_search": {"vector_stores": [{"file_ids": ["file-a", "file-b"]}]}}
        self.assertEqual(vector_store_file_ids(resources), ["file-a", "file-b"])

    def test_malformed_levels_do_not_raise(self):
        self.assertEqual(vector_store_file_ids({"file_search": {"vector_stores": [None]}}), [])
        self.assertEqual(vector_store_file_ids({"file_search": {"vector_stores": [{"file_ids": None}]}}), [])


class StreamEntryTests(unittest.TestCase):
    def test_valid_entry(self):
        self.assertTrue(is_stream_entry(["1700000000-0", {"event": "delta"}]))

    def test_malformed_entries(self):
        for bad in (None, [], ["only-id"], [1, {}], ["id", None], "id"):
            self.assertFalse(is_stream_entry(bad), bad)


if __name__ == "__main__":
    unittest.main()
