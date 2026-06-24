# How To: Groupby Boxplot Sharey

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DataFrame: test groupby boxplot sharey

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas.tests.plotting.common`

**Setup Required:**
```python
# Fixtures: kwargs, expected
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [-1.43, -0.15, -3.7, -1.43, -0.14], 'b': [0.56, 0.84, 0.29, 0.56, 0.85], 'c': [0, 1, 2, 3, 1]}, index=[0, 1, 2, 3, 4])
```


## Complete Example

```python
# Setup
# Fixtures: kwargs, expected

# Workflow
df = DataFrame({'a': [-1.43, -0.15, -3.7, -1.43, -0.14], 'b': [0.56, 0.84, 0.29, 0.56, 0.85], 'c': [0, 1, 2, 3, 1]}, index=[0, 1, 2, 3, 4])
```

## Next Steps


---

*Source: test_frame_groupby.py:35 | Complexity: Beginner | Last updated: 2026-06-02*