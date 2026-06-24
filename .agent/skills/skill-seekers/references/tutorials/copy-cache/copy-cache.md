# How To: Copy Cache

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test copy cache

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1]})
```

**Verification:**
```python
assert df['a'].values[0] == -1
```

### Step 2: Assign unknown = value

```python
df['x'] = [0]
```

### Step 3: df['a']

```python
df['a']
```

### Step 4: Call df.copy()

```python
df.copy()
```

### Step 5: Assign unknown = value

```python
df['a'].values[0] = -1
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, DataFrame({'a': [-1], 'x': [0]}))
```

### Step 7: Assign unknown = value

```python
df['y'] = [0]
```

**Verification:**
```python
assert df['a'].values[0] == -1
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, DataFrame({'a': [-1], 'x': [0], 'y': [0]}))
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1]})
df['x'] = [0]
df['a']
df.copy()
df['a'].values[0] = -1
tm.assert_frame_equal(df, DataFrame({'a': [-1], 'x': [0]}))
df['y'] = [0]
assert df['a'].values[0] == -1
tm.assert_frame_equal(df, DataFrame({'a': [-1], 'x': [0], 'y': [0]}))
```

## Next Steps


---

*Source: test_copy.py:22 | Complexity: Advanced | Last updated: 2026-06-02*