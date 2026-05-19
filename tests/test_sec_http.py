import http.client

from scripts import sec_http


def test_fetch_bytes_retries_remote_disconnected(monkeypatch):
    calls = {"count": 0}

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def read(self):
            return b"ok"

    def fake_urlopen(request, timeout):
        calls["count"] += 1
        if calls["count"] == 1:
            raise http.client.RemoteDisconnected("Remote end closed connection without response")
        return FakeResponse()

    monkeypatch.setattr(sec_http.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(sec_http.time, "sleep", lambda seconds: None)
    monkeypatch.setattr(sec_http, "_throttle", lambda min_interval_seconds: None)

    data = sec_http.fetch_bytes(
        "https://data.sec.gov/submissions/CIK0001759760.json",
        user_agent="13F-Tracker-Test/1.0 maintainer@example.com",
        max_attempts=2,
        logger=None,
    )

    assert data == b"ok"
    assert calls["count"] == 2


def test_fetch_bytes_retries_incomplete_read(monkeypatch):
    calls = {"count": 0}

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def read(self):
            calls["count"] += 1
            if calls["count"] == 1:
                raise http.client.IncompleteRead(b"{", 10)
            return b"{}"

    monkeypatch.setattr(sec_http.urllib.request, "urlopen", lambda request, timeout: FakeResponse())
    monkeypatch.setattr(sec_http.time, "sleep", lambda seconds: None)
    monkeypatch.setattr(sec_http, "_throttle", lambda min_interval_seconds: None)

    data = sec_http.fetch_bytes(
        "https://data.sec.gov/submissions/CIK0001759760.json",
        user_agent="13F-Tracker-Test/1.0 maintainer@example.com",
        max_attempts=2,
        logger=None,
    )

    assert data == b"{}"
    assert calls["count"] == 2
