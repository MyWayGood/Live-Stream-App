import os
import zipfile
import subprocess
import logging

# Set up logging
logging.basicConfig(filename='LiveStreamApp/logs/install.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def extract_zip(zip_file, extract_to):
    """Extracts the contents of a ZIP file."""
    try:
        logging.info(f"Extracting {zip_file} to {extract_to}")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        logging.info(f"Extraction of {zip_file} successful")
    except Exception as e:
        logging.error(f"Error extracting {zip_file}: {str(e)}")

def install_python():
    """Install Python from the pre-downloaded zip file."""
    try:
        python_zip = 'LiveStreamApp/dependencies/Python-3.12.5.zip'
        python_install_dir = 'C:/Python3125'
        if not os.path.exists(python_install_dir):
            os.makedirs(python_install_dir)
        extract_zip(python_zip, python_install_dir)
        logging.info("Python installation successful.")
    except Exception as e:
        logging.error(f"Python installation failed: {str(e)}")

def install_pyinstaller():
    """Install PyInstaller."""
    try:
        pyinstaller_zip = 'LiveStreamApp/dependencies/pyinstaller-6.10.0.zip'
        pyinstaller_install_dir = 'C:/PyInstaller'
        if not os.path.exists(pyinstaller_install_dir):
            os.makedirs(pyinstaller_install_dir)
        extract_zip(pyinstaller_zip, pyinstaller_install_dir)
        subprocess.check_call([os.path.join(pyinstaller_install_dir, 'setup.py'), 'install'])
        logging.info("PyInstaller installation successful.")
    except Exception as e:
        logging.error(f"PyInstaller installation failed: {str(e)}")

def install_ffmpeg():
    """Install FFmpeg."""
    try:
        ffmpeg_zip = 'LiveStreamApp/dependencies/ffmpeg-master-latest-win64-gpl.zip'
        ffmpeg_install_dir = 'LiveStreamApp/bin/ffmpeg'
        if not os.path.exists(ffmpeg_install_dir):
            os.makedirs(ffmpeg_install_dir)
        extract_zip(ffmpeg_zip, ffmpeg_install_dir)
        logging.info("FFmpeg installation successful.")
    except Exception as e:
        logging.error(f"FFmpeg installation failed: {str(e)}")

def install_kivy():
    """Install Kivy."""
    try:
        kivy_zip = 'LiveStreamApp/dependencies/kivy-2.3.0.zip'
        kivy_install_dir = 'LiveStreamApp/bin/kivy'
        if not os.path.exists(kivy_install_dir):
            os.makedirs(kivy_install_dir)
        extract_zip(kivy_zip, kivy_install_dir)
        subprocess.check_call(['pip', 'install', '-r', 'LiveStreamApp/requirements.txt'])
        logging.info("Kivy installation successful.")
    except Exception as e:
        logging.error(f"Kivy installation failed: {str(e)}")

def install_yt_dlp():
    """Install YT-DLP."""
    try:
        yt_dlp_zip = 'LiveStreamApp/dependencies/yt-dlp-2024.08.06.zip'
        yt_dlp_install_dir = 'LiveStreamApp/bin/yt-dlp'
        if not os.path.exists(yt_dlp_install_dir):
            os.makedirs(yt_dlp_install_dir)
        extract_zip(yt_dlp_zip, yt_dlp_install_dir)
        logging.info("YT-DLP installation successful.")
    except Exception as e:
        logging.error(f"YT-DLP installation failed: {str(e)}")

def install_flatpickr():
    """Install Flatpickr."""
    try:
        flatpickr_zip = 'LiveStreamApp/dependencies/flatpickr-4.6.13.zip'
        flatpickr_install_dir = 'LiveStreamApp/bin/flatpickr'
        if not os.path.exists(flatpickr_install_dir):
            os.makedirs(flatpickr_install_dir)
        extract_zip(flatpickr_zip, flatpickr_install_dir)
        logging.info("Flatpickr installation successful.")
    except Exception as e:
        logging.error(f"Flatpickr installation failed: {str(e)}")

def main():
    """Main function that orchestrates the installation of dependencies."""
    logging.info("Starting the installation process.")
    install_python()
    install_pyinstaller()
    install_ffmpeg()
    install_kivy()
    install_yt_dlp()
    install_flatpickr()
    logging.info("Installation process completed.")

if __name__ == '__main__':
    main()
