# Test Scripts

This directory contains test scripts for the OA Server project.

## Available Tests

### OBS WebSocket Tests

1. **`test_obs_connection.py`** - Basic OBS WebSocket connection test
   ```bash
   cd tests
   python test_obs_connection.py
   ```

2. **`obs_test.py`** - Comprehensive OBS functionality test with CLI options
   ```bash
   cd tests
   python obs_test.py --host 192.168.0.128 --port 4455
   ```

## Requirements

- OBS Studio running with WebSocket server enabled
- Python dependencies installed via `uv sync`
- Network connectivity to OBS instance

## Running Tests

From the project root:
```bash
# Run basic connection test
python tests/test_obs_connection.py

# Run comprehensive test with options
python tests/obs_test.py --host 192.168.0.128
```

From the tests directory:
```bash
cd tests
python test_obs_connection.py
python obs_test.py
```