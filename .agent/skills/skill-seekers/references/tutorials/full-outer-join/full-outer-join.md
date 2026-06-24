# How To: Full Outer Join

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test full outer join

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df, df2
```

## Step-by-Step Guide

### Step 1: Assign joined_key2 = merge(...)

```python
joined_key2 = merge(df, df2, on='key2', how='outer')
```

### Step 2: Call _check_join()

```python
_check_join(df, df2, joined_key2, ['key2'], how='outer')
```

### Step 3: Assign joined_both = merge(...)

```python
joined_both = merge(df, df2, how='outer')
```

### Step 4: Call _check_join()

```python
_check_join(df, df2, joined_both, ['key1', 'key2'], how='outer')
```


## Complete Example

```python
# Setup
# Fixtures: df, df2

# Workflow
joined_key2 = merge(df, df2, on='key2', how='outer')
_check_join(df, df2, joined_key2, ['key2'], how='outer')
joined_both = merge(df, df2, how='outer')
_check_join(df, df2, joined_both, ['key1', 'key2'], how='outer')
```

## Next Steps


---

*Source: test_join.py:95 | Complexity: Intermediate | Last updated: 2026-06-02*