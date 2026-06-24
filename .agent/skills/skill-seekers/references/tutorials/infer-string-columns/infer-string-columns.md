# How To: Infer String Columns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer string columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

### Step 2: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 3: Assign df = DataFrame.set_index(...)

```python
df = DataFrame(1, columns=list('ABCD'), index=list(range(10))).set_index(['A', 'B'])
```

### Step 4: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 5: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format='table')
```

### Step 6: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'df')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
pytest.importorskip('pyarrow')
path = tmp_path / setup_path
with pd.option_context('future.infer_string', True):
    df = DataFrame(1, columns=list('ABCD'), index=list(range(10))).set_index(['A', 'B'])
    expected = df.copy()
    df.to_hdf(path, key='df', format='table')
    result = read_hdf(path, 'df')
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_round_trip.py:575 | Complexity: Intermediate | Last updated: 2026-06-02*