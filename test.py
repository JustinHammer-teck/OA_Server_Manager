from __future__ import annotations
from core.server.server import tail_log

log_path = r"D:\HuyDinh\arena\openarena-0.8.8\openarena-0.8.8\baseoa\qconsole.log"

for line in tail_log(log_path):
    print("[SERVER LOG]", line)
