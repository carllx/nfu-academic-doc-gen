# How To: Fillna Datelike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna datelike

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'Date': [NaT, Timestamp('2014-1-1')], 'Date2': [Timestamp('2013-1-1'), NaT]})
```

### Step 2: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 3: Assign unknown = unknown.fillna(...)

```python
expected['Date'] = expected['Date'].fillna(df.loc[df.index[0], 'Date2'])
```

### Step 4: Assign result = df.fillna(...)

```python
result = df.fillna(value={'Date': df['Date2']})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'Date': [NaT, Timestamp('2014-1-1')], 'Date2': [Timestamp('2013-1-1'), NaT]})
expected = df.copy()
expected['Date'] = expected['Date'].fillna(df.loc[df.index[0], 'Date2'])
result = df.fillna(value={'Date': df['Date2']})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_fillna.py:159 | Complexity: Intermediate | Last updated: 2026-06-02*