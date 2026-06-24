# How To: Partial Set Empty Frame2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial set empty frame2

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=Index(['foo']), index=Index([], dtype='object'))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(index=Index([], dtype='object'))
```

### Step 3: Assign unknown = Series(...)

```python
df['foo'] = Series([], dtype='object')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(index=Index([]))
```

### Step 6: Assign unknown = Series(...)

```python
df['foo'] = Series(df.index)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame(index=Index([]))
```

### Step 9: Assign unknown = value

```python
df['foo'] = df.index
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
expected = DataFrame(columns=Index(['foo']), index=Index([], dtype='object'))
df = DataFrame(index=Index([], dtype='object'))
df['foo'] = Series([], dtype='object')
tm.assert_frame_equal(df, expected)
df = DataFrame(index=Index([]))
df['foo'] = Series(df.index)
tm.assert_frame_equal(df, expected)
df = DataFrame(index=Index([]))
df['foo'] = df.index
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_partial.py:95 | Complexity: Advanced | Last updated: 2026-06-02*