# How To: Select With Dups

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate concat: test select with dups

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign df = concat(...)

```python
df = concat([DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=['A', 'A', 'B', 'B']), DataFrame(np.random.default_rng(2).integers(0, 10, size=20).reshape(10, 2), columns=['A', 'C'])], axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df = concat([DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=['A', 'A', 'B', 'B']), DataFrame(np.random.default_rng(2).integers(0, 10, size=20).reshape(10, 2), columns=['A', 'C'])], axis=1)
```

## Next Steps


---

*Source: test_select.py:85 | Complexity: Beginner | Last updated: 2026-06-02*