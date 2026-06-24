# How To: Get Type Hints Str

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: Test `typing.get_type_hints` with string-representation of types.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `typing`
- `pytest`
- `numpy`
- `numpy._typing`
- `numpy.typing`

**Setup Required:**
```python
# Fixtures: name, tup
```

## Step-by-Step Guide

### Step 1: Assign ref = value

```python
ref = {'a': getattr(npt, str(name)), 'return': type(None)}
```


## Complete Example

```python
# Setup
# Fixtures: name, tup

# Workflow
ref = {'a': getattr(npt, str(name)), 'return': type(None)}
```

## Next Steps


---

*Source: test_runtime.py:84 | Complexity: Beginner | Last updated: 2026-06-02*