# How To: Difference Freq

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test difference freq

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign index = period_range(...)

```python
index = period_range('20160920', '20160925', freq='D')
```

### Step 2: Assign other = period_range(...)

```python
other = period_range('20160921', '20160924', freq='D')
```

### Step 3: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex(['20160920', '20160925'], freq='D')
```

### Step 4: Assign idx_diff = index.difference(...)

```python
idx_diff = index.difference(other, sort)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx_diff, expected)
```

### Step 6: Call tm.assert_attr_equal()

```python
tm.assert_attr_equal('freq', idx_diff, expected)
```

### Step 7: Assign other = period_range(...)

```python
other = period_range('20160922', '20160925', freq='D')
```

### Step 8: Assign idx_diff = index.difference(...)

```python
idx_diff = index.difference(other, sort)
```

### Step 9: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex(['20160920', '20160921'], freq='D')
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx_diff, expected)
```

### Step 11: Call tm.assert_attr_equal()

```python
tm.assert_attr_equal('freq', idx_diff, expected)
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
index = period_range('20160920', '20160925', freq='D')
other = period_range('20160921', '20160924', freq='D')
expected = PeriodIndex(['20160920', '20160925'], freq='D')
idx_diff = index.difference(other, sort)
tm.assert_index_equal(idx_diff, expected)
tm.assert_attr_equal('freq', idx_diff, expected)
other = period_range('20160922', '20160925', freq='D')
idx_diff = index.difference(other, sort)
expected = PeriodIndex(['20160920', '20160921'], freq='D')
tm.assert_index_equal(idx_diff, expected)
tm.assert_attr_equal('freq', idx_diff, expected)
```

## Next Steps


---

*Source: test_setops.py:317 | Complexity: Advanced | Last updated: 2026-06-02*