# GitHub Universe 2025 Badge Repository

Welcome to the GitHub Universe 2025 Badge repository! This repository is a one-stop solution for all the apps, tools, and resources you need to unlock the full potential of your GitHub Universe 2025 Tufty Badge. By simply copying and pasting the contents of this repository onto your badge, you can access everything in one place and start exploring the endless possibilities.

## Repository Structure

Here's an overview of the repository structure to help you navigate through the contents:

```
/
├── badge/                    # Badge firmware and apps (deployed to /system/ on device)
│   ├── apps/                 # Application directory
│   │   ├── badge/            # GitHub profile stats viewer
│   │   ├── flappy/           # Flappy Bird style game
│   │   ├── gallery/          # Image gallery viewer
│   │   ├── menu/             # App launcher/menu system
│   │   ├── monapet/          # Virtual pet simulator
│   │   ├── quest/            # IR beacon scavenger hunt
│   │   ├── sketch/           # Drawing app
│   │   ├── startup/          # Boot animation
│   │   ├── snake/            # Classic Snake game
│   │   ├── weather/          # Weather app
│   │   ├── wifi/             # WiFi configuration app
│   │   └── ...               # More apps to explore!
│   └── assets/               # Shared assets (fonts, sprites)
│       ├── fonts/            # Pixel Perfect Fonts (.ppf, .af)
│       └── mona-sprites/     # Mona character sprite sheets
├── simulator/                # Badge simulator for testing apps on your computer
│   ├── badge_simulator.py    # Simulator script
│   └── README.md             # Simulator documentation
├── badgerware/               # Core libraries and documentation for badge development
│   ├── brushes.md            # Documentation for brushes module
│   ├── Image.md              # Documentation for Image module
│   ├── io.md                 # Documentation for io module
│   ├── Matrix.md             # Documentation for Matrix module
│   ├── PixelFont.md          # Documentation for PixelFont module
│   └── shapes.md             # Documentation for shapes module
├── README.md                 # Introduction to the repository
├── LICENSE                   # License information
├── main.py                   # Main entry point and app launcher
└── secrets.py                # WiFi configuration secrets
```

## Repository Overview

This repository is a comprehensive collection of apps, tools, and resources for the GitHub Universe 2025 Tufty Badge. It combines multiple repositories into one, making it easier for users to access everything they need in a single place.

### Key Highlights

- **Apps Directory:**
  - Explore a variety of pre-built apps, including games, utilities, and creative tools.
  - Each app is self-contained with its own assets and code.

- **Simulator:**
  - Test your apps on your computer before deploying them to the badge.
  - Includes detailed documentation for setup and usage.

- **Core Libraries:**
  - Access the `badgerware` libraries for creating and customizing apps.
  - Includes modules for graphics, input handling, and more.

- **Documentation:**
  - Find detailed guides and examples to help you get started.
  - Includes API references for the badge's core modules.

### How to Use This Repository

1. **Copy the Repository to Your Badge:**
   - Connect your badge to your computer via USB.
   - Put the badge into mass storage mode by pressing the RESET button twice.
   - Copy the contents of this repository to the `/system/` directory on your badge.

2. **Explore the Apps:**
   - Navigate through the `badge/apps/` directory to discover pre-installed apps.
   - Launch apps directly from the badge's menu.

3. **Develop Your Own Apps:**
   - Use the examples and libraries provided to create your own apps.
   - Follow the structure and guidelines in the `docs/README.md` file.

4. **Test with the Simulator:**
   - Use the simulator to test your apps on your computer.
   - Refer to the `simulator/README.md` for detailed instructions.

5. **Contribute:**
   - Submit your own apps or improvements via pull requests.
   - Check the `CONTRIBUTING.md` file for guidelines.

---

Happy hacking with your GitHub Universe 2025 Badge!
