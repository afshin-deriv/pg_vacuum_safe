import psutil
import subprocess


def check_disk_utilization(threshold):
    usage = psutil.disk_usage('/')
    if usage.percent > threshold:
        raise RuntimeError(
            f"Disk utilization is above {threshold}%: {usage.percent}%")


def check_system_metrics(cpu_threshold, memory_threshold):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    if cpu_usage > cpu_threshold:
        raise RuntimeError(
            f"CPU utilization is above {cpu_threshold}%: {cpu_usage}%")
    if memory_usage > memory_threshold:
        raise RuntimeError(
            f"Memory utilization is above {memory_threshold}%: {memory_usage}%")


def check_active_tables():
    result = subprocess.run(
        ['psql', '-c', "SELECT * FROM pg_stat_activity WHERE state = 'active';"], capture_output=True, text=True)
    active_tables = result.stdout.splitlines()
    if active_tables:
        raise RuntimeError("Active tables detected, aborting vacuum")
