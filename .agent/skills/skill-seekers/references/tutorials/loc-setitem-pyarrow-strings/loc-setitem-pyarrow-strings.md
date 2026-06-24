# How To: Loc Setitem Pyarrow Strings

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc setitem pyarrow strings

## Prerequisites

**Required Modules:**
- `collections`
- `contextlib`
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.indexing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'strings': Series(['A', 'B', 'C'], dtype='string[pyarrow]'), 'ids': Series([True, True, False])})
```

### Step 3: Assign new_value = Series(...)

```python
new_value = Series(['X', 'Y'])
```

### Step 4: Assign unknown = new_value

```python
df.loc[df.ids, 'strings'] = new_value
```

### Step 5: Assign expected_df = DataFrame(...)

```python
expected_df = DataFrame({'strings': Series(['X', 'Y', 'C'], dtype='string[pyarrow]'), 'ids': Series([True, True, False])})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected_df)
```


## Complete Example

```python
# Workflow
pytest.importorskip('pyarrow')
df = DataFrame({'strings': Series(['A', 'B', 'C'], dtype='string[pyarrow]'), 'ids': Series([True, True, False])})
new_value = Series(['X', 'Y'])
df.loc[df.ids, 'strings'] = new_value
expected_df = DataFrame({'strings': Series(['X', 'Y', 'C'], dtype='string[pyarrow]'), 'ids': Series([True, True, False])})
tm.assert_frame_equal(df, expected_df)
```

## Next Steps


---

*Source: test_loc.py:3124 | Complexity: Intermediate | Last updated: 2026-06-02*