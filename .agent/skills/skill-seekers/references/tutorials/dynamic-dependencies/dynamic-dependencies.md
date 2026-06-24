# How To: Dynamic Dependencies

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: test dynamic dependencies

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `inspect`
- `pytest`
- `jaraco`
- `setuptools.config.pyprojecttoml`
- `setuptools.dist`
- `setuptools.warnings`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'requirements.txt': 'six\n  # comment\n', 'pyproject.toml': cleandoc('\n            [project]\n            name = "myproj"\n            version = "1.0"\n            dynamic = ["dependencies"]\n\n            [build-system]\n            requires = ["setuptools", "wheel"]\n            build-backend = "setuptools.build_meta"\n\n            [tool.setuptools.dynamic.dependencies]\n            file = ["requirements.txt"]\n            ')}
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
files = {'requirements.txt': 'six\n  # comment\n', 'pyproject.toml': cleandoc('\n            [project]\n            name = "myproj"\n            version = "1.0"\n            dynamic = ["dependencies"]\n\n            [build-system]\n            requires = ["setuptools", "wheel"]\n            build-backend = "setuptools.build_meta"\n\n            [tool.setuptools.dynamic.dependencies]\n            file = ["requirements.txt"]\n            ')}
```

## Next Steps


---

*Source: test_pyprojecttoml_dynamic_deps.py:12 | Complexity: Beginner | Last updated: 2026-06-02*