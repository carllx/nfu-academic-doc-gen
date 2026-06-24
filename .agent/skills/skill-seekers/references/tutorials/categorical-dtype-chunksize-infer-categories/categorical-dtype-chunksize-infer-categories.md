# How To: Categorical Dtype Chunksize Infer Categories

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical dtype chunksize infer categories

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

### Step 3: Assign expecteds = value

```python
expecteds = [DataFrame({'a': [1, 1], 'b': Categorical(['a', 'b'])}), DataFrame({'a': [1, 2], 'b': Categorical(['b', 'c'])}, index=[2, 3])]
```

### Step 4: Assign msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
```

### Step 5: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), dtype={'b': 'category'}, chunksize=2)
```

### Step 6: Call tm.assert_frame_equal()

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
expecteds = [DataFrame({'a': [1, 1], 'b': Categorical(['a', 'b'])}), DataFrame({'a': [1, 2], 'b': Categorical(['b', 'c'])}, index=[2, 3])]
if parser.engine == 'pyarrow':
    msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), dtype={'b': 'category'}, chunksize=2)
    return
with parser.read_csv(StringIO(data), dtype={'b': 'category'}, chunksize=2) as actuals:
    for actual, expected in zip(actuals, expecteds):
        tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_categorical.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*