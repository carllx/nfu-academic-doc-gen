# How To: Missing Github Token Skips Prompt

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Without GITHUB_TOKEN, don't ask 5 questions and fail 5 times.

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

### Step 1: "Without GITHUB_TOKEN, don't ask 5 questions and fail 5 times."

```python
"Without GITHUB_TOKEN, don't ask 5 questions and fail 5 times."
```

**Verification:**
```python
assert prompt.call_count == 0
```

### Step 2: Assign cfg = self._write_cfg(...)

```python
cfg = self._write_cfg(tmp_path, 'newlib')
```

**Verification:**
```python
assert submit.call_count == 0
```

### Step 3: Assign submit = self._async_mock(...)

```python
submit = self._async_mock()
```

**Verification:**
```python
assert 'GITHUB_TOKEN' in captured.out
```

### Step 4: Assign prompt = self._async_mock(...)

```python
prompt = self._async_mock()
```

**Verification:**
```python
assert prompt.call_count == 0
```

### Step 5: Assign captured = capsys.readouterr(...)

```python
captured = capsys.readouterr()
```

**Verification:**
```python
assert 'GITHUB_TOKEN' in captured.out
```

### Step 6: Call self._run()

```python
self._run(maybe_publish([cfg], skip_prompt=False))
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, capsys

# Workflow
"Without GITHUB_TOKEN, don't ask 5 questions and fail 5 times."
cfg = self._write_cfg(tmp_path, 'newlib')
submit = self._async_mock()
prompt = self._async_mock()
with patch('skill_seekers.cli.scan_command._submit_config', submit), patch.dict('os.environ', {}, clear=True), patch('skill_seekers.cli.scan_command._prompt_async', prompt):
    self._run(maybe_publish([cfg], skip_prompt=False))
assert prompt.call_count == 0
assert submit.call_count == 0
captured = capsys.readouterr()
assert 'GITHUB_TOKEN' in captured.out
```

## Next Steps


---

*Source: test_scan_command.py:768 | Complexity: Advanced | Last updated: 2026-06-02*