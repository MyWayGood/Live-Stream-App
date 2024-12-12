# -*- mode: python ; coding: utf-8 -*-

import PyInstaller.__main__
from PyInstaller.utils.hooks import collect_data_files
import os

# Define paths to the configuration files
config_files = [
    ('config/settings.json', 'config'),
    ('config/stream_keys.json', 'config'),
    ('config/scheduled_streams.json', 'config'),
]

# The entry point of your app (main.py)
a = Analysis(
    ['LiveStreamApp/main.py'],  # This should point to the correct location of main.py
    pathex=['LiveStreamApp'],  # This should point to your project's root directory
    binaries=[],
    datas=[
        ('config/settings.json', 'config'),
        ('config/stream_keys.json', 'config'),
        ('config/scheduled_streams.json', 'config'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
)

# Build the final executable
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='LiveStreamApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Change to True if you want a console window
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='LiveStreamApp'
)

# Call PyInstaller to build the app with the .spec file
PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--add-data=config/settings.json;config',
    '--add-data=config/stream_keys.json;config',
    '--add-data=config/scheduled_streams.json;config',
])
