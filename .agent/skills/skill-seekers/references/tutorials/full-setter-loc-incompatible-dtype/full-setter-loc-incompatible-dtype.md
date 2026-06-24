# How To: Full Setter Loc Incompatible Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test full setter loc incompatible dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2]})
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [True, True]})
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2]})
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [3.5, 4.5]})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2]})
```

### Step 8: Assign unknown = value

```python
df.loc[:, 'a'] = {0: 3, 1: 4}
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [3, 4]})
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 11: Assign unknown = True

```python
df.loc[:, 'a'] = True
```

### Step 12: Assign unknown = value

```python
df.loc[:, 'a'] = {0: 3.5, 1: 4.5}
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2]})
with tm.assert_produces_warning(FutureWarning, match='incompatible dtype'):
    df.loc[:, 'a'] = True
expected = DataFrame({'a': [True, True]})
tm.assert_frame_equal(df, expected)
df = DataFrame({'a': [1, 2]})
with tm.assert_produces_warning(FutureWarning, match='incompatible dtype'):
    df.loc[:, 'a'] = {0: 3.5, 1: 4.5}
expected = DataFrame({'a': [3.5, 4.5]})
tm.assert_frame_equal(df, expected)
df = DataFrame({'a': [1, 2]})
df.loc[:, 'a'] = {0: 3, 1: 4}
expected = DataFrame({'a': [3, 4]})
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_setitem.py:1493 | Complexity: Advanced | Last updated: 2026-06-02*