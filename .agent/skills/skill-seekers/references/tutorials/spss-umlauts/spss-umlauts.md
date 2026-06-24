# How To: Spss Umlauts

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test spss umlauts

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
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign fname = datapath(...)

```python
fname = datapath('io', 'data', 'spss', 'umlauts.sav')
```

### Step 2: Assign df = pd.read_spss(...)

```python
df = pd.read_spss(fname, convert_categoricals=True)
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'var1': ['the ä umlaut', 'the ü umlaut', 'the ä umlaut', 'the ö umlaut']})
```

### Step 4: Assign unknown = pd.Categorical(...)

```python
expected['var1'] = pd.Categorical(expected['var1'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 6: Assign df = pd.read_spss(...)

```python
df = pd.read_spss(fname, convert_categoricals=False)
```

### Step 7: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'var1': [1.0, 2.0, 1.0, 3.0]})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
fname = datapath('io', 'data', 'spss', 'umlauts.sav')
df = pd.read_spss(fname, convert_categoricals=True)
expected = pd.DataFrame({'var1': ['the ä umlaut', 'the ü umlaut', 'the ä umlaut', 'the ö umlaut']})
expected['var1'] = pd.Categorical(expected['var1'])
tm.assert_frame_equal(df, expected)
df = pd.read_spss(fname, convert_categoricals=False)
expected = pd.DataFrame({'var1': [1.0, 2.0, 1.0, 3.0]})
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_spss.py:70 | Complexity: Advanced | Last updated: 2026-06-02*