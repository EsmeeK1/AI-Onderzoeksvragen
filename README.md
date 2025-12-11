# README - AI Research Questions

This repository serves as a learning environment for exploring AI research topics, which can differ from zero shot learning to dashboarding to evaluation methods. Anything that has something to do in the AI-World.

I will treat each research question as a **mini-project** with notebooks, code, and results.

---

## Project Structure
```bash
ai-onderzoeksvragen
│
├── bootstrap.cmd # Setup script (.venv + VSCode settings)
├── requirements.txt # Shared dependencies
├── README.md # Project overview (this file)
│
├── research_questions/ # Each backlog item is a mini-project
│ ├── Project-1/
│ │ ├── notebooks/ # Jupyter experiments
│ │ ├── src/ # Scripts/modules
│ │ ├── results/ # Outputs (plots, logs, metrics)
│ │ └── README.md # Mini-project description
│ ├── Project-2/
│ └── ...
│
├── shared/ # Utilities & common resources
│ ├── utils/
│ └── config/
│
└── .vscode/ # VS Code integration (auto from bootstrap.cmd)
```

## Setup
1. Clone this repository:
```bash
git clone https://bitbucket.org/<your-username>/ai-research-questions.git
cd ai-research-questions
```
2. Run the bootstrap script in `Command Prompt` (not Powershell)
```bash
bootstrap.cmd
```
3. Open the repo in VS Code and select the Python enviroment (.venv) and install the dependencies
```bash
pip install -r requirements.txt
```

# Research Topics (Backlog)
The questions in this repo will update along the way, so there's no way of saying whats currently in the repo or will be. Since this repo will be actively updated. But each will be documented in its own subdirectory under research_questions/.

# Mini-Project README
Each research question folder contains its own README.md with:

* Research question
* Approach / methods
* Experiments
* Results
* Reflection / learning points

