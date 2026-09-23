"""
Test cases for the Daily Tarot REST API endpoints.

Skipped automatically if fastapi/httpx aren't installed (the [api] extra),
matching the fact that the API is an optional install.
"""

import os
import tempfile
import unittest

fastapi = None
try:
    from fastapi.testclient import TestClient

    fastapi = True
except ImportError:
    fastapi = False


@unittest.skipUnless(fastapi, "fastapi/httpx not installed (pip install -e '.[api]')")
class TestDailyAPI(unittest.TestCase):
    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self._env_patcher = self._patch_env()
        self._env_patcher.start()

        from api.main import app

        self.client = TestClient(app)

    def tearDown(self):
        self._env_patcher.stop()
        self._tmpdir.cleanup()

    def _patch_env(self):
        from unittest.mock import patch

        return patch.dict(os.environ, {"TAROT_READER_HOME": self._tmpdir.name})

    def test_get_daily_card(self):
        """Test that GET /api/v1/daily returns a well-formed daily reading."""
        response = self.client.get("/api/v1/daily")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("date", data)
        self.assertIn("card", data)
        self.assertIn(data["card"]["orientation"], ["upright", "reversed"])

    def test_get_daily_card_is_consistent_same_day(self):
        """Test that repeated calls return the same card."""
        r1 = self.client.get("/api/v1/daily").json()
        r2 = self.client.get("/api/v1/daily").json()
        self.assertEqual(r1, r2)

    def test_get_daily_card_with_seed(self):
        """Test that a seed produces a repeatable personalized card."""
        r1 = self.client.get("/api/v1/daily", params={"seed": "INFP"}).json()
        r2 = self.client.get("/api/v1/daily", params={"seed": "INFP"}).json()
        self.assertEqual(r1, r2)

    def test_history_starts_empty(self):
        """Test that daily history is empty before any global reading is saved."""
        response = self.client.get("/api/v1/daily/history")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_history_populated_after_unseeded_call(self):
        """Test that an unseeded daily call is persisted to history."""
        self.client.get("/api/v1/daily")
        response = self.client.get("/api/v1/daily/history")
        history = response.json()
        self.assertEqual(len(history), 1)

    def test_seeded_call_not_persisted(self):
        """Test that seeded (personalized) calls are not saved server-side."""
        self.client.get("/api/v1/daily", params={"seed": "INFP"})
        response = self.client.get("/api/v1/daily/history")
        self.assertEqual(response.json(), [])


if __name__ == "__main__":
    unittest.main()
