# How To: Align

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test align

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series, first_slice, second_slice, join_type, fill
```

## Step-by-Step Guide

### Step 1: Assign a = value

```python
a = datetime_series[slice(*first_slice)]
```

**Verification:**
```python
assert (aa.reindex(diff_a) == fill).all()
```

### Step 2: Assign b = value

```python
b = datetime_series[slice(*second_slice)]
```

**Verification:**
```python
assert (ab.reindex(diff_b) == fill).all()
```

### Step 3: Assign unknown = a.align(...)

```python
aa, ab = a.align(b, join=join_type, fill_value=fill)
```

**Verification:**
```python
assert aa.name == 'ts'
```

### Step 4: Assign join_index = a.index.join(...)

```python
join_index = a.index.join(b.index, how=join_type)
```

**Verification:**
```python
assert ea.name == 'ts'
```

### Step 5: Assign ea = a.reindex(...)

```python
ea = a.reindex(join_index)
```

**Verification:**
```python
assert ab.name == 'ts'
```

### Step 6: Assign eb = b.reindex(...)

```python
eb = b.reindex(join_index)
```

**Verification:**
```python
assert eb.name == 'ts'
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(aa, ea)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ab, eb)
```

**Verification:**
```python
assert aa.name == 'ts'
```

### Step 9: Assign diff_a = aa.index.difference(...)

```python
diff_a = aa.index.difference(join_index)
```

### Step 10: Assign diff_b = ab.index.difference(...)

```python
diff_b = ab.index.difference(join_index)
```

### Step 11: Assign ea = ea.fillna(...)

```python
ea = ea.fillna(fill)
```

### Step 12: Assign eb = eb.fillna(...)

```python
eb = eb.fillna(fill)
```

**Verification:**
```python
assert (aa.reindex(diff_a) == fill).all()
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series, first_slice, second_slice, join_type, fill

# Workflow
a = datetime_series[slice(*first_slice)]
b = datetime_series[slice(*second_slice)]
aa, ab = a.align(b, join=join_type, fill_value=fill)
join_index = a.index.join(b.index, how=join_type)
if fill is not None:
    diff_a = aa.index.difference(join_index)
    diff_b = ab.index.difference(join_index)
    if len(diff_a) > 0:
        assert (aa.reindex(diff_a) == fill).all()
    if len(diff_b) > 0:
        assert (ab.reindex(diff_b) == fill).all()
ea = a.reindex(join_index)
eb = b.reindex(join_index)
if fill is not None:
    ea = ea.fillna(fill)
    eb = eb.fillna(fill)
tm.assert_series_equal(aa, ea)
tm.assert_series_equal(ab, eb)
assert aa.name == 'ts'
assert ea.name == 'ts'
assert ab.name == 'ts'
assert eb.name == 'ts'
```

## Next Steps


---

*Source: test_align.py:25 | Complexity: Advanced | Last updated: 2026-06-02*