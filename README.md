# MarketingAI
<div align="center">

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/CogitoNTNU/MarketingAI/main.yml)
![GitHub top language](https://img.shields.io/github/languages/top/CogitoNTNU/MarketingAI)
![GitHub language count](https://img.shields.io/github/languages/count/CogitoNTNU/MarketingAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Version](https://img.shields.io/badge/version-1.0.0-blue)](https://img.shields.io/badge/version-1.0.0-blue)

<img src="https://atlasimagesgallery.blob.core.windows.net/images/MarketingAILogo.png" width="50%" alt="Cogito Image" style="display: block; margin-left: auto; margin-right: auto;">

</div>

## Table of contents
1. [Introduction](#introduction)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Tests](#tests)
6. [Repository Structure](#repository-structure)
7. [Contributors](#contributors)


## Introduction
MarketingAI is a sophisticated software application designed to empower users in creating impactful marketing materials. MarketingAI caters to marketers, content creators, and anyone looking for an automated, creative solution for their advertising needs.

**Our goal:** A software application is that allows users to input specific themes or topics for a meme or Marketing poster. Following this input, the application should be capable of autonomously generating relevant imagery and accompanying text. Subsequently, it should seamlessly integrate these elements to produce a cohesive poster

## Setup
To setup the project, one needs to have all the prerequisites installed. Then one needs to clone the repository, setup a virtual environment, and install the dependencies. This is described in more detail below.

### Prerequisites
- Ensure Python 3.9 or newer is installed on your machine. [Download Python](https://www.python.org/downloads/)
- Familiarity with basic Python package management and virtual environments is beneficial.

### Clone the repository
```bash
git clone https://github.com/CogitoNTNU/MarketingAI.git
cd MarketingAI
```

### Virtual Environment (Recommended)

<details> 
<summary><strong>🚀 A better way to set up repositories </strong></summary>

Using a virtual environment helps manage dependencies and keeps your system tidy.
```bash
pip install virtualenv
```

### Create virtual environment
```bash
python -m venv venv
```

For windows:
```bash
source ./venv/Scripts/activate
```

For Linux / MacOS:
```bash
source venv/bin/activate
```

### Settup VSCode with virtual environment
With VSCode opened press ```Ctrl+Shift+P``` and search for ```python: Select Interpreter``` and click on it

Then select the relevant virtual environment as shown

![Vscode setup](/docs/img/vscodeSettup.png)

Now you can utilize all the installed goodies from the environment ;)

</details>

### Install dependencies
Once inside the virtual environment, you can install the required packages:
```bash
pip install -r requirements.txt
```

### Create a .env file
Create a file called `.env` in the root of the project. This file should contain the following:
* API_KEY: The API key for the OpenAI API.

If you do not have an OpenAI API Key visit [OpenAI/API-Keys](https://platform.openai.com/api-keys) and generate a key.
NOTE: Never Commit .env to Version Control. The .env file should be kept private and never be committed to public repositories as it contains secretes like API keys.
  
```bash
touch .env
echo "API_KEY=YOUR_API_KEY" > .env # Remember to change YOUR_API_KEY to your actual API key
```



## Usage
To use the project, you can run the following command:
```bash
python main.py
```

## Tests
To run the full test suit, run the following command:
```bash
pytest
```

To run all tests except api tests, run the following command:
```bash
pytest -m "not apitest"
```

## Repository structure
* **docs/:** Store all your documentation here. Architectural diagrams, architectural decisions reasoning, and API references.

* **src/:** Main source code directory.
  * **assembler/:** Code that takes the generated text and image and assembles the picture.
  * **fine_tuning/:** Code for fine-tuning the GPT model, and data used for it.
  * **function_calling/:** All code for letting agents call the functions and agent chains.
  * **gpt/:** Code related to chat Completion.
  * **image_generation/:** Code for generating images from prompts.
* **tests/:** Unit tests, integration tests, and any other testing code.
* **images/:** All images created by the program both raw images and the assembled images.

## Contributors
<table>
  <tr>
    <td align="center">
        <a href="https://github.com/Spiderpig02">
            <img src="https://github.com/Spiderpig02.png?size=100" width="100px;" alt="Daniel Neukirch Hansen"/><br />
            <sub><b>Daniel Neukirch Hansen</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Eduard-Prokhorikhin">
            <img src="https://github.com/Eduard-Prokhorikhin.png?size=100" width="100px;" alt="Eduard Prokhorikhin"/><br />
            <sub><b>Eduard Prokhorikhin</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/HFossdal">
            <img src="https://github.com/HFossdal.png?size=100" width="100px;" alt="Håvard Fossdal"/><br />
            <sub><b>Håvard Fossdal</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/JHJORE">
            <img src="https://github.com/JHJORE.png?size=100" width="100px;" alt="Jørgen Haugdal Jore"/><br />
            <sub><b>Jørgen Haugdal Jore</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Knolaisen">
            <img src="https://github.com/Knolaisen.png?size=100" width="100px;" alt="Kristoffer Nohr Olaisen"/><br />
            <sub><b>Kristoffer Nohr Olaisen</b></sub>
        </a>
    </td>
    <!-- More contributors... -->
    <td align="center">
        <a href="https://github.com/olavsl">
            <img src="https://github.com/olavsl.png?size=100" width="100px;" alt="Olav Selnes Lorentzen"/><br />
            <sub><b>Olav Selnes Lorentzen</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/svemyh">
            <img src="https://github.com/svemyh.png?size=100" width="100px;" alt="Sveinung Myhre"/><br />
            <sub><b>Sveinung Myhre</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/SverreNystad">
            <img src="https://github.com/SverreNystad.png?size=100" width="100px;"/><br />
            <sub><b>Sverre Nystad</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/sandviklee">
            <img src="https://github.com/sandviklee.png?size=100" width="100px;" alt="Simon Sandvik Lee"/><br />
            <sub><b>Simon Sandvik Lee</b></sub>
        </a>
    </td>
  
  </tr>
</table>

This project could not have been possible without all of the wonderful contributors. Thank you all for your hard work!
