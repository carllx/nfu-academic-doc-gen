# How To: Round Daily

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round daily

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('20130101 09:10:11', periods=5)
```

### Step 2: Assign result = dti.round(...)

```python
result = dti.round('D')
```

### Step 3: Assign expected = date_range(...)

```python
expected = date_range('20130101', periods=5)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign dti = dti.tz_localize.tz_convert(...)

```python
dti = dti.tz_localize('UTC').tz_convert('US/Eastern')
```

### Step 6: Assign result = dti.round(...)

```python
result = dti.round('D')
```

### Step 7: Assign expected = date_range.tz_localize(...)

```python
expected = date_range('20130101', periods=5).tz_localize('US/Eastern')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign result = dti.round(...)

```python
result = dti.round('s')
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, dti)
```


## Complete Example

```python
# Workflow
dti = date_range('20130101 09:10:11', periods=5)
result = dti.round('D')
expected = date_range('20130101', periods=5)
tm.assert_index_equal(result, expected)
dti = dti.tz_localize('UTC').tz_convert('US/Eastern')
result = dti.round('D')
expected = date_range('20130101', periods=5).tz_localize('US/Eastern')
tm.assert_index_equal(result, expected)
result = dti.round('s')
tm.assert_index_equal(result, dti)
```

## Next Steps


---

*Source: test_round.py:15 | Complexity: Advanced | Last updated: 2026-06-02*