# How To: Datetime

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime

## Prerequisites

**Required Modules:**
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `decimal`


## Step-by-Step Guide

### Step 1: Assign begin = np.datetime64(...)

```python
begin = np.datetime64('2000-01-01', 'D')
```

**Verification:**
```python
assert_equal(d_count, i_count)
```

### Step 2: Assign offsets = np.array(...)

```python
offsets = np.array([0, 0, 1, 1, 2, 3, 5, 10, 20])
```

**Verification:**
```python
assert_equal(t_count, i_count)
```

### Step 3: Assign bins = np.array(...)

```python
bins = np.array([0, 2, 7, 20])
```

**Verification:**
```python
assert_equal((d_edge - begin).astype(int), i_edge)
```

### Step 4: Assign dates = value

```python
dates = begin + offsets
```

**Verification:**
```python
assert_equal(t_edge.astype(int), i_edge)
```

### Step 5: Assign date_bins = value

```python
date_bins = begin + bins
```

**Verification:**
```python
assert_equal(d_edge.dtype, dates.dtype)
```

### Step 6: Assign td = np.dtype(...)

```python
td = np.dtype('timedelta64[D]')
```

**Verification:**
```python
assert_equal(t_edge.dtype, td)
```

### Step 7: Assign unknown = histogram(...)

```python
d_count, d_edge = histogram(dates, bins=date_bins)
```

### Step 8: Assign unknown = histogram(...)

```python
t_count, t_edge = histogram(offsets.astype(td), bins=bins.astype(td))
```

### Step 9: Assign unknown = histogram(...)

```python
i_count, i_edge = histogram(offsets, bins=bins)
```

### Step 10: Call assert_equal()

```python
assert_equal(d_count, i_count)
```

### Step 11: Call assert_equal()

```python
assert_equal(t_count, i_count)
```

### Step 12: Call assert_equal()

```python
assert_equal((d_edge - begin).astype(int), i_edge)
```

### Step 13: Call assert_equal()

```python
assert_equal(t_edge.astype(int), i_edge)
```

### Step 14: Call assert_equal()

```python
assert_equal(d_edge.dtype, dates.dtype)
```

### Step 15: Call assert_equal()

```python
assert_equal(t_edge.dtype, td)
```


## Complete Example

```python
# Workflow
begin = np.datetime64('2000-01-01', 'D')
offsets = np.array([0, 0, 1, 1, 2, 3, 5, 10, 20])
bins = np.array([0, 2, 7, 20])
dates = begin + offsets
date_bins = begin + bins
td = np.dtype('timedelta64[D]')
d_count, d_edge = histogram(dates, bins=date_bins)
t_count, t_edge = histogram(offsets.astype(td), bins=bins.astype(td))
i_count, i_edge = histogram(offsets, bins=bins)
assert_equal(d_count, i_count)
assert_equal(t_count, i_count)
assert_equal((d_edge - begin).astype(int), i_edge)
assert_equal(t_edge.astype(int), i_edge)
assert_equal(d_edge.dtype, dates.dtype)
assert_equal(t_edge.dtype, td)
```

## Next Steps


---

*Source: test_histograms.py:304 | Complexity: Advanced | Last updated: 2026-06-02*