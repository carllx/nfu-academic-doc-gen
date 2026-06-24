# How To: Set Value By Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set value by index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign warn = None

```python
warn = None
```

### Step 2: Assign msg = 'will attempt to set the values inplace'

```python
msg = 'will attempt to set the values inplace'
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(9).reshape(3, 3).T)
```

### Step 4: Assign df.columns = list(...)

```python
df.columns = list('AAA')
```

### Step 5: Assign expected = unknown.copy(...)

```python
expected = df.iloc[:, 2].copy()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df.iloc[:, 2], expected)
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(9).reshape(3, 3).T)
```

### Step 8: Assign df.columns = value

```python
df.columns = [2, float(2), str(2)]
```

### Step 9: Assign expected = unknown.copy(...)

```python
expected = df.iloc[:, 1].copy()
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df.iloc[:, 1], expected)
```

### Step 11: Assign unknown = 3

```python
df.iloc[:, 0] = 3
```

### Step 12: Assign unknown = 3

```python
df.iloc[:, 0] = 3
```


## Complete Example

```python
# Workflow
warn = None
msg = 'will attempt to set the values inplace'
df = DataFrame(np.arange(9).reshape(3, 3).T)
df.columns = list('AAA')
expected = df.iloc[:, 2].copy()
with tm.assert_produces_warning(warn, match=msg):
    df.iloc[:, 0] = 3
tm.assert_series_equal(df.iloc[:, 2], expected)
df = DataFrame(np.arange(9).reshape(3, 3).T)
df.columns = [2, float(2), str(2)]
expected = df.iloc[:, 1].copy()
with tm.assert_produces_warning(warn, match=msg):
    df.iloc[:, 0] = 3
tm.assert_series_equal(df.iloc[:, 1], expected)
```

## Next Steps


---

*Source: test_nonunique_indexes.py:318 | Complexity: Advanced | Last updated: 2026-06-02*