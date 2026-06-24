# How To: Categorical Dtype High Cardinality Numeric

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test categorical dtype high cardinality numeric

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
# Fixtures: all_parsers, monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign heuristic = value

```python
heuristic = 2 ** 5
```

### Step 3: Assign data = np.sort(...)

```python
data = np.sort([str(i) for i in range(heuristic + 1)])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': Categorical(data, ordered=True)})
```

### Step 5: Assign unknown = unknown.cat.reorder_categories(...)

```python
actual['a'] = actual['a'].cat.reorder_categories(np.sort(actual.a.cat.categories), ordered=True)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```

### Step 7: Call m.setattr()

```python
m.setattr(libparsers, 'DEFAULT_BUFFER_HEURISTIC', heuristic)
```

### Step 8: Assign actual = parser.read_csv(...)

```python
actual = parser.read_csv(StringIO('a\n' + '\n'.join(data)), dtype='category')
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, monkeypatch

# Workflow
parser = all_parsers
heuristic = 2 ** 5
data = np.sort([str(i) for i in range(heuristic + 1)])
expected = DataFrame({'a': Categorical(data, ordered=True)})
with monkeypatch.context() as m:
    m.setattr(libparsers, 'DEFAULT_BUFFER_HEURISTIC', heuristic)
    actual = parser.read_csv(StringIO('a\n' + '\n'.join(data)), dtype='category')
actual['a'] = actual['a'].cat.reorder_categories(np.sort(actual.a.cat.categories), ordered=True)
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_categorical.py:119 | Complexity: Advanced | Last updated: 2026-06-02*