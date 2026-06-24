# How To: Groupby Sample With Empty Inputs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby sample with empty inputs

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [], 'b': []})
```

### Step 2: Assign groupby_df = df.groupby(...)

```python
groupby_df = df.groupby('a')
```

### Step 3: Assign result = groupby_df.sample(...)

```python
result = groupby_df.sample()
```

### Step 4: Assign expected = df

```python
expected = df
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [], 'b': []})
groupby_df = df.groupby('a')
result = groupby_df.sample()
expected = df
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sample.py:147 | Complexity: Intermediate | Last updated: 2026-06-02*