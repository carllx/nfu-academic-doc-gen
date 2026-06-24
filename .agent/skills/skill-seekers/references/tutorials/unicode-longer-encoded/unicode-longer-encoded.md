# How To: Unicode Longer Encoded

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unicode longer encoded

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
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign char = 'Δ'

```python
char = 'Δ'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [char]})
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['a', char], 'B': ['b', 'b']})
```

### Step 4: Call store.put()

```python
store.put('df', df, format='table', encoding='utf-8')
```

### Step 5: Assign result = store.get(...)

```python
result = store.get('df')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 7: Call store.put()

```python
store.put('df', df, format='table', encoding='utf-8')
```

### Step 8: Assign result = store.get(...)

```python
result = store.get('df')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
char = 'Δ'
df = DataFrame({'A': [char]})
with ensure_clean_store(setup_path) as store:
    store.put('df', df, format='table', encoding='utf-8')
    result = store.get('df')
    tm.assert_frame_equal(result, df)
df = DataFrame({'A': ['a', char], 'B': ['b', 'b']})
with ensure_clean_store(setup_path) as store:
    store.put('df', df, format='table', encoding='utf-8')
    result = store.get('df')
    tm.assert_frame_equal(result, df)
```

## Next Steps


---

*Source: test_round_trip.py:538 | Complexity: Advanced | Last updated: 2026-06-02*