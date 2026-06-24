# How To: Align Fill Method

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test align fill method

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
# Fixtures: datetime_series, first_slice, second_slice, join_type, method, limit
```

## Step-by-Step Guide

### Step 1: Assign a = value

```python
a = datetime_series[slice(*first_slice)]
```

### Step 2: Assign b = value

```python
b = datetime_series[slice(*second_slice)]
```

### Step 3: Assign msg = "The 'method', 'limit', and 'fill_axis' keywords in Series.align are deprecated"

```python
msg = "The 'method', 'limit', and 'fill_axis' keywords in Series.align are deprecated"
```

### Step 4: Assign join_index = a.index.join(...)

```python
join_index = a.index.join(b.index, how=join_type)
```

### Step 5: Assign ea = a.reindex(...)

```python
ea = a.reindex(join_index)
```

### Step 6: Assign eb = b.reindex(...)

```python
eb = b.reindex(join_index)
```

### Step 7: Assign msg2 = "Series.fillna with 'method' is deprecated"

```python
msg2 = "Series.fillna with 'method' is deprecated"
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(aa, ea)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ab, eb)
```

### Step 10: Assign unknown = a.align(...)

```python
aa, ab = a.align(b, join=join_type, method=method, limit=limit)
```

### Step 11: Assign ea = ea.fillna(...)

```python
ea = ea.fillna(method=method, limit=limit)
```

### Step 12: Assign eb = eb.fillna(...)

```python
eb = eb.fillna(method=method, limit=limit)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series, first_slice, second_slice, join_type, method, limit

# Workflow
a = datetime_series[slice(*first_slice)]
b = datetime_series[slice(*second_slice)]
msg = "The 'method', 'limit', and 'fill_axis' keywords in Series.align are deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    aa, ab = a.align(b, join=join_type, method=method, limit=limit)
join_index = a.index.join(b.index, how=join_type)
ea = a.reindex(join_index)
eb = b.reindex(join_index)
msg2 = "Series.fillna with 'method' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg2):
    ea = ea.fillna(method=method, limit=limit)
    eb = eb.fillna(method=method, limit=limit)
tm.assert_series_equal(aa, ea)
tm.assert_series_equal(ab, eb)
```

## Next Steps


---

*Source: test_align.py:66 | Complexity: Advanced | Last updated: 2026-06-02*