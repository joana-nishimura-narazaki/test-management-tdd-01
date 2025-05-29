````markdown
# Test Management (TDD) — Lesson 1

## 📖 Overview

This repository contains the example project for **Lesson 1: Test Management (TDD)
** from the **MBA in Software Engineering** at **USP/ESALQ**.
It demonstrates how to drive the design and implementation of domain entities (`User` and `Task`) using **Test-Driven Development (TDD)** in Python.

---

## 🎯 Goals

- Illustrate the **Red → Green → Refactor** cycle  
- Show unit test patterns for constructors, data validation, and domain methods  
- Enforce business rules via automated tests  
- Organize code and tests for clarity and maintainability  

---

## 🛠️ Technology Stack

- **Language**: Python 3.13  
- **Testing**: pytest  
- **Dependency Management**: pip / virtualenv  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ installed  
- `virtualenv` (optional but recommended)

### Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\Activate   # Windows
   source .venv/bin/activate # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Running Tests

Execute all unit and integration tests with:

```bash
pytest
```

You should see all tests pass:

```
collected 10 items / 10 passed
```

---

## 📂 Project Structure

```
├── domain/                  # Domain entities and business logic
│   ├── user/                # User entity and validations
│   └── task/                # Task entity and validations
├── tests/                   # Test suites
│   ├── domain/unit/         # Unit tests for User and Task
│   └── domain/integration/  # Integration tests between entities
├── requirements.txt         # Project dependencies
└── README.md                # This documentation
```

---

## ✍️ Test Highlights

* **Initialization Tests**: Ensure valid instances set all attributes correctly
* **Validation Tests**: Enforce UUID format, non-empty strings, boolean flags
* **Domain Method Test**: Verify `Task.mark_as_completed()` toggles state

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork this repository
2. Create a feature branch (`git checkout -b feat/your-feature`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to your branch (`git push origin feat/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

Joana Nishimura Narazaki

* Email: [joana.narazaki45@gmail.com](mailto:joana.narazaki45@gmail.com)
* LinkedIn: [https://linkedin.com/in/joana-narazaki](https://linkedin.com/in/joana-narazaki)
* GitHub: [https://github.com/joana-nishimura-narazaki](https://github.com/joana-nishimura-narazaki)

```
```
