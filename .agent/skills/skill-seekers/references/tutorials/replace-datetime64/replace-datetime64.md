# How To: Replace Datetime64

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace datetime64

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series(pd.date_range('20130101', periods=5))
```

### Step 2: Assign expected = ser.copy(...)

```python
expected = ser.copy()
```

### Step 3: Assign unknown = pd.Timestamp(...)

```python
expected.loc[2] = pd.Timestamp('20120101')
```

### Step 4: Assign result = ser.replace(...)

```python
result = ser.replace({pd.Timestamp('20130103'): pd.Timestamp('20120101')})
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = ser.replace(...)

```python
result = ser.replace(pd.Timestamp('20130103'), pd.Timestamp('20120101'))
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = pd.Series(pd.date_range('20130101', periods=5))
expected = ser.copy()
expected.loc[2] = pd.Timestamp('20120101')
result = ser.replace({pd.Timestamp('20130103'): pd.Timestamp('20120101')})
tm.assert_series_equal(result, expected)
result = ser.replace(pd.Timestamp('20130103'), pd.Timestamp('20120101'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_replace.py:157 | Complexity: Intermediate | Last updated: 2026-06-02*