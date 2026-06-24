# How To: Range Slice Outofbounds

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test range slice outofbounds

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: make_range
```

## Step-by-Step Guide

### Step 1: Assign idx = make_range(...)

```python
idx = make_range(start='2013/10/01', freq='D', periods=10)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'units': [100 + i for i in range(10)]}, index=idx)
```

### Step 3: Assign empty = DataFrame(...)

```python
empty = DataFrame(index=idx[:0], columns=['units'])
```

### Step 4: Assign unknown = unknown.astype(...)

```python
empty['units'] = empty['units'].astype('int64')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df['2013/09/01':'2013/09/30'], empty)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df['2013/09/30':'2013/10/02'], df.iloc[:2])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df['2013/10/01':'2013/10/02'], df.iloc[:2])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df['2013/10/02':'2013/09/30'], empty)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df['2013/10/15':'2013/10/17'], empty)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df['2013-06':'2013-09'], empty)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df['2013-11':'2013-12'], empty)
```


## Complete Example

```python
# Setup
# Fixtures: make_range

# Workflow
idx = make_range(start='2013/10/01', freq='D', periods=10)
df = DataFrame({'units': [100 + i for i in range(10)]}, index=idx)
empty = DataFrame(index=idx[:0], columns=['units'])
empty['units'] = empty['units'].astype('int64')
tm.assert_frame_equal(df['2013/09/01':'2013/09/30'], empty)
tm.assert_frame_equal(df['2013/09/30':'2013/10/02'], df.iloc[:2])
tm.assert_frame_equal(df['2013/10/01':'2013/10/02'], df.iloc[:2])
tm.assert_frame_equal(df['2013/10/02':'2013/09/30'], empty)
tm.assert_frame_equal(df['2013/10/15':'2013/10/17'], empty)
tm.assert_frame_equal(df['2013-06':'2013-09'], empty)
tm.assert_frame_equal(df['2013-11':'2013-12'], empty)
```

## Next Steps


---

*Source: test_partial_slicing.py:115 | Complexity: Advanced | Last updated: 2026-06-02*