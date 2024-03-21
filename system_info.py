import psutil
import subprocess
import time

def get_cpu_usage():
    return f"{psutil.cpu_percent()}%"

def get_memory_usage():
    mem = psutil.virtual_memory()
    return {"Usage": f"{mem.percent}%", "Available": f"{mem.available / (1024**3):.2f} GB"}

def get_disk_space():
    disk = psutil.disk_usage('/')
    return {"Total": f"{disk.total / (1024**3):.2f} GB", "Free": f"{disk.free / (1024**3):.2f} GB"}

def get_top_processes(n: int):
    processes = [(p.info['name'], p.info['memory_percent']) for p in psutil.process_iter(['name', 'memory_percent'])]
    top_processes = sorted(processes, key=lambda x: x[1], reverse=True)[:n]
    return {p[0]: f"{p[1]:.2f}%" for p in top_processes}

def get_network_stats():
    stats = psutil.net_if_stats()
    return {iface: f"{'Up' if stats[iface].isup else 'Down'}" for iface in stats}

def get_system_uptime():
    uptime_seconds = psutil.boot_time()
    uptime_hours = (time.time() - uptime_seconds) / 3600
    return f"{uptime_hours:.2f} hours"

def get_system_data():
    print('Geting system data:')
    sys_data = {}
    sys_data["CPU Usage"] = get_cpu_usage()
    sys_data["Memory"] = get_memory_usage()
    sys_data["Disk Space"] = get_disk_space()
    sys_data["Top 5 Processes"] = get_top_processes(n=5)
    sys_data["Network Stats"] = get_network_stats()
    sys_data["System Uptime"] = get_system_uptime()
    return sys_data

if __name__ == "__main__":
    print(get_system_data())
    