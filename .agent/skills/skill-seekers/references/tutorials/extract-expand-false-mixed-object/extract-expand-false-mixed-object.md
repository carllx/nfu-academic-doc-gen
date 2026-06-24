# How To: Extract Expand False Mixed Object

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extract expand False mixed object

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(['aBAD_BAD', np.nan, 'BAD_b_BAD', True, datetime.today(), 'foo', None, 1, 2.0])
```

### Step 2: Assign result = ser.str.extract(...)

```python
result = ser.str.extract('.*(BAD[_]+).*(BAD)', expand=False)
```

### Step 3: Assign er = value

```python
er = [np.nan, np.nan]
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([['BAD_', 'BAD'], er, ['BAD_', 'BAD'], er, er, er, er, er, er], dtype=object)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = ser.str.extract(...)

```python
result = ser.str.extract('.*(BAD[_]+).*BAD', expand=False)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(['BAD_', np.nan, 'BAD_', np.nan, np.nan, np.nan, None, np.nan, np.nan], dtype=object)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(['aBAD_BAD', np.nan, 'BAD_b_BAD', True, datetime.today(), 'foo', None, 1, 2.0])
result = ser.str.extract('.*(BAD[_]+).*(BAD)', expand=False)
er = [np.nan, np.nan]
expected = DataFrame([['BAD_', 'BAD'], er, ['BAD_', 'BAD'], er, er, er, er, er, er], dtype=object)
tm.assert_frame_equal(result, expected)
result = ser.str.extract('.*(BAD[_]+).*BAD', expand=False)
expected = Series(['BAD_', np.nan, 'BAD_', np.nan, np.nan, np.nan, None, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:42 | Complexity: Advanced | Last updated: 2026-06-02*