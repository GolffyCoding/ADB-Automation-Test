import unittest
from ppadb.client import Client as AdbClient
import time

class TestADBOperations(unittest.TestCase):
   @classmethod 
   def setUpClass(cls):
       cls.client = AdbClient(host="127.0.0.1", port=5037)
       cls.device = cls.client.devices()[0]
       cls.package_name = "com.example.app"
       
   def setUp(self):
       self.device.shell("input keyevent 26")
       self.device.shell("input keyevent 82")
       self.device.shell(f"am start -n {self.package_name}/.MainActivity")
       time.sleep(2)
   
   def test_device_connection(self):
       self.assertIsNotNone(self.device)
       self.assertTrue(self.device.is_connected())
       
   def test_app_installation(self):
       apk_path = "test.apk"
       self.device.install(apk_path)
       
       packages = self.device.shell("pm list packages")
       self.assertIn(self.package_name, packages)
       
       self.device.uninstall(self.package_name)
       packages = self.device.shell("pm list packages")
       self.assertNotIn(self.package_name, packages)
   
   def test_app_launch(self):
       result = self.device.shell(f"am start -n {self.package_name}/.MainActivity")
       self.assertIn("Starting:", result)
       
       current_app = self.device.shell("dumpsys window | grep mCurrentFocus")
       self.assertIn(self.package_name, current_app)
   
   def test_ui_interactions(self):
       self.device.shell("input tap 100 200")
       self.device.shell("input text 'test'")
       self.device.shell("input swipe 100 500 100 100")
   
   def test_file_operations(self):
       self.device.push("local.txt", "/sdcard/test.txt")
       
       files = self.device.shell("ls /sdcard/")
       self.assertIn("test.txt", files)
       
       self.device.pull("/sdcard/test.txt", "downloaded.txt")
       
       self.device.shell("rm /sdcard/test.txt")
       files = self.device.shell("ls /sdcard/")
       self.assertNotIn("test.txt", files)
   
   def test_device_info(self):
       model = self.device.shell("getprop ro.product.model")
       self.assertIsNotNone(model)
       
       version = self.device.shell("getprop ro.build.version.release")
       self.assertIsNotNone(version)
       
       resolution = self.device.shell("wm size")
       self.assertIn("Physical size:", resolution)
   
   def test_logcat(self):
       self.device.shell("logcat -c")
       
       self.device.shell(f"am start -n {self.package_name}/.MainActivity")
       
       logs = self.device.shell("logcat -d")
       self.assertNotEqual(logs.strip(), "")
   
   def test_network(self):
       self.device.shell("svc wifi enable")
       wifi_state = self.device.shell("settings get global wifi_on")
       self.assertIn("1", wifi_state)
       
       self.device.shell("svc wifi disable")
       wifi_state = self.device.shell("settings get global wifi_on")
       self.assertIn("0", wifi_state)
   
   def test_screenshot(self):
       result = self.device.screencap()
       with open("screen.png", "wb") as f:
           f.write(result)
   
   def test_battery(self):
       battery = self.device.shell("dumpsys battery")
       self.assertIn("level:", battery)
   
   def test_memory_info(self):
       memory = self.device.shell("dumpsys meminfo")
       self.assertIn("Total RAM:", memory)
   
   def tearDown(self):
       self.device.shell(f"pm clear {self.package_name}")
   
   @classmethod
   def tearDownClass(cls):
       cls.device = None
       cls.client = None

if __name__ == "__main__":
   unittest.main()