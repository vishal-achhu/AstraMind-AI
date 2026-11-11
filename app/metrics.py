from threading import Lock
lock=Lock()
stats={"requests":0,"errors":0,"latency_ms":0.0,"feedback":{}}
def record_request(ms,error=False):
    with lock:
        stats["requests"]+=1; stats["errors"]+=int(error); stats["latency_ms"]+=ms
def record_feedback(rating):
    with lock: stats["feedback"][str(rating)]=stats["feedback"].get(str(rating),0)+1
def snapshot():
    with lock:
        n=stats["requests"]
        return {"requests":n,"errors":stats["errors"],"average_latency_ms":round(stats["latency_ms"]/n,2) if n else 0,"feedback_by_rating":dict(stats["feedback"])}
