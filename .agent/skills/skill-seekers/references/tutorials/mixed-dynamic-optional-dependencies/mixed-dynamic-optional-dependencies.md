# How To: Mixed Dynamic Optional Dependencies

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: Test that if PEP 621 was loosened to allow mixing of dynamic and static
configurations in the case of fields containing sub-fields (groups),
things would work out.

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
files = {'requirements-images.txt': 'pillow~=42.0\n  # comment\n', 'pyproject.toml': cleandoc('\n            [project]\n            name = "myproj"\n            version = "1.0"\n            dynamic = ["optional-dependencies"]\n\n            [project.optional-dependencies]\n            docs = ["sphinx"]\n\n            [tool.setuptools.dynamic.optional-dependencies.images]\n            file = ["requirements-images.txt"]\n            ')}
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
files = {'requirements-images.txt': 'pillow~=42.0\n  # comment\n', 'pyproject.toml': cleandoc('\n            [project]\n            name = "myproj"\n            version = "1.0"\n            dynamic = ["optional-dependencies"]\n\n            [project.optional-dependencies]\n            docs = ["sphinx"]\n\n            [tool.setuptools.dynamic.optional-dependencies.images]\n            file = ["requirements-images.txt"]\n            ')}
```

## Next Steps


---

*Source: test_pyprojecttoml_dynamic_deps.py:67 | Complexity: Beginner | Last updated: 2026-06-02*