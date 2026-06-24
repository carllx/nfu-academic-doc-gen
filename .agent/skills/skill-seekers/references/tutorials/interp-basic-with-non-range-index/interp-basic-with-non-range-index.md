# How To: Interp Basic With Non Range Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test interp basic with non range index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, np.nan, 4], 'B': [1, 4, 9, np.nan], 'C': [1, 2, 3, 5], 'D': list('abcd')})
```

### Step 2: Assign msg = 'DataFrame.interpolate with object dtype'

```python
msg = 'DataFrame.interpolate with object dtype'
```

### Step 3: Assign warning = value

```python
warning = FutureWarning if not using_infer_string else None
```

### Step 4: Assign expected = df.set_index(...)

```python
expected = df.set_index('C')
```

### Step 5: Assign unknown = 3

```python
expected.loc[3, 'A'] = 3
```

### Step 6: Assign unknown = 9

```python
expected.loc[5, 'B'] = 9
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = df.set_index.interpolate(...)

```python
result = df.set_index('C').interpolate()
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
df = DataFrame({'A': [1, 2, np.nan, 4], 'B': [1, 4, 9, np.nan], 'C': [1, 2, 3, 5], 'D': list('abcd')})
msg = 'DataFrame.interpolate with object dtype'
warning = FutureWarning if not using_infer_string else None
with tm.assert_produces_warning(warning, match=msg):
    result = df.set_index('C').interpolate()
expected = df.set_index('C')
expected.loc[3, 'A'] = 3
expected.loc[5, 'B'] = 9
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_interpolate.py:124 | Complexity: Advanced | Last updated: 2026-06-02*