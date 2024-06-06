import yaml  # type: ignore
import os
import subprocess
import threading
import time
from .datadog_integration import check_datadog_metrics
from .utils import check_disk_utilization, check_system_metrics, check_active_tables

# Load configurations
with open('./config/datadog_config.yaml') as f:
    datadog_config = yaml.safe_load(f)

with open('./config/vacuum_tool_config.yaml') as f:
    tool_config = yaml.safe_load(f)

# Global flag to control monitoring
monitoring_active = True


def monitor_system_metrics():
    global monitoring_active
    while monitoring_active:
        try:
            check_disk_utilization(tool_config['disk_threshold'])
            check_system_metrics(
                tool_config['cpu_threshold'], tool_config['memory_threshold'])
            check_datadog_metrics(datadog_config)
        except RuntimeError as e:
            print(f"Error: {e}")
            monitoring_active = False
            os._exit(1)
        time.sleep(tool_config['check_interval'])


def run_vacuum():
    global monitoring_active
    # Create the monitoring thread
    monitoring_thread = threading.Thread(target=monitor_system_metrics)
    monitoring_thread.start()

    try:
        check_disk_utilization(tool_config['disk_threshold'])
        check_system_metrics(
            tool_config['cpu_threshold'], tool_config['memory_threshold'])
        check_active_tables()
        subprocess.run(['psql', '-U', 'postgres', '-d', 'feed', '-p',
                       '5432', '-h', 'localhost', '-c', 'VACUUM FULL ANALYZE;'])
    except RuntimeError as e:
        print(f"Error: {e}")
    finally:
        monitoring_active = False
        if monitoring_thread.is_alive():
            monitoring_thread.join()


if __name__ == "__main__":
    run_vacuum()
