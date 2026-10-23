# Repository Guidelines

## Project Structure & Module Organization

This repository contains 42 Python for Data Science exercises, organized by module:

- `python-0/ex00` through `ex09`: Python fundamentals, command-line programs, and packaging.
- `python-1/ex00` through `ex02`: BMI calculations, array operations, and image loading.
- Each module includes its subject PDF, `requirements.txt`, and `Dockerfile`.
- Exercise source files and manual `tester.py` scripts live together. Image fixtures belong in the relevant exercise directory.
- `python-0/ex09/ft_package/` contains the packaging exercise, with build metadata in `pyproject.toml` and `setup.py`.

## Build, Test, and Development Commands

Use Python 3.10, matching the Docker images. For local development:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r python-1/requirements.txt
```

Use `python-0/requirements.txt` when working on that module. Keep the local environment out of commits.

- `make up`: build and start the container; Compose currently mounts `python-1` at `/app`.
- `make exec`: open a shell in the running container.
- `make down`: stop the Compose services.
- `python -m flake8 python-0 python-1`: lint both modules.
- `cd python-1/ex00 && python tester.py`: run an exercise's manual checks with local imports resolved.
- `cd python-0/ex09 && python -m build`: build the package distributions.

Image-display exercises require a graphical display; Compose includes Linux X11 configuration.

## Coding Style & Naming Conventions

Use four-space indentation, PEP 8 formatting, and Flake8's default checks. Prefer descriptive `snake_case` functions and variables, concise docstrings, and type hints where useful. Preserve subject-required filenames and function signatures, including names such as `Hello.py`, `NULL_not_found.py`, and `ft_load`. Guard executable entry points with `if __name__ == "__main__":` where appropriate.

## Testing Guidelines

There is no centralized test framework or coverage threshold. Run an exercise's `tester.py` when requested and compare results with its subject PDF. Check valid inputs, invalid types, boundary cases, and required error output. Verify image fixture paths before image tests. Suggest additional checks in chat.

## Commit & Pull Request Guidelines

History uses short, exercise-focused messages such as `python1-ex02` and `fix norm`; no formal commit standard is enforced. Prefer concise messages identifying the module, exercise, and change. Keep commits scoped. Pull requests should describe the affected exercises, link relevant issues, and list validation commands and results. Include screenshots when changing visual output.

## Exercise Constraints

Use the relevant `*.en.subject.pdf` as the authoritative project requirements. Read it before advising on exercises; follow its allowed-library restrictions and required output format.

## Learning & Language Rules

- Give explanations and hints first. Do not reveal solution code unless explicitly requested.
- Never create or edit exercise code for the learner. Show requested code previews only in chat; the learner implements them.
- When Thai explanations are requested, explain in Thai while keeping technical terms in English.
