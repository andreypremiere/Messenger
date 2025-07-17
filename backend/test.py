from datetime import datetime, timezone, timedelta

exp = datetime.now(timezone.utc) + timedelta(days=1)

print(int(exp.timestamp()))