# Live Stream App

Live Stream App is a versatile and user-friendly Windows application designed for live streaming to multiple platforms. It allows users to configure streams, manage settings, and broadcast content effortlessly.

---

## Features

- **Multi-Platform Streaming**: Supports YouTube, Facebook, Instagram, Twitch, and other platforms via RTMP.
- **Custom RTMP Support**: Add custom RTMP URLs for flexibility.
- **Stream Scheduling**: Plan and schedule streams in advance.
- **Automated Streaming**: Configure automated start/stop for live streams.
- **Video Format Conversion**: Built-in tools for seamless video format changes.
- **Live Preview**: Preview your streams before going live.
- **Bitrate and Resolution Control**: Optimize streaming quality based on your needs.
- **Stream Key Management**: Securely store and manage stream keys.
- **Dependency Management**: Automated installation of required dependencies.
- **User-Friendly Interface**: Built with Kivy for a modern and intuitive UI.

---

## System Requirements

- **Operating System**: Windows 10 or later
- **Processor**: Intel Core i3 or equivalent
- **Memory**: 4 GB RAM (8 GB recommended)
- **Storage**: 500 MB of free disk space
- **Dependencies**:
  - FFmpeg
  - Kivy
  - Python 3.8+

---

## Installation

1. **Download the Application**:
   - Obtain the installer or executable file from the [official website](https://avodtv.com).

2. **Install Dependencies**:
   - Dependencies will be installed automatically during the setup process.

3. **Run the Application**:
   - Double-click the executable file to launch the app.

For detailed instructions, refer to the [Installation Guide](docs/installation.pdf).

---

## Usage

1. Launch the application.
2. Configure your stream settings under the **Settings** menu.
3. Add and manage stream keys for your preferred platforms.
4. Schedule or manually start a stream.
5. Monitor your stream status and logs in real-time.

For detailed instructions, refer to the [User Manual](docs/user_manual.pdf).

---

## Configuration Files

The app uses JSON files for configuration:

- `config/settings.json`: Stores application settings like default resolution and platform URLs.
- `config/stream_keys.json`: Contains secure stream keys for supported platforms.
- `config/scheduled_streams.json`: Stores scheduled stream details.

---

## Supported Platforms

The app supports streaming to:

- **YouTube**
- **Facebook**
- **Instagram**
- **Twitch**
- **Dailymotion**
- **TikTok**
- **Rumble**
- **Kick**
- **Vimeo**
- **X (Twitter)**
- **Custom RTMP URLs**

---

## Troubleshooting

- **Configuration Errors**:
  - Ensure all required JSON files exist in the `config` directory.

- **Stream Key Issues**:
  - Verify that the correct stream key is set for the desired platform.

- **Dependency Errors**:
  - Ensure Python and FFmpeg are correctly installed.

Refer to the [FAQ](docs/faq.pdf) for additional help.

---

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request with detailed changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For support or inquiries, contact us at [support@avodtv.com](mailto:support@avodtv.com) or visit our [website](https://avodtv.com).

