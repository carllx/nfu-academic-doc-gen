# How To: Nullable Int Not Cast As Float

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nullable int not cast as float

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, dtype, val
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [val, pd.NA]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'grp': [1, 1], 'b': data}, dtype=dtype)
```

### Step 3: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('grp')
```

### Step 4: Assign result = grouped.transform(...)

```python
result = grouped.transform(method)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': data}, dtype=dtype)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method, dtype, val

# Workflow
data = [val, pd.NA]
df = DataFrame({'grp': [1, 1], 'b': data}, dtype=dtype)
grouped = df.groupby('grp')
result = grouped.transform(method)
expected = DataFrame({'b': data}, dtype=dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_cumulative.py:284 | Complexity: Intermediate | Last updated: 2026-06-02*