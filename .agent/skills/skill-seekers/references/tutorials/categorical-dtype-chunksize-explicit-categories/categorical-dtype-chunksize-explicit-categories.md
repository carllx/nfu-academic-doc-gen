# How To: Categorical Dtype Chunksize Explicit Categories

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical dtype chunksize explicit categories

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b\n1,a\n1,b\n1,b\n2,c'

```python
data = 'a,b\n1,a\n1,b\n1,b\n2,c'
```

### Step 3: Assign cats = value

```python
cats = ['a', 'b', 'c']
```

### Step 4: Assign expecteds = value

```python
expecteds = [DataFrame({'a': [1, 1], 'b': Categorical(['a', 'b'], categories=cats)}), DataFrame({'a': [1, 2], 'b': Categorical(['b', 'c'], categories=cats)}, index=[2, 3])]
```

### Step 5: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(cats)
```

### Step 6: Assign msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), dtype={'b': dtype}, chunksize=2)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'a,b\n1,a\n1,b\n1,b\n2,c'
cats = ['a', 'b', 'c']
expecteds = [DataFrame({'a': [1, 1], 'b': Categorical(['a', 'b'], categories=cats)}), DataFrame({'a': [1, 2], 'b': Categorical(['b', 'c'], categories=cats)}, index=[2, 3])]
dtype = CategoricalDtype(cats)
if parser.engine == 'pyarrow':
    msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), dtype={'b': dtype}, chunksize=2)
    return
with parser.read_csv(StringIO(data), dtype={'b': dtype}, chunksize=2) as actuals:
    for actual, expected in zip(actuals, expecteds):
        tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_categorical.py:175 | Complexity: Advanced | Last updated: 2026-06-02*