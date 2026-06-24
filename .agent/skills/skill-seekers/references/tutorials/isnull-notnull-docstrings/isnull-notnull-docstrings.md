# How To: Isnull Notnull Docstrings

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isnull notnull docstrings

## Prerequisites

**Required Modules:**
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign doc = value

```python
doc = pd.DataFrame.notnull.__doc__
```

**Verification:**
```python
assert doc.startswith('\nDataFrame.notnull is an alias for DataFrame.notna.\n')
```

### Step 2: Assign doc = value

```python
doc = pd.DataFrame.isnull.__doc__
```

**Verification:**
```python
assert doc.startswith('\nDataFrame.isnull is an alias for DataFrame.isna.\n')
```

### Step 3: Assign doc = value

```python
doc = Series.notnull.__doc__
```

**Verification:**
```python
assert doc.startswith('\nSeries.notnull is an alias for Series.notna.\n')
```

### Step 4: Assign doc = value

```python
doc = Series.isnull.__doc__
```

**Verification:**
```python
assert doc.startswith('\nSeries.isnull is an alias for Series.isna.\n')
```


## Complete Example

```python
# Workflow
doc = pd.DataFrame.notnull.__doc__
assert doc.startswith('\nDataFrame.notnull is an alias for DataFrame.notna.\n')
doc = pd.DataFrame.isnull.__doc__
assert doc.startswith('\nDataFrame.isnull is an alias for DataFrame.isna.\n')
doc = Series.notnull.__doc__
assert doc.startswith('\nSeries.notnull is an alias for Series.notna.\n')
doc = Series.isnull.__doc__
assert doc.startswith('\nSeries.isnull is an alias for Series.isna.\n')
```

## Next Steps


---

*Source: test_misc.py:23 | Complexity: Intermediate | Last updated: 2026-06-02*