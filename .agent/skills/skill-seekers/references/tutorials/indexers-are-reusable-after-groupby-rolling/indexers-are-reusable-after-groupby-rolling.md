# How To: Indexers Are Reusable After Groupby Rolling

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test indexers are reusable after groupby rolling

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: indexer_class, window_size, df_data
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(df_data)
```

**Verification:**
```python
assert indexer.window_size == original_window_size
```

### Step 2: Assign num_trials = 3

```python
num_trials = 3
```

### Step 3: Assign indexer = indexer_class(...)

```python
indexer = indexer_class(window_size=window_size)
```

### Step 4: Assign original_window_size = value

```python
original_window_size = indexer.window_size
```

### Step 5: Call unknown.rolling.mean()

```python
df.groupby('a')['b'].rolling(window=indexer, min_periods=1).mean()
```

**Verification:**
```python
assert indexer.window_size == original_window_size
```


## Complete Example

```python
# Setup
# Fixtures: indexer_class, window_size, df_data

# Workflow
df = DataFrame(df_data)
num_trials = 3
indexer = indexer_class(window_size=window_size)
original_window_size = indexer.window_size
for i in range(num_trials):
    df.groupby('a')['b'].rolling(window=indexer, min_periods=1).mean()
    assert indexer.window_size == original_window_size
```

## Next Steps


---

*Source: test_base_indexer.py:333 | Complexity: Intermediate | Last updated: 2026-06-02*