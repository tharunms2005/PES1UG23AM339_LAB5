### 🧠 Objective

To enhance the quality, security, and maintainability of Python code by performing **static code analysis** using **Pylint**, **Flake8**, and **Bandit** on the given `inventory_system.py` file.

---

### 🧩 Tools Used

| Tool       | Purpose                                         |
| ---------- | ----------------------------------------------- |
| **Pylint** | Detects logical and structural issues in code   |
| **Flake8** | Enforces PEP8 coding style and formatting rules |
| **Bandit** | Identifies potential security vulnerabilities   |

---

### ⚙️ Steps Followed

#### **Step 1 – Environment Setup**

* Created a new GitHub repository
* Cloned it locally
* Installed analysis tools using:

  ```bash
  pip install pylint flake8 bandit
  ```
* Ran the initial program to observe its behavior:

  ```bash
  python inventory_system.py
  ```

#### **Step 2 – Running Static Analysis Tools**

Executed:

```bash
pylint inventory_system.py > pylint_report.txt
bandit -r inventory_system.py > bandit_report.txt
flake8 inventory_system.py > flake8_report.txt
```

Generated three reports for code quality, security, and style issues.

#### **Step 3 – Identifying and Documenting Issues**

Reviewed all reports and listed common problems found in the code.

---

### 📋 Known Issues Table

| Issue                                | Type             | Line(s) | Description                                      | Fix Approach                                            |
| ------------------------------------ | ---------------- | ------- | ------------------------------------------------ | ------------------------------------------------------- |
| Mutable default argument             | Bug              | 12      | `logs=[]` is shared across function calls        | Use `logs=None` and initialize inside function          |
| Bare `except:` used                  | Logic / Security | 25      | Hides all exceptions, making debugging difficult | Replace with `except KeyError:` or specific exception   |
| Insecure use of `eval()`             | Security         | 70      | Executes arbitrary code, high security risk      | Remove `eval()` completely                              |
| No input validation                  | Logic            | 15–25   | Non-string items or invalid quantities allowed   | Use `isinstance()` to validate data types               |
| Files opened without context manager | Maintainability  | 45–53   | Files not closed safely                          | Use `with open(...) as f:`                              |
| Missing logging configuration        | Maintainability  | 8–10    | Uses manual print/log appends                    | Use Python’s `logging` module instead                   |
| Use of magic numbers                 | Style            | 58      | Hardcoded threshold (5)                          | Use constant variable (e.g., `LOW_STOCK_THRESHOLD = 5`) |

---

### 🧼 Step 4 – Fixing Issues

Created a new file named **`cleaned_inventory_system.py`** implementing:

* Proper input validation
* Context managers for file handling
* Removal of `eval()`
* Use of f-strings and proper exception handling
* Logging improvements
* Better readability and maintainability

Reran all analysis tools:

```bash
pylint cleaned_inventory_system.py > pylint_report.txt
bandit -r cleaned_inventory_system.py > bandit_report.txt
flake8 cleaned_inventory_system.py > flake8_report.txt
```

Most issues were resolved or reduced in severity.

---

### 🪞 Reflection

**1. Which issues were easiest vs hardest to fix?**
The easiest were formatting and mutable default argument fixes. The hardest was redesigning file handling and removing `eval()` safely without affecting functionality.

**2. Any false positives?**
Yes, Bandit flagged basic string formatting as a potential security risk even though no user input was executed. This was a minor false positive.

**3. How would you integrate these tools into real development?**
I would integrate Pylint, Bandit, and Flake8 into a CI/CD pipeline (e.g., GitHub Actions) so that every commit automatically triggers static checks before merging.

**4. Improvements observed after fixing issues:**
The code is now cleaner, safer, and easier to maintain. It follows Pythonic standards (PEP8), handles exceptions properly, and avoids unsafe functions.

---

### 📦 Repository Structure

```
📁 static-code-analysis-lab
│
├── inventory_system.py                # Original code
├── cleaned_inventory_system.py        # Fixed version
├── pylint_report.txt
├── bandit_report.txt
├── flake8_report.txt
├── pylint_report_new.txt
├── bandit_report_new.txt
├── flake8_report_new.txt
├── reflection.md
├── README.md
```
