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

### [brew](https://brew.sh/)
Package manager for MacOS. This will let you install packages easily.

To install `brew` run this command from your terminal.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### [git](https://git-scm.com/)
Git is a code version control tool. We'll use it mainly just to fetch this repository from the web.

To install git run this command from your terminal.

```bash
brew install git
```

After you've installed `git`, you can use it from your terminal to fetch a local copy of this repository:

```bash
git clone git@github.com:DigitalBrainApp/ml-101.git
```

This will create a local directory called `ml-101`.

### [uv](https://docs.astral.sh/uv/)
uv is a modern python package manager. It will help you install the dependencies for this project and set up the local environment.

To install `uv` run this command from your terminal.

```bash
brew install uv
```

After you've installed `uv`, you can use it from your terminal to sync the project's dependencies:

```bash
uv sync
```

### VS Code
Visual Studio Code is the recommended code editor.

For installation, follow the [official instructions](https://code.visualstudio.com/docs/setup/mac).

After installing, use it to open the `ml-101` folder.

> `File` > `Open Folder` > Search and open `ml-101`
