# How To: Detect Chained Assignment Is Copy

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test detect chained assignment is copy

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.dropna(...)

```python
df = DataFrame({'a': [1]}).dropna()
```

**Verification:**
```python
assert df._is_copy is None
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1]}).dropna()
assert df._is_copy is None
df['a'] += 1
```

## Next Steps


---

*Source: test_chaining_and_caching.py:403 | Complexity: Beginner | Last updated: 2026-06-02*