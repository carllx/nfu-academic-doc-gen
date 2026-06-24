# How To: Sas Archive

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sas archive

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign fname_uncompressed = datapath(...)

```python
fname_uncompressed = datapath('io', 'sas', 'data', 'airline.sas7bdat')
```

### Step 2: Assign df_uncompressed = read_sas(...)

```python
df_uncompressed = read_sas(fname_uncompressed)
```

### Step 3: Assign fname_compressed = datapath(...)

```python
fname_compressed = datapath('io', 'sas', 'data', 'airline.sas7bdat.gz')
```

### Step 4: Assign df_compressed = read_sas(...)

```python
df_compressed = read_sas(fname_compressed, format='sas7bdat')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_uncompressed, df_compressed)
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
fname_uncompressed = datapath('io', 'sas', 'data', 'airline.sas7bdat')
df_uncompressed = read_sas(fname_uncompressed)
fname_compressed = datapath('io', 'sas', 'data', 'airline.sas7bdat.gz')
df_compressed = read_sas(fname_compressed, format='sas7bdat')
tm.assert_frame_equal(df_uncompressed, df_compressed)
```

## Next Steps


---

*Source: test_sas.py:29 | Complexity: Intermediate | Last updated: 2026-06-02*