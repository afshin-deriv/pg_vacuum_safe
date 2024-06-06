import unittest
from src.datadog_integration import check_datadog_metrics


class TestDatadogIntegration(unittest.TestCase):
    def test_check_datadog_metrics(self):
        # Example test case for Datadog metrics check
        config = {
            'api_key': 'test_api_key',
            'app_key': 'test_app_key',
            'metrics': {
                'disk_utilization': 'system.disk.utilization',
                'cpu_usage': 'system.cpu.usage',
                'memory_usage': 'system.memory.usage'
            }
        }
        with self.assertRaises(RuntimeError):
            check_datadog_metrics(config)


if __name__ == '__main__':
    unittest.main()
