# How To: Nth Bdays

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nth bdays

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
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign business_dates = pd.date_range(...)

```python
business_dates = pd.date_range(start='4/1/2014', end='6/30/2014', freq='B', unit=unit)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(1, index=business_dates, columns=['a', 'b'])
```

### Step 3: Assign key = value

```python
key = [df.index.year, df.index.month]
```

### Step 4: Assign result = df.groupby.nth(...)

```python
result = df.groupby(key, as_index=False).nth([0, 3, -2, -1])
```

### Step 5: Assign expected_dates = pd.to_datetime.as_unit(...)

```python
expected_dates = pd.to_datetime(['2014/4/1', '2014/4/4', '2014/4/29', '2014/4/30', '2014/5/1', '2014/5/6', '2014/5/29', '2014/5/30', '2014/6/2', '2014/6/5', '2014/6/27', '2014/6/30']).as_unit(unit)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(1, columns=['a', 'b'], index=expected_dates)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
business_dates = pd.date_range(start='4/1/2014', end='6/30/2014', freq='B', unit=unit)
df = DataFrame(1, index=business_dates, columns=['a', 'b'])
key = [df.index.year, df.index.month]
result = df.groupby(key, as_index=False).nth([0, 3, -2, -1])
expected_dates = pd.to_datetime(['2014/4/1', '2014/4/4', '2014/4/29', '2014/4/30', '2014/5/1', '2014/5/6', '2014/5/29', '2014/5/30', '2014/6/2', '2014/6/5', '2014/6/27', '2014/6/30']).as_unit(unit)
expected = DataFrame(1, columns=['a', 'b'], index=expected_dates)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nth.py:298 | Complexity: Intermediate | Last updated: 2026-06-02*