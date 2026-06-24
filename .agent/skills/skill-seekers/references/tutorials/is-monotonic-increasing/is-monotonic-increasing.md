# How To: Is Monotonic Increasing

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: test is monotonic increasing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: in_vals, out_vals
```

## Step-by-Step Guide

### Step 1: Assign source_dict = value

```python
source_dict = {'A': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], 'B': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd'], 'C': in_vals}
```


## Complete Example

```python
# Setup
# Fixtures: in_vals, out_vals

# Workflow
source_dict = {'A': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], 'B': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd'], 'C': in_vals}
```

## Next Steps


---

*Source: test_is_monotonic.py:32 | Complexity: Beginner | Last updated: 2026-06-02*