---
title: "Introducing Bentobox: Linux Subsystem for Windows (LSW)"
author: Language Seed
date: "2025-11-23"
excerpt: "Flipping the script on WSL - Bentobox puts Linux first with Windows as a guest via WinBoat. A thoughtfully curated Ubuntu setup for developers seeking a Windows exit strategy without ditching Windows completely."
tags: ["devops", "ubuntu", "docker", "ai", "announcement", "wsl", "winboat"]
---

# Introducing Bentobox: Linux Subsystem for Windows (LSW)

> **Built on the shoulders of giants**: This project is inspired by and built upon [Omakub](https://omakub.org) by DHH and the ambitious [Omarchy](https://omarchy.org) project. We're grateful to the 37signals team for their vision of beautiful, opinionated Linux environments.

I'm excited to announce the release of [**Bentobox**](https://github.com/languageseed/bentobox), a carefully curated Ubuntu development environment that **flips the Windows Subsystem for Linux (WSL) paradigm on its head**.

## The Big Idea: Linux Subsystem for Windows (LSW)

For years, Windows developers have used WSL to run Linux inside Windows. Bentobox does the reverse - it makes **Linux your primary OS** and runs Windows as a seamless guest using **WinBoat**.

This isn't revolutionary technology - it's a Windows VM. But WinBoat makes the experience so polished that Windows apps integrate naturally with your Linux desktop. For Windows users looking for an **exit strategy without completely ditching Windows**, this is the best compromise I've found.

Let's make "Linux Subsystem for Windows" (LSW) a thing. 😄

## What is Bentobox?

Bentobox is a fork of the excellent [Omakub](https://github.com/basecamp/omakub) project by DHH, customized and enhanced for professional development workflows with a focus on **containers, AI integration, remote work, and Windows app compatibility**.

The name reflects our philosophy: like a Japanese bento box, we've carefully selected quality tools over quantity, each serving a specific purpose, arranged thoughtfully in a beautiful container.

<carousel>
/images/2025-11-24-bentobox-1.png|Bentobox Desktop Interface|Beautiful curated Ubuntu desktop with modern wallpapers;
/images/2025-11-24-bentobox-2.png|GUI Installer|Intuitive desktop installer for selecting applications and tools;
/images/2025-11-24-bentobox-3.png|Theme Selection|Choose from multiple professionally curated themes;
/images/2025-11-24-bentobox-4.png|Docker Integration|Portainer and OpenWebUI for container and AI management;
/images/2025-11-24-bentobox-5.png|Development Environment|Modern editors and development tools ready to use
</carousel>

## 🎯 Key Features

### Core Tools (Always Installed)

- **Modern Editors**: Neovim, VS Code, Zed
- **Docker & Portainer**: Full container management UI at `localhost:9000`
- **OpenWebUI**: AI chat interface at `localhost:3000`
- **Essential Apps**: Chrome, Obsidian, VLC, Flameshot, and more
- **60+ Premium Wallpapers**: Professionally curated from Unsplash and Pexels
- **GUI Installer**: Beautiful desktop interface with selection menus

### Optional Components (Your Choice)

During installation, you can select:

- **Programming Languages**: Ruby on Rails, Node.js, Python, Go, PHP, Elixir, Rust, Java
- **Professional Tools**: 1Password, Tailscale VPN, Sublime Text
- **WinBoat**: Run Windows apps seamlessly on Linux (like "reverse WSL")
- **Ollama**: Local LLM server for privacy-focused AI development
- **Barrier**: Free KVM sharing for multi-computer setups

### Extension System

Bentobox features a powerful extension system that makes customization easy:

- **Simple Metadata Format**: Add new applications with just a template file
- **Automatic GUI Integration**: New extensions appear automatically in the installer
- **Theme System**: Create and share custom themes with colors and wallpapers
- **Ready-to-Use Templates**: Get started quickly with provided templates
- **Community Sharing**: Easy to contribute and share extensions via pull requests

## 🚀 Quick Start

Installation is simple - just run this one command on a fresh Ubuntu 24.04+ system:

```bash
wget -qO- https://raw.githubusercontent.com/languageseed/bentobox/master/boot.sh | bash
```

The GUI installer will guide you through:
1. Selecting optional applications from an intuitive desktop interface
2. Choosing programming languages you need
3. Picking your preferred theme and wallpaper
4. Configuring Docker containers (Portainer, OpenWebUI, Ollama)
5. Setting up your development environment

Installation takes 15-30 minutes depending on your selections.

### Post-Installation

After rebooting, you can:

- **Access Portainer**: `http://localhost:9000` (create admin account on first visit)
- **Access OpenWebUI**: `http://localhost:3000`
- **Access Ollama** (if installed): `http://localhost:11434`
- **Download AI Models**: `docker exec -it ollama ollama pull llama3.2`
- **Set Up Tailscale**: `sudo tailscale up` (if installed)

## 💡 What Makes Bentobox Special?

### It Flips the Script: LSW > WSL

Microsoft gave us Windows Subsystem for Linux. Bentobox gives you **Linux Subsystem for Windows**. 

Linux becomes your primary OS - your terminal, your development environment, your daily driver. Windows stays available when you need it, but it's no longer in control. For anyone tired of Windows Update interruptions, telemetry concerns, or just wanting more control over their machine, this is the migration path that lets you keep one foot in both worlds.

### Container-First Development

Bentobox comes with **Portainer** pre-configured, giving you a powerful Docker management UI right out of the box. No more memorizing docker commands - manage containers, images, volumes, and networks through an intuitive web interface.

### AI-Ready

With **OpenWebUI** included by default, you're ready to integrate AI into your workflow immediately. Add the optional **Ollama** container to run models like Llama 3.2 locally, keeping your code and prompts private.

### Remote Work Friendly

Optional **Tailscale** integration makes remote development seamless. Access your development environment securely from anywhere - your Portainer dashboard, web apps, even your clipboard sync with Barrier.

### Highly Customizable

The new **extension system** makes Bentobox incredibly flexible:

- **Add New Applications**: Use simple templates to add any package
- **Create Custom Themes**: Design your own color schemes and wallpapers
- **Share Extensions**: Easy pull request workflow for community contributions
- **Automatic Discovery**: Extensions appear automatically in the GUI installer

Whether you want to add Slack, customize your terminal colors, or create a completely personalized setup, Bentobox's metadata-based extension system makes it straightforward.

### The LSW Experience: Windows Apps on Linux

Here's where Bentobox really shines. The optional **WinBoat** feature creates what I call **Linux Subsystem for Windows (LSW)** - the reverse of Microsoft's WSL.

WinBoat runs a Windows 10 VM under the hood, but the experience is seamless:
- Windows apps appear as native Linux windows
- Shared clipboard between Linux and Windows
- Filesystem integration - access your Linux files from Windows
- USB device passthrough
- Native Linux window management

It's nothing revolutionary - just a VM with good integration. But WinBoat makes it *feel* right. You're not switching between two worlds; Windows just becomes another application layer on your Linux desktop.

**For Windows users seeking an exit plan**, this is the compromise that works. You keep Windows for those stubborn apps (Adobe Creative Suite, specialized tools, legacy software) while making Linux your daily driver. No cold turkey required.

## 📚 Documentation & Support

The repository includes comprehensive documentation:

- **Complete Installation Guide**: Step-by-step setup instructions
- **GUI Guide**: Using the desktop installer interface
- **Extension System Documentation**: Complete specs and developer guides
- **Theme System**: Creating and customizing themes
- **Post-Installation Setup**: Configuring AI models, Tailscale, WinBoat
- **Troubleshooting Guide**: Common issues and solutions
- **WinBoat Testing Guides**: Testing procedures and known issues
- **Architecture Documentation**: Bentobox vs Omakub comparison
- **Wallpaper Licensing**: Credits and licensing information

### Known Issues & Workarounds

The documentation covers known issues like:
- Ulauncher crashes on first boot (cosmetic only, easily fixed)
- GDM login screen background customization (Ubuntu 24.04 limitation)
- Complete troubleshooting steps for Docker, Portainer, and containers

## 🙏 Credits & License

Bentobox is released under the **MIT License** and is built on the excellent foundation of Omakub by DHH and contributors. Huge thanks to the original project for creating such a solid base to build upon.

**Wallpapers**: Special thanks to the Unsplash and Pexels photography communities! Bentobox includes 60+ professionally curated wallpapers from 64 talented photographers:
- Licensed under Unsplash License and Pexels License - free to use, modify, and distribute
- Full credits and licensing details available in the repository's `wallpaper/LICENSE.md`

## 🔗 Get Started

Ready to try Bentobox?

- **Repository**: [github.com/languageseed/bentobox](https://github.com/languageseed/bentobox)
- **Original Omakub**: [github.com/basecamp/omakub](https://github.com/basecamp/omakub)
- **Report Issues**: [github.com/languageseed/bentobox/issues](https://github.com/languageseed/bentobox/issues)

## 🌟 Why Bentobox?

The name "Bentobox" reflects our philosophy: a carefully curated selection of tools, each serving a specific purpose, arranged thoughtfully in a beautiful container. Like a Japanese bento box, we've chosen quality over quantity, creating a balanced and professional development environment.

But more importantly, Bentobox represents a shift in thinking. **You don't need Windows as your primary OS anymore**. With LSW (Linux Subsystem for Windows), you get:
- The power and flexibility of Linux as your foundation
- Access to Windows when you absolutely need it
- A beautiful, curated development environment
- Freedom from Windows' quirks while maintaining compatibility

Whether you're setting up a new development machine, containerizing your workflow, exploring AI-assisted development, or finally making the jump from Windows to Linux (without burning bridges), Bentobox provides a thoughtfully curated starting point.

Give it a try and let me know what you think! And if "Linux Subsystem for Windows" catches on... well, you heard it here first. 😉

---

*Have questions or suggestions? Feel free to open an issue on the GitHub repository or reach out directly.*

