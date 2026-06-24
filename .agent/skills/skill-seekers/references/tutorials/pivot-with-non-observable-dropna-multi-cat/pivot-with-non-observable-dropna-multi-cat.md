# How To: Pivot With Non Observable Dropna Multi Cat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot with non observable dropna multi cat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape`
- `pandas.core.reshape.pivot`

**Setup Required:**
```python
# Fixtures: dropna
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': Categorical(['left', 'low', 'high', 'low', 'high'], categories=['low', 'high', 'left'], ordered=True), 'B': range(5)})
```

### Step 2: Assign msg = 'The default value of observed=False is deprecated'

```python
msg = 'The default value of observed=False is deprecated'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'B': [2.0, 3.0, 0.0]}, index=Index(Categorical.from_codes([0, 1, 2], categories=['low', 'high', 'left'], ordered=True), name='A'))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.pivot_table(...)

```python
result = df.pivot_table(index='A', values='B', dropna=dropna)
```

### Step 6: Assign unknown = unknown.astype(...)

```python
expected['B'] = expected['B'].astype(float)
```


## Complete Example

```python
# Setup
# Fixtures: dropna

# Workflow
df = DataFrame({'A': Categorical(['left', 'low', 'high', 'low', 'high'], categories=['low', 'high', 'left'], ordered=True), 'B': range(5)})
msg = 'The default value of observed=False is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.pivot_table(index='A', values='B', dropna=dropna)
expected = DataFrame({'B': [2.0, 3.0, 0.0]}, index=Index(Categorical.from_codes([0, 1, 2], categories=['low', 'high', 'left'], ordered=True), name='A'))
if not dropna:
    expected['B'] = expected['B'].astype(float)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pivot.py:281 | Complexity: Intermediate | Last updated: 2026-06-02*