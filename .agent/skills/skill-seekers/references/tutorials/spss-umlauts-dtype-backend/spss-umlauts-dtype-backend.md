# How To: Spss Umlauts Dtype Backend

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test spss umlauts dtype backend

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pathlib`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: datapath, dtype_backend
```

## Step-by-Step Guide

### Step 1: Assign fname = datapath(...)

```python
fname = datapath('io', 'data', 'spss', 'umlauts.sav')
```

### Step 2: Assign df = pd.read_spss(...)

```python
df = pd.read_spss(fname, convert_categoricals=False, dtype_backend=dtype_backend)
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'var1': [1.0, 2.0, 1.0, 3.0]}, dtype='Int64')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 5: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({col: ArrowExtensionArray(pa.array(expected[col], from_pandas=True)) for col in expected.columns})
```


## Complete Example

```python
# Setup
# Fixtures: datapath, dtype_backend

# Workflow
fname = datapath('io', 'data', 'spss', 'umlauts.sav')
df = pd.read_spss(fname, convert_categoricals=False, dtype_backend=dtype_backend)
expected = pd.DataFrame({'var1': [1.0, 2.0, 1.0, 3.0]}, dtype='Int64')
if dtype_backend == 'pyarrow':
    pa = pytest.importorskip('pyarrow')
    from pandas.arrays import ArrowExtensionArray
    expected = pd.DataFrame({col: ArrowExtensionArray(pa.array(expected[col], from_pandas=True)) for col in expected.columns})
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_spss.py:95 | Complexity: Intermediate | Last updated: 2026-06-02*