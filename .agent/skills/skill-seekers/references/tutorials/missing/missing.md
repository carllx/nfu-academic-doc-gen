# How To: Missing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test missing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: date_range_frame
```

## Step-by-Step Guide

### Step 1: Assign N = 10

```python
N = 10
```

**Verification:**
```python
assert isinstance(result.name, Period)
```

### Step 2: Assign df = unknown.copy.astype(...)

```python
df = date_range_frame.iloc[:N].copy().astype('float64')
```

### Step 3: Assign result = df.asof(...)

```python
result = df.asof('1989-12-31')
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(index=['A', 'B'], name=Timestamp('1989-12-31'), dtype=np.float64)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = df.asof(...)

```python
result = df.asof(to_datetime(['1989-12-31']))
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=to_datetime(['1989-12-31']), columns=['A', 'B'], dtype='float64')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign df = df.to_period(...)

```python
df = df.to_period('D')
```

### Step 10: Assign result = df.asof(...)

```python
result = df.asof('1989-12-31')
```

**Verification:**
```python
assert isinstance(result.name, Period)
```


## Complete Example

```python
# Setup
# Fixtures: date_range_frame

# Workflow
N = 10
df = date_range_frame.iloc[:N].copy().astype('float64')
result = df.asof('1989-12-31')
expected = Series(index=['A', 'B'], name=Timestamp('1989-12-31'), dtype=np.float64)
tm.assert_series_equal(result, expected)
result = df.asof(to_datetime(['1989-12-31']))
expected = DataFrame(index=to_datetime(['1989-12-31']), columns=['A', 'B'], dtype='float64')
tm.assert_frame_equal(result, expected)
df = df.to_period('D')
result = df.asof('1989-12-31')
assert isinstance(result.name, Period)
```

## Next Steps


---

*Source: test_asof.py:78 | Complexity: Advanced | Last updated: 2026-06-02*