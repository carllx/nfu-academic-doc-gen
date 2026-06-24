# How To: No False Positive Frameworks

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Test that framework detection doesn't produce false positives (Issue #239).

## Prerequisites

**Required Modules:**
- `json`
- `os`
- `shutil`
- `tempfile`
- `unittest`
- `pathlib`
- `skill_seekers.cli.codebase_scraper`
- `skill_seekers.cli.codebase_scraper`
- `skill_seekers.cli.codebase_scraper`


## Step-by-Step Guide

### Step 1: "Test that framework detection doesn't produce false positives (Issue #239)."

```python
"Test that framework detection doesn't produce false positives (Issue #239)."
```

### Step 2: Assign app_dir = value

```python
app_dir = self.test_project / 'app'
```

### Step 3: Call app_dir.mkdir()

```python
app_dir.mkdir()
```

### Step 4: Call unknown.write_text()

```python
(app_dir / 'utils.py').write_text("def my_function():\n    return 'hello'\n")
```

### Step 5: Call analyze_codebase()

```python
analyze_codebase(directory=self.test_project, output_dir=self.output_dir, depth='deep', enhance_level=0)
```

### Step 6: Assign arch_file = value

```python
arch_file = self.output_dir / 'references' / 'architecture' / 'architectural_patterns.json'
```

### Step 7: Assign frameworks = arch_data.get(...)

```python
frameworks = arch_data.get('frameworks_detected', [])
```

### Step 8: Call self.assertNotIn()

```python
self.assertNotIn('Flask', frameworks, 'Should not detect Flask without imports')
```

### Step 9: Assign arch_data = json.load(...)

```python
arch_data = json.load(f)
```

### Step 10: Call self.assertNotIn()

```python
self.assertNotIn(fw, frameworks, f'Should not detect {fw} without real evidence')
```


## Complete Example

```python
# Workflow
"Test that framework detection doesn't produce false positives (Issue #239)."
app_dir = self.test_project / 'app'
app_dir.mkdir()
(app_dir / 'utils.py').write_text("def my_function():\n    return 'hello'\n")
from skill_seekers.cli.codebase_scraper import analyze_codebase
analyze_codebase(directory=self.test_project, output_dir=self.output_dir, depth='deep', enhance_level=0)
arch_file = self.output_dir / 'references' / 'architecture' / 'architectural_patterns.json'
if arch_file.exists():
    with open(arch_file) as f:
        arch_data = json.load(f)
    frameworks = arch_data.get('frameworks_detected', [])
    self.assertNotIn('Flask', frameworks, 'Should not detect Flask without imports')
    for fw in ['ASP.NET', 'Rails', 'Laravel']:
        self.assertNotIn(fw, frameworks, f'Should not detect {fw} without real evidence')
```

## Next Steps


---

*Source: test_framework_detection.py:115 | Complexity: Advanced | Last updated: 2026-06-02*