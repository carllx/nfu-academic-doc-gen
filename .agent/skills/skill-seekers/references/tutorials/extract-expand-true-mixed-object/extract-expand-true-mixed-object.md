# How To: Extract Expand True Mixed Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extract expand True mixed object

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign er = value

```python
er = [np.nan, np.nan]
```

### Step 2: Assign mixed = Series(...)

```python
mixed = Series(['aBAD_BAD', np.nan, 'BAD_b_BAD', True, datetime.today(), 'foo', None, 1, 2.0])
```

### Step 3: Assign result = mixed.str.extract(...)

```python
result = mixed.str.extract('.*(BAD[_]+).*(BAD)', expand=True)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([['BAD_', 'BAD'], er, ['BAD_', 'BAD'], er, er, er, er, er, er], dtype=object)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
er = [np.nan, np.nan]
mixed = Series(['aBAD_BAD', np.nan, 'BAD_b_BAD', True, datetime.today(), 'foo', None, 1, 2.0])
result = mixed.str.extract('.*(BAD[_]+).*(BAD)', expand=True)
expected = DataFrame([['BAD_', 'BAD'], er, ['BAD_', 'BAD'], er, er, er, er, er, er], dtype=object)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:227 | Complexity: Intermediate | Last updated: 2026-06-02*