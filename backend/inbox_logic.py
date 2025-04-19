import random, string, time, os
from fastapi import HTTPException

inboxes = {}

def random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = os.getenv("DOMAIN_NAME", "tempmail.net")
    return f"{username}@{domain}"

def generate_email():
    email = random_email()
    inboxes[email] = {
        "created": time.time(),
        "emails": []
    }
    return {
        "email": email,
        "expires_in": int(os.getenv("INBOX_TTL", 3600)),
        "max_emails": int(os.getenv("MAX_EMAILS", 10))
    }

def get_inbox(email):
    inbox = inboxes.get(email)
    if not inbox:
        return {"emails": []}
    return {"emails": inbox["emails"]}

def receive_email(email, message):
    if email in inboxes:
        inboxes[email]["emails"].append(message)
        return {"status": "received"}
    raise HTTPException(404, detail="Email not found")
