from datetime import datetime

now = datetime.now()
ts = now.timestamp()
print(
    f"Seconds since January 1, 1970: {ts:,.4f} "
    f"or {ts:.2e} in scientific notation"
)
print(now.strftime("%b %d %Y"))
