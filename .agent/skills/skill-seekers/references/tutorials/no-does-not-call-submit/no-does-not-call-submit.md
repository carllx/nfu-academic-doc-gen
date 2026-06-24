# How To: No Does Not Call Submit

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test no does not call submit

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `json`
- `pathlib`
- `unittest.mock`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.signal_collectors`
- `asyncio`
- `skill_seekers.cli.main`
- `skill_seekers.cli.main`
- `argparse`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.parsers`
- `argparse`
- `skill_seekers.cli.parsers.scan_parser`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign cfg = self._write_cfg(...)

```python
cfg = self._write_cfg(tmp_path, 'newlib')
```

**Verification:**
```python
assert submit.call_count == 0
```

### Step 2: Assign submit = self._async_mock(...)

```python
submit = self._async_mock()
```

### Step 3: Assign prompt = self._async_mock(...)

```python
prompt = self._async_mock(return_value='n')
```

### Step 4: Assign find = self._async_mock(...)

```python
find = self._async_mock(return_value=None)
```

**Verification:**
```python
assert submit.call_count == 0
```

### Step 5: Call self._run()

```python
self._run(maybe_publish([cfg], skip_prompt=False))
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
cfg = self._write_cfg(tmp_path, 'newlib')
submit = self._async_mock()
prompt = self._async_mock(return_value='n')
find = self._async_mock(return_value=None)
with patch.dict('os.environ', {'GITHUB_TOKEN': 'fake'}), patch('skill_seekers.cli.scan_command._submit_config', submit), patch('skill_seekers.cli.scan_command._prompt_async', prompt), patch('skill_seekers.cli.scan_command._find_existing_issue', find):
    self._run(maybe_publish([cfg], skip_prompt=False))
assert submit.call_count == 0
```

## Next Steps


---

*Source: test_scan_command.py:754 | Complexity: Advanced | Last updated: 2026-06-02*