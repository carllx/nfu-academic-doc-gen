# How To: Show Versions

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: test show versions

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `re`
- `pandas.util._print_versions`
- `pandas`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign expected = value

```python
expected = {'system': _get_sys_info(), 'dependencies': _get_dependency_info()}
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
expected = {'system': _get_sys_info(), 'dependencies': _get_dependency_info()}
```

## Next Steps


---

*Source: test_show_versions.py:24 | Complexity: Beginner | Last updated: 2026-06-02*