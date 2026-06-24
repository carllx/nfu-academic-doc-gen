# How To: Sort Values Without Freq Periodindex Nat

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values without freq periodindex nat

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011', '2013', 'NaT', '2011'], name='pidx', freq='D')
```

### Step 2: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex(['NaT', '2011', '2011', '2013'], name='pidx', freq='D')
```

### Step 3: Assign ordered = idx.sort_values(...)

```python
ordered = idx.sort_values(na_position='first')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ordered, expected)
```

### Step 5: Call check_freq_nonmonotonic()

```python
check_freq_nonmonotonic(ordered, idx)
```

### Step 6: Assign ordered = idx.sort_values(...)

```python
ordered = idx.sort_values(ascending=False)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ordered, expected[::-1])
```

### Step 8: Call check_freq_nonmonotonic()

```python
check_freq_nonmonotonic(ordered, idx)
```


## Complete Example

```python
# Workflow
idx = PeriodIndex(['2011', '2013', 'NaT', '2011'], name='pidx', freq='D')
expected = PeriodIndex(['NaT', '2011', '2011', '2013'], name='pidx', freq='D')
ordered = idx.sort_values(na_position='first')
tm.assert_index_equal(ordered, expected)
check_freq_nonmonotonic(ordered, idx)
ordered = idx.sort_values(ascending=False)
tm.assert_index_equal(ordered, expected[::-1])
check_freq_nonmonotonic(ordered, idx)
```

## Next Steps


---

*Source: test_sort_values.py:295 | Complexity: Advanced | Last updated: 2026-06-02*