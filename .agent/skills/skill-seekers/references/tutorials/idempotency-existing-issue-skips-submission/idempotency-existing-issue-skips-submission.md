# How To: Idempotency Existing Issue Skips Submission

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: WS11: if an issue already exists, skip the prompt + submission.

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
# Fixtures: tmp_path, capsys
```

## Step-by-Step Guide

### Step 1: 'WS11: if an issue already exists, skip the prompt + submission.'

```python
'WS11: if an issue already exists, skip the prompt + submission.'
```

**Verification:**
```python
assert submit.call_count == 0
```

### Step 2: Assign cfg = self._write_cfg(...)

```python
cfg = self._write_cfg(tmp_path, 'newlib')
```

**Verification:**
```python
assert prompt.call_count == 0
```

### Step 3: Assign submit = self._async_mock(...)

```python
submit = self._async_mock()
```

**Verification:**
```python
assert 'issues/42' in captured.out
```

### Step 4: Assign prompt = self._async_mock(...)

```python
prompt = self._async_mock()
```

### Step 5: Assign find = self._async_mock(...)

```python
find = self._async_mock(return_value='https://github.com/y/z/issues/42')
```

**Verification:**
```python
assert submit.call_count == 0
```

### Step 6: Assign captured = capsys.readouterr(...)

```python
captured = capsys.readouterr()
```

**Verification:**
```python
assert 'issues/42' in captured.out
```

### Step 7: Call self._run()

```python
self._run(maybe_publish([cfg], skip_prompt=False))
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, capsys

# Workflow
'WS11: if an issue already exists, skip the prompt + submission.'
cfg = self._write_cfg(tmp_path, 'newlib')
submit = self._async_mock()
prompt = self._async_mock()
find = self._async_mock(return_value='https://github.com/y/z/issues/42')
with patch.dict('os.environ', {'GITHUB_TOKEN': 'fake'}), patch('skill_seekers.cli.scan_command._submit_config', submit), patch('skill_seekers.cli.scan_command._prompt_async', prompt), patch('skill_seekers.cli.scan_command._find_existing_issue', find):
    self._run(maybe_publish([cfg], skip_prompt=False))
assert submit.call_count == 0
assert prompt.call_count == 0
captured = capsys.readouterr()
assert 'issues/42' in captured.out
```

## Next Steps


---

*Source: test_scan_command.py:799 | Complexity: Advanced | Last updated: 2026-06-02*