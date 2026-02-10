# ML-101
This repository is intended to be a public repository with basic ML knowledge and tutorials.

## Assumptions
It is assumed that:
- You work at Luminai (though the repository is public)
- You are interested in ML
- You are willing to interact with the content
- You are using a Mac

## Setup (MacOS)
This repository might contain some practical exercises, so setting it up locally is recommended.

### Using the Terminal
Most of the instructions below will require you to use your `Terminal`. To open the terminal you can either open the launchpad or Spotlight search (`Cmd + Space`) and then type in `terminal`.

### [brew](https://brew.sh/)
Package manager for MacOS. This will let you install packages easily.

To install `brew` run this command from your terminal.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

You will need to follow the instructions on the terminal. Most notably, enter your password, and accept a few things.

### Downloading the repository
In order to use this code, from the [web interface](https://github.com/DigitalBrainApp/ml-101), click on the Green `<> Code` button on the top-right and then on `Download ZIP`.

Click on the download as it shows up on the top-right in order to navigate to it on `Finder` and unzip it. If it now shows up as a blue folder you're good to go! If you see no blue folder, and only a `.zip` file, double-click it to make sure it unzips.

### Navigating your terminal to the repository
You can navigate your terminal to the newly created directory (folder) with the following command:

```bash
cd ~/Downloads/ml-101-main
```

The anatomy of this command, if you are interested:
- `cd`: Change directory
- `~/`: The user directory
- `/Downloads/`: The `Downloads` directory within your user directory
- `/ml-101-main`: The name of the directory we just created from the downloaded zip file

Alternatively, you can always right-click the directory > `Services` > `New Terminal at Folder`.

### [uv](https://docs.astral.sh/uv/)
uv is a modern python package manager. It will help you install the dependencies for this project and set up the local environment.

To install `uv` run this command from your terminal.

```bash
brew install uv
```

After you've installed `uv`, you can use it from your terminal to sync the project's dependencies. This assumes you're already inside the project directory.

```bash
uv sync
```

### (Optional) VS Code
Visual Studio Code is the recommended code editor. You only need this if you want to visualize the code locally, and potentially make changes to it. If you just want to read the code, the tutorials will have links pointing you to the code on the web.

For installation, follow the [official instructions](https://code.visualstudio.com/docs/setup/mac).

After installing, use it to open the `ml-101-main` folder.

> `File` > `Open Folder` > Search and open `ml-101-main`

## Table of Contents

Now that you've finished the setup, click on one of the topics below to get started!

1. [Math fundamentals](/math_fundamentals)
2. (Tentative) What is training?
3. (Tentative) Measure of success
4. (Tentative) LLMs
