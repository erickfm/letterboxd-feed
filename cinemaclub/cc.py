from letterboxdpy import user
from datetime import datetime


# feed generator for a Letterboxd user’s *following* list
def get_feed(username):
    root = user.User(username)
    following = root.get_following()
    combined_logs = {
        log_id: {**log, "username": u}
        for u in following
        for log_id, log in user.User(u).get_activity()["logs"].items()
    }
    combined_logs = dict(
        sorted(
            combined_logs.items(),
            key=lambda item: datetime(**item[1]["time"]),
            reverse=True,
        )
    )
    return {"logs": combined_logs, "total_logs": len(combined_logs)}
