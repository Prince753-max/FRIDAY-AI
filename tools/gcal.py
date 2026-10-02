from datetime import datetime, timedelta
from googleapiclient.discovery import build
from tools.google_auth import get_credentials

TIMEZONE = "Asia/Kolkata"


def _service():
    return build("calendar", "v3", credentials=get_credentials())


def list_events(days_ahead: int = 1) -> str:
    """Lists upcoming calendar events for the next N days (default 1)."""
    now = datetime.now().astimezone()
    end = now + timedelta(days=days_ahead)
    result = _service().events().list(
        calendarId="primary",
        timeMin=now.isoformat(),
        timeMax=end.isoformat(),
        singleEvents=True,
        orderBy="startTime",
        maxResults=15,
    ).execute()
    events = result.get("items", [])
    if not events:
        return "No upcoming events."
    
    lines = []
    for e in events:
        raw = e["start"].get("dateTime")
        if raw:
            when = datetime.fromisoformat(raw).astimezone().strftime("%a %d %b, %I:%M %p")
        else:
            when = e["start"].get("date") + " (all day)"
        lines.append(f"{when} - {e.get('summary', '(no title)')}")
    return "\n".join(lines)

def create_event(title: str, start_time: str, duration_minutes: int = 30) -> str:
    """Creates a calendar event. start_time must be ISO format like 2026-10-04T16:00:00 in India time."""
    start = datetime.fromisoformat(start_time)
    end = start + timedelta(minutes=duration_minutes)
    body = {
        "summary": title,
        "start": {"dateTime": start.isoformat(), "timeZone": TIMEZONE},
        "end": {"dateTime": end.isoformat(), "timeZone": TIMEZONE},
    }
    created = _service().events().insert(calendarId="primary", body=body).execute()
    return f"Created '{title}' at {start_time}. Link: {created.get('htmlLink')}"