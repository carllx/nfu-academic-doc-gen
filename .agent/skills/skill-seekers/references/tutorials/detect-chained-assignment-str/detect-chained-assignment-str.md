# How To: Detect Chained Assignment Str

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test detect chained assignment str

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = random_text(...)

```python
df = random_text(100000)
```

### Step 2: Assign indexer = df.letters.apply(...)

```python
indexer = df.letters.apply(lambda x: len(x) > 10)
```

### Step 3: Assign unknown = unknown.apply(...)

```python
df.loc[indexer, 'letters'] = df.loc[indexer, 'letters'].apply(str.lower)
```


## Complete Example

```python
# Workflow
df = random_text(100000)
indexer = df.letters.apply(lambda x: len(x) > 10)
df.loc[indexer, 'letters'] = df.loc[indexer, 'letters'].apply(str.lower)
```

## Next Steps


---

*Source: test_chaining_and_caching.py:397 | Complexity: Beginner | Last updated: 2026-06-02*