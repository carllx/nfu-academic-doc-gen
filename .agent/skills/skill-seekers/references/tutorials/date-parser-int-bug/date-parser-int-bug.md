# How To: Date Parser Int Bug

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date parser int bug

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `dateutil.parser`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `pandas.core.tools.datetimes`
- `pandas.io.parsers`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'posix_timestamp,elapsed,sys,user,queries,query_time,rows,accountid,userid,contactid,level,silo,method\n1343103150,0.062353,0,4,6,0.01690,3,12345,1,-1,3,invoice_InvoiceResource,search\n'

```python
data = 'posix_timestamp,elapsed,sys,user,queries,query_time,rows,accountid,userid,contactid,level,silo,method\n1343103150,0.062353,0,4,6,0.01690,3,12345,1,-1,3,invoice_InvoiceResource,search\n'
```

### Step 3: Assign result = parser.read_csv_check_warnings(...)

```python
result = parser.read_csv_check_warnings(FutureWarning, "use 'date_format' instead", StringIO(data), index_col=0, parse_dates=[0], date_parser=lambda x: datetime.fromtimestamp(int(x), tz=timezone.utc).replace(tzinfo=None), raise_on_extra_warnings=False)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0.062353, 0, 4, 6, 0.0169, 3, 12345, 1, -1, 3, 'invoice_InvoiceResource', 'search']], columns=['elapsed', 'sys', 'user', 'queries', 'query_time', 'rows', 'accountid', 'userid', 'contactid', 'level', 'silo', 'method'], index=Index([Timestamp('2012-07-24 04:12:30')], name='posix_timestamp'))
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
data = 'posix_timestamp,elapsed,sys,user,queries,query_time,rows,accountid,userid,contactid,level,silo,method\n1343103150,0.062353,0,4,6,0.01690,3,12345,1,-1,3,invoice_InvoiceResource,search\n'
result = parser.read_csv_check_warnings(FutureWarning, "use 'date_format' instead", StringIO(data), index_col=0, parse_dates=[0], date_parser=lambda x: datetime.fromtimestamp(int(x), tz=timezone.utc).replace(tzinfo=None), raise_on_extra_warnings=False)
expected = DataFrame([[0.062353, 0, 4, 6, 0.0169, 3, 12345, 1, -1, 3, 'invoice_InvoiceResource', 'search']], columns=['elapsed', 'sys', 'user', 'queries', 'query_time', 'rows', 'accountid', 'userid', 'contactid', 'level', 'silo', 'method'], index=Index([Timestamp('2012-07-24 04:12:30')], name='posix_timestamp'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:732 | Complexity: Intermediate | Last updated: 2026-06-02*