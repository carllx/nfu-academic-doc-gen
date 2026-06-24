# How To: Select Columns In Where

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate MultiIndex: test select columns in where

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

### Step 1: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[['foo', 'bar', 'baz', 'qux'], ['one', 'two', 'three']], codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]], names=['foo_name', 'bar_name'])
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
index = MultiIndex(levels=[['foo', 'bar', 'baz', 'qux'], ['one', 'two', 'three']], codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]], names=['foo_name', 'bar_name'])
```

## Next Steps


---

*Source: test_select.py:34 | Complexity: Beginner | Last updated: 2026-06-02*