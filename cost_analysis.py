def compare_costs(previous, current, threshold=25):
    results = []

    for service in sorted(set(previous) | set(current)):
        old = float(previous.get(service, 0))
        new = float(current.get(service, 0))

        difference = new - old
        percent = (difference / old * 100) if old > 0 else None

        if old == 0 and new > 0:
            status = "NEW SERVICE"
        elif percent is not None and percent >= threshold:
            status = "COST SPIKE"
        else:
            status = "OK"

        results.append({
            "service": service,
            "previous": old,
            "current": new,
            "difference": difference,
            "percent": percent,
            "status": status
        })

    return results
