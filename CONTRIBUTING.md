# Contributing to Axon

Thank you for considering contributing to Axon! This document explains our
contribution process.

## Contributor License Agreement

Before we can accept your contribution, you must sign our Contributor License
Agreement (CLA). When you open your first pull request, the CLA bot will
comment with instructions. You sign by posting a comment:

> I have read the CLA Document and I hereby sign the CLA

You only need to do this once across all Taurine Technology repositories.

## Development Setup
```bash
git clone https://github.com/Taurine-Technology/axon-shared.git
cd axon-shared
pip install -e ".[test]"
```

## Making Changes

1. Fork the repository and create a branch from `main`
2. Make your changes
3. Run linting: `flake8 axon_shared/ --max-line-length=120`
4. Run tests: `pytest tests/ -v`
5. If you changed `.proto` files, run `make proto` in `axon_shared/proto/` and
   commit the generated `_pb2.py` files
6. Submit a pull request

## Code Conventions

- Max line length: 120 characters
- Follow existing patterns in the codebase
- Include docstrings for public functions and classes
- Exclude `*_pb2.py` files from linting (auto-generated)

## Reporting Issues

Use GitHub Issues. Please include:
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS

## Questions?

Open a GitHub Discussion or email info@taurinetech.com.