# How To: Na Trailing Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test na trailing columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
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

### Step 2: Assign data = 'Date,Currency,Symbol,Type,Units,UnitPrice,Cost,Tax\n2012-03-14,USD,AAPL,BUY,1000\n2012-05-12,USD,SBUX,SELL,500'

```python
data = 'Date,Currency,Symbol,Type,Units,UnitPrice,Cost,Tax\n2012-03-14,USD,AAPL,BUY,1000\n2012-05-12,USD,SBUX,SELL,500'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([['2012-03-14', 'USD', 'AAPL', 'BUY', 1000, np.nan, np.nan, np.nan], ['2012-05-12', 'USD', 'SBUX', 'SELL', 500, np.nan, np.nan, np.nan]], columns=['Date', 'Currency', 'Symbol', 'Type', 'Units', 'UnitPrice', 'Cost', 'Tax'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'Date,Currency,Symbol,Type,Units,UnitPrice,Cost,Tax\n2012-03-14,USD,AAPL,BUY,1000\n2012-05-12,USD,SBUX,SELL,500'
result = parser.read_csv(StringIO(data))
expected = DataFrame([['2012-03-14', 'USD', 'AAPL', 'BUY', 1000, np.nan, np.nan, np.nan], ['2012-05-12', 'USD', 'SBUX', 'SELL', 500, np.nan, np.nan, np.nan]], columns=['Date', 'Currency', 'Symbol', 'Type', 'Units', 'UnitPrice', 'Cost', 'Tax'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:467 | Complexity: Intermediate | Last updated: 2026-06-02*