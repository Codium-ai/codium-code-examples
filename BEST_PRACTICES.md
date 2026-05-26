###  Project Best Practices

#### 1. Project Purpose
_Short paragraph summarizing what the project does and its domain_

This repository contains multiple small Python example projects and exercises focused on algorithmic practice and simple domain models (library, bank account, quick sort, YAML utilities). The codebase is organized as a collection of examples and tests intended for learning, automated test generation, and demonstration of best-practice patterns in small, self-contained modules.

#### 2. Project Structure
- Overview of folder layout
  - src/ and examples/ contain the primary code examples and test suites. examples/ holds multiple small packages (library, bank_account, quick_sort, yaml_strip, etc.).
  - docs/ and media/docs/ contain supporting documentation and images for tutorials or guides.
  - .qodo/ and .claude/ hold tooling/config for generation agents and workflows.
  - README.md at project root explains repository purpose and quick navigation.

- Description of roles of key directories/files
  - examples/: Primary collection of small Python projects. Each subdirectory is a mini-package with modules and tests.
  - examples/*/test or tests: Unit tests for the corresponding example. Prefer colocated tests within each package folder.
  - src/: (If present) intended for production or library code separate from examples.
  - .qodo/ and .pr_agent.toml: CI/automation/agent configuration—do not modify unless updating agent behavior.
  - media/docs/: Images and animated GIFs used in documentation and guides.

#### 3. Test Strategy
- Framework(s) used
  - Tests are written using pytest and some unittest style tests. The repository relies primarily on pytest conventions (test_*.py filenames and assert-based tests).

- How and where tests are organized
  - Tests are colocated in each example's directory (e.g., examples/library_2/test_library_2.py). There are also dedicated test folders inside packages (examples/bank_account_2/test).
  - Naming conventions: test_*.py for test files and *_modified or *_helpers for auxiliary code used in tests.

- Mocking guidelines
  - Use pytest's monkeypatch fixture or unittest.mock for simple mocking. Keep mocks focused and avoid over-mocking; prefer injecting small, test-friendly interfaces when possible.
  - For examples that interact with in-memory DBs (like in_memory_user_db.py), write tests that exercise the in-memory implementations rather than mocking them away.

- When/how to write unit vs integration tests
  - Unit tests: Test pure functions and individual classes (e.g., quick_sort, yaml_strip functions, library utilities) in isolation. Keep tests small, deterministic, and fast.
  - Integration tests: Add integration tests where multiple components interact (e.g., user-management + in-memory DB, library borrowing flows). Use fixtures to set up realistic in-memory state.
  - Criterion: Prefer unit tests by default; add integration tests for behavior that spans modules or requires realistic state transitions.

#### 4. Code Style
- Language-specific rules
  - Python 3.8+ idioms are used: type hints in many modules, simple generator/iterator usage, and small functional helpers.
  - Prefer explicit is better than implicit: avoid complex one-liners that reduce clarity.
  - Keep functions pure where possible; for stateful modules (bank account, library), encapsulate state and expose minimal public API.

- Naming conventions
  - Files and modules: snake_case (e.g., bank_account.py, quick_sort.py).
  - Functions and variables: snake_case. Classes: PascalCase.
  - Tests: start with test_ prefix for files and functions.

- Commenting and docstring habits
  - Add module-level docstrings explaining purpose and public API for each example package.
  - Public classes and functions should have concise docstrings covering arguments, return values, and side effects.
  - Keep inline comments for non-obvious logic and algorithms. Avoid obvious comments that restate code.

- Error and exception handling
  - Validate inputs at public API boundaries and raise ValueError/TypeError with clear messages for misuse.
  - For domain errors (e.g., overdraft in bank account), define specific exception classes when meaningful (e.g., OverdraftError) and document when they are raised.
  - Do not swallow exceptions silently; prefer to let exceptions bubble up or be transformed into domain-specific errors.

#### 5. Common Patterns
- Reusable utilities or base classes
  - In-memory DB patterns used across examples: simple dict-backed storage with CRUD helpers. Factor this into a small utility if reused widely.
  - Factory functions (e.g., library_factory.py) to construct configured instances for testing and examples.

- Design patterns or architectural approaches
  - Separation of concerns: examples often separate domain logic (models) from storage (in_memory_*_db). Keep this boundary clear.
  - Use composition over inheritance: prefer small service objects that wrap storage and provide behavior.

- Frequently used idioms
  - Tests use fixtures and helper factories to generate sample data (see random_data_gen.py).
  - Keep side-effecting operations explicit and minimize global mutable state.

#### 6. Do's and Don'ts
- ✅ Things developers should always do
  - ✅ Write tests for new behavior; aim for clear, focused unit tests.
  - ✅ Keep modules small and single-responsibility.
  - ✅ Use type hints for public APIs and CI checks for linting/formatting (black, flake8/ruff, mypy where applicable).
  - ✅ Document public module behavior with docstrings and update README when adding examples.
  - ✅ Use fixtures and factory helpers to reduce duplication in tests.

- ❌ Common mistakes to avoid
  - ❌ Overloading example modules with multiple responsibilities; split when complexity grows.
  - ❌ Over-mocking core logic; prefer testing against in-memory implementations to validate behavior.
  - ❌ Relying on external state or network in unit tests. Keep external interactions mocked or use in-memory substitutes.

#### 7. Tools & Dependencies
- Key libraries and their purpose
  - pytest: primary test runner and assertion framework.
  - unittest.mock: mocking and patching when needed.
  - No heavy web frameworks detected; this repo is focused on small Python examples.

- Project setup instructions (if relevant)
  - Create a virtualenv: python -m venv .venv && source .venv/bin/activate
  - Install test deps: pip install -U pytest
  - Run tests: pytest -q

#### 8. Other Notes
- For an LLM generating code in this repo
  - Keep changes minimal and localized to the example module requested. Follow the project's naming and testing conventions.
  - Preserve simple, explicit logic over clever optimizations. Include or update tests with any behavioral change.
  - When adding new examples, include a README and accompanying tests demonstrating usage.

- Special edge cases or constraints
  - Many examples intentionally use in-memory or simplified implementations—do not add heavy dependencies or external services unless creating a new, well-documented example.

