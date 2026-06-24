# How To: Empty Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: check_dtype
```

## Step-by-Step Guide

### Step 1: Assign columns = value

```python
columns = ['col1', 'col2']
```

### Step 2: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(columns=columns)
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(columns=columns)
```

### Step 4: Assign kwargs = value

```python
kwargs = {'check_dtype': check_dtype}
```

### Step 5: Assign unknown = unknown.astype(...)

```python
df1['col1'] = df1['col1'].astype('int64')
```

### Step 6: Assign msg = 'Attributes of DataFrame\\..* are different'

```python
msg = 'Attributes of DataFrame\\..* are different'
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df2, **kwargs)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df2, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: check_dtype

# Workflow
columns = ['col1', 'col2']
df1 = DataFrame(columns=columns)
df2 = DataFrame(columns=columns)
kwargs = {'check_dtype': check_dtype}
df1['col1'] = df1['col1'].astype('int64')
if check_dtype:
    msg = 'Attributes of DataFrame\\..* are different'
    with pytest.raises(AssertionError, match=msg):
        tm.assert_frame_equal(df1, df2, **kwargs)
else:
    tm.assert_frame_equal(df1, df2, **kwargs)
```

## Next Steps


---

*Source: test_assert_frame_equal.py:95 | Complexity: Advanced | Last updated: 2026-06-02*