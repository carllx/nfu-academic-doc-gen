# How To: Iset Splits Blocks Inplace

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: test iset splits blocks inplace

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, locs, arr, dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12], 'e': [13, 14, 15], 'f': Series(['a', 'b', 'c'], dtype=object)})
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, locs, arr, dtype

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12], 'e': [13, 14, 15], 'f': Series(['a', 'b', 'c'], dtype=object)})
```

## Next Steps


---

*Source: test_internals.py:101 | Complexity: Beginner | Last updated: 2026-06-02*