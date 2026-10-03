import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from tools.google_auth import get_credentials


def _service():
    return build("gmail", "v1", credentials=get_credentials())


def list_recent_emails(max_results: int = 5) -> str:
    """Lists recent emails from the inbox with sender, subject and a short snippet."""
    svc = _service()
    result = svc.users().messages().list(userId="me", maxResults=max_results, labelIds=["INBOX"]).execute()
    msgs = result.get("messages", [])
    if not msgs:
        return "No recent emails."
    lines = []
    for m in msgs:
        msg = svc.users().messages().get(userId="me", id=m["id"], format="metadata",
                                          metadataHeaders=["From", "Subject"]).execute()
        headers = {h["name"]: h["value"] for h in msg["payload"]["headers"]}
        snippet = msg.get("snippet", "")
        lines.append(f"From: {headers.get('From', 'Unknown')}\nSubject: {headers.get('Subject', '(no subject)')}\n{snippet}\n")
    return "\n".join(lines)


def create_draft_reply(to: str, subject: str, body: str) -> str:
    """Creates a Gmail draft (not sent). The user must review and send it manually."""
    message = MIMEText(body)
    message["to"] = to
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    draft = _service().users().drafts().create(userId="me", body={"message": {"raw": raw}}).execute()
    return f"Draft created to {to} with subject '{subject}'. Check your Gmail Drafts folder to review and send."