import unittest
from src.metrics_monitor import monitor_disk_utilization, monitor_system_metrics


class TestMetricsMonitor(unittest.TestCase):
    def test_monitor_disk_utilization(self):
        # Example test case for disk utilization monitoring
        with self.assertRaises(RuntimeError):
            monitor_disk_utilization(threshold=0)

    def test_monitor_system_metrics(self):
        # Example test case for system metrics monitoring
        with self.assertRaises(RuntimeError):
            monitor_system_metrics(cpu_threshold=0, memory_threshold=0)


if __name__ == '__main__':
    unittest.main()
