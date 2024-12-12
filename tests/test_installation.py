import unittest
import subprocess
import os

class TestInstallation(unittest.TestCase):
    
    def setUp(self):
        # Define paths to important scripts and dependencies
        self.install_sh = os.path.join("LiveStreamApp", "scripts", "install.sh")
        self.install_bat = os.path.join("LiveStreamApp", "scripts", "install.bat")
        self.dependencies_path = os.path.join("LiveStreamApp", "dependencies")
        self.virtual_env_path = os.path.join("venv")
    
    def test_dependency_installation(self):
        """
        Verifies that all dependencies are installed by checking for their existence in the expected paths.
        """
        dependencies = [
            os.path.join(self.dependencies_path, "Python-3.12.5.zip"),
            os.path.join(self.dependencies_path, "pyinstaller-6.10.0.zip"),
            os.path.join(self.dependencies_path, "ffmpeg-master-latest-win64-gpl.zip"),
            os.path.join(self.dependencies_path, "kivy-2.3.0.zip"),
            os.path.join(self.dependencies_path, "yt-dlp-2024.08.06.zip"),
            os.path.join(self.dependencies_path, "flatpickr-4.6.13.zip")
        ]
        for dep in dependencies:
            self.assertTrue(os.path.exists(dep), f"Dependency {dep} not found.")

    def test_script_execution(self):
        """
        Ensures that installation scripts run without errors and exit with code 0.
        """
        # Test execution of install.sh (Linux/Mac) or install.bat (Windows)
        if os.name == 'posix':  # Linux or Mac
            result = subprocess.run(['bash', self.install_sh], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertEqual(result.returncode, 0, f"install.sh script failed: {result.stderr.decode()}")
        elif os.name == 'nt':  # Windows
            result = subprocess.run([self.install_bat], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertEqual(result.returncode, 0, f"install.bat script failed: {result.stderr.decode()}")

    def test_environment_setup(self):
        """
        Confirms that the environment is correctly set up after installation by checking for the virtual environment and Python installation.
        """
        python_exec = os.path.join(self.virtual_env_path, "Scripts", "python.exe") if os.name == 'nt' else os.path.join(self.virtual_env_path, "bin", "python")
        self.assertTrue(os.path.exists(python_exec), "Virtual environment not set up correctly. Python executable not found.")
    
if __name__ == '__main__':
    unittest.main()
