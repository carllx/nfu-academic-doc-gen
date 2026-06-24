# How To: Setitem List

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem list

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign unknown = 'foo'

```python
float_frame['E'] = 'foo'
```

### Step 2: Assign data = value

```python
data = float_frame[['A', 'B']]
```

### Step 3: Assign unknown = data

```python
float_frame[['B', 'A']] = data
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(float_frame['B'], data['A'], check_names=False)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(float_frame['A'], data['B'], check_names=False)
```

### Step 6: Assign msg = 'Columns must be same length as key'

```python
msg = 'Columns must be same length as key'
```

### Step 7: Assign newcolumndata = range(...)

```python
newcolumndata = range(len(data.index) - 1)
```

### Step 8: Assign msg = value

```python
msg = f'Length of values \\({len(newcolumndata)}\\) does not match length of index \\({len(data)}\\)'
```

### Step 9: Assign unknown = value

```python
data[['A']] = float_frame[['A', 'B']]
```

### Step 10: Assign unknown = newcolumndata

```python
data['A'] = newcolumndata
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
float_frame['E'] = 'foo'
data = float_frame[['A', 'B']]
float_frame[['B', 'A']] = data
tm.assert_series_equal(float_frame['B'], data['A'], check_names=False)
tm.assert_series_equal(float_frame['A'], data['B'], check_names=False)
msg = 'Columns must be same length as key'
with pytest.raises(ValueError, match=msg):
    data[['A']] = float_frame[['A', 'B']]
newcolumndata = range(len(data.index) - 1)
msg = f'Length of values \\({len(newcolumndata)}\\) does not match length of index \\({len(data)}\\)'
with pytest.raises(ValueError, match=msg):
    data['A'] = newcolumndata
```

## Next Steps


---

*Source: test_indexing.py:93 | Complexity: Advanced | Last updated: 2026-06-02*