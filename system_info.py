import psutil


def get_system_stats():
    cpu_usage = round(psutil.cpu_percent(), 2)
    memory_usage = round(psutil.virtual_memory().percent, 2)
    disk_usage = round(psutil.disk_usage('/').percent, 2)
    return cpu_usage, memory_usage, disk_usage


def get_process_list(search_text=""):
    # Convert once to avoid redundant calls
    search_text = search_text.lower().strip()

    processes = (
        (p.info["pid"], p.info["name"], round(p.info["cpu_percent"]
         or 0.0, 2), round(p.info["memory_percent"] or 0.0, 2))
        for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"])
    )

    # Sort before filtering
    sorted_processes = sorted(processes, key=lambda x: x[2], reverse=True)

    if search_text:
        sorted_processes = filter(
            lambda p: search_text in p[1].lower(), sorted_processes)  # Faster filtering

    return list(sorted_processes)  # Convert to list only at the end



