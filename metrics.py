import psutil
import platform
import socket

# 🖥️ CPU Metrics
def get_cpu_usage():
    """Returns CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def get_cpu_count():
    """Returns the number of CPU cores."""
    return psutil.cpu_count(logical=True)

def get_cpu_freq():
    """Returns CPU frequency in MHz."""
    return psutil.cpu_freq()._asdict()

# 🛠️ Memory Metrics
def get_memory_usage():
    """Returns memory usage details."""
    memory = psutil.virtual_memory()
    return memory._asdict()

# 💾 Disk Metrics
def get_disk_usage():
    """Returns disk usage details."""
    return psutil.disk_usage('/')._asdict()

def get_disk_partitions():
    """Returns all disk partitions."""
    partitions = psutil.disk_partitions()
    return [p._asdict() for p in partitions]

# 🌐 Network Metrics
def get_network_io():
    """Returns network I/O stats."""
    return psutil.net_io_counters()._asdict()

def get_network_connections():
    """Returns a list of active network connections."""
    connections = psutil.net_connections()
    return [conn._asdict() for conn in connections]

# 📌 Process Metrics
def get_running_processes():
    """Returns a list of running processes."""
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    return processes

# 🏠 System Information
def get_system_info():
    """Returns system information."""
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname())
    }
