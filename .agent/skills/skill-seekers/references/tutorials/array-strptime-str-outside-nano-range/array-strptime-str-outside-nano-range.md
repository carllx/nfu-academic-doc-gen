# How To: Array Strptime Str Outside Nano Range

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array strptime str outside nano range

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.strptime`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign vals = np.array(...)

```python
vals = np.array(['2401-09-15'], dtype=object)
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array(['2401-09-15'], dtype='M8[s]')
```

### Step 3: Assign fmt = 'ISO8601'

```python
fmt = 'ISO8601'
```

### Step 4: Assign unknown = array_strptime(...)

```python
res, _ = array_strptime(vals, fmt=fmt, creso=creso_infer)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 6: Assign vals2 = np.array(...)

```python
vals2 = np.array(['Sep 15, 2401'], dtype=object)
```

### Step 7: Assign expected2 = np.array(...)

```python
expected2 = np.array(['2401-09-15'], dtype='M8[s]')
```

### Step 8: Assign fmt2 = '%b %d, %Y'

```python
fmt2 = '%b %d, %Y'
```

### Step 9: Assign unknown = array_strptime(...)

```python
res2, _ = array_strptime(vals2, fmt=fmt2, creso=creso_infer)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res2, expected2)
```


## Complete Example

```python
# Workflow
vals = np.array(['2401-09-15'], dtype=object)
expected = np.array(['2401-09-15'], dtype='M8[s]')
fmt = 'ISO8601'
res, _ = array_strptime(vals, fmt=fmt, creso=creso_infer)
tm.assert_numpy_array_equal(res, expected)
vals2 = np.array(['Sep 15, 2401'], dtype=object)
expected2 = np.array(['2401-09-15'], dtype='M8[s]')
fmt2 = '%b %d, %Y'
res2, _ = array_strptime(vals2, fmt=fmt2, creso=creso_infer)
tm.assert_numpy_array_equal(res2, expected2)
```

## Next Steps


---

*Source: test_strptime.py:98 | Complexity: Advanced | Last updated: 2026-06-02*