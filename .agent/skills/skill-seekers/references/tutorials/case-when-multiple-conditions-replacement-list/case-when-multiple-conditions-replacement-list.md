# How To: Case When Multiple Conditions Replacement List

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate case_when: Test output when replacement is a list

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign result = Series.case_when(...)

```python
result = Series([np.nan, np.nan, np.nan]).case_when([([True, False, False], 1), (df['a'].gt(1) & df['b'].eq(5), [1, 2, 3])])
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
result = Series([np.nan, np.nan, np.nan]).case_when([([True, False, False], 1), (df['a'].gt(1) & df['b'].eq(5), [1, 2, 3])])
```

## Next Steps


---

*Source: test_case_when.py:85 | Complexity: Beginner | Last updated: 2026-06-02*