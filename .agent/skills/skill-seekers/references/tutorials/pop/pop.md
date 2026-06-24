# How To: Pop

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test pop

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign a = DataFrame(...)

```python
a = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'], index=['X', 'Y'])
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, warn_copy_on_write

# Workflow
a = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'], index=['X', 'Y'])
```

## Next Steps


---

*Source: test_pop.py:24 | Complexity: Beginner | Last updated: 2026-06-02*