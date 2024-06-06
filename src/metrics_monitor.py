import psutil
import time


def monitor_disk_utilization(threshold):
    while True:
        usage = psutil.disk_usage('/')
        if usage.percent > threshold:
            raise RuntimeError(
                f"Disk utilization is above {threshold}%: {usage.percent}%")
        time.sleep(5)


def monitor_system_metrics(cpu_threshold, memory_threshold):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        if cpu_usage > cpu_threshold:
            raise RuntimeError(
                f"CPU utilization is above {cpu_threshold}%: {cpu_usage}%")
        if memory_usage > memory_threshold:
            raise RuntimeError(
                f"Memory utilization is above {memory_threshold}%: {memory_usage}%")
        time.sleep(5)
