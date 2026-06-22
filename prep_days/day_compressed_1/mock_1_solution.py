"""
Mock #1 — Day 18 prompt (event ingest + top-K + collaborative recs)
Target time: 60 min
Actual time: ___

Clarifying Qs / Assumptions (fill in before coding — paused clock):
- Can there be missing data in these events? How to handle those?
- Can there be repeated data in the events (i.e. for some reason a user generates exactly same event twice or there is an upstream error that causes this). In this case, can I take the latest event as the most relevant one?
-
-
"""

from datetime import datetime


# Your code below this line.
def top_k_items_last_hour(k, now):
    """
    return the K most-viewed items in the hour preceding `now`
    """

    # collect items in the last hour across users.
