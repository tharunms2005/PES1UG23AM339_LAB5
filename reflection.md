# Reflection – Static Code Analysis Lab

### 1. Which issues were the easiest to fix, and which were the hardest?  
The easiest issues to fix were style-based ones reported by Flake8, such as missing blank lines and improper spacing.  
The hardest were the security and logic issues like removing the `eval()` function and handling mutable default arguments safely without breaking functionality.

---

### 2. Did the static analysis tools report any false positives?  
Yes, Bandit occasionally flagged some non-critical operations as potential risks, even though they were harmless in this simple program. For example, it warned about basic file handling as a potential vulnerability.

---

### 3. How would you integrate static analysis tools into your workflow?  
I would integrate Pylint, Bandit, and Flake8 into a continuous integration (CI) workflow using GitHub Actions. Each commit or pull request would automatically trigger these tools to ensure the code meets quality and security standards before merging.

---

### 4. What tangible improvements did you observe after applying the fixes?  
The code became much cleaner, easier to read, and more reliable.  
Security risks like `eval()` were removed, file handling became safer using context managers, and input validation made the program more robust.  
Following PEP 8 conventions improved consistency and maintainability overall.
