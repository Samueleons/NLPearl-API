# Testing Guide - NLPearl API V1 & V2

## How to Use the Example Files

You now have two comprehensive example files that contain **ALL** available endpoints for V1 and V2.

### Files Created

1. **`example_v1_usage.py`** - All V1 API endpoints (24+ endpoints)
2. **`example_v2_usage.py`** - All V2 API endpoints (17 endpoints)

## Quick Start

### Step 1: Set Your API Key

Open each example file and replace:
```python
pearl.api_key = "your_api_key_here"  # <-- SET YOUR API KEY
```

### Step 2: Run the Examples

#### Test V1 API
```bash
python example_v1_usage.py
```

#### Test V2 API
```bash
python example_v2_usage.py
```

### Step 3: Uncomment Sections to Test

Each endpoint section is commented out. To test a specific endpoint:

1. Find the section (e.g., `[3.2] Get Specific Inbound`)
2. Uncomment the code block
3. Replace placeholder IDs with real ones from your account
4. Run the file again

**Example:**
```python
# Before
# inbound_id = "your_inbound_id"  # <-- REPLACE
# try:
#     inbound = pearl.Inbound.get(inbound_id)
#     print(f"Name: {inbound['name']}")
# except Exception as e:
#     print(f"Error: {e}")

# After
inbound_id = "6655dc82c953bf1009e52be6"  # Your real ID
try:
    inbound = pearl.Inbound.get(inbound_id)
    print(f"Name: {inbound['name']}")
except Exception as e:
    print(f"Error: {e}")
```

## V1 Example - All Endpoints

### Account (1 endpoint)
- `[1.1]` Get Account

### Call Operations (2 endpoints)
- `[2.1]` Get Call
- `[2.2]` Delete Calls

### Inbound Operations (6 endpoints)
- `[3.1]` Get All Inbounds
- `[3.2]` Get Specific Inbound
- `[3.3]` Set Inbound Active/Inactive
- `[3.4]` Get Inbound Ongoing Calls
- `[3.5]` Search Inbound Calls
- `[3.6]` Get Inbound Analytics

### Outbound Operations (5 endpoints)
- `[4.1]` Get All Outbounds
- `[4.2]` Get Specific Outbound
- `[4.3]` Set Outbound Active/Inactive
- `[4.4]` Get Outbound Calls
- `[4.5]` Get Outbound Analytics

### Lead Management (8 endpoints)
- `[5.1]` Add Lead
- `[5.2]` Get Lead by ID
- `[5.3]` Get Lead by External ID
- `[5.4]` Get Lead by Phone Number
- `[5.5]` Update Lead
- `[5.6]` Search Leads
- `[5.7]` Delete Leads
- `[5.8]` Delete Leads by External ID

### Outbound Calling - V1 Only (3 endpoints)
- `[6.1]` Make Call
- `[6.2]` Get Call Request
- `[6.3]` Search Call Requests

### Memory Management (1 endpoint)
- `[7.1]` Reset Customer Memory

**Total: 26 endpoints**

## V2 Example - All Endpoints

### Account (1 endpoint)
- `[1.1]` Get Account

### Call Operations (2 endpoints)
- `[2.1]` Get Call
- `[2.2]` Delete Calls

### Pearl Operations - V2 Only (6 endpoints)
- `[3.1]` Get All Pearls
- `[3.2]` Get Specific Pearl
- `[3.3]` Set Pearl Active/Inactive
- `[3.4]` Get Pearl Ongoing Calls
- `[3.5]` Get Pearl Calls
- `[3.6]` Get Pearl Analytics

### Lead Management (8 endpoints)
- `[4.1]` Add Lead (uses pearl_id)
- `[4.2]` Get Lead by ID
- `[4.3]` Get Lead by External ID
- `[4.4]` Get Lead by Phone Number
- `[4.5]` Update Lead
- `[4.6]` Search Leads
- `[4.7]` Delete Leads by ID
- `[4.8]` Delete Leads by External ID

### Memory Management (2 endpoints)
- `[5.1]` Reset Memory
- `[5.2]` Reset Customer Memory (alternative)

**Total: 19 endpoints**

## Testing Workflow

### 1. Start with Account (Always Works)
```python
# In either example file
pearl.api_key = "your_real_api_key"
# Uncomment section [1.1]
# Run the file
```

### 2. Get Your IDs
Run the "Get All" methods to get IDs for testing:

**V1:**
```python
# Uncomment [3.1] to get inbound IDs
# Uncomment [4.1] to get outbound IDs
```

**V2:**
```python
# Uncomment [3.1] to get pearl IDs
```

### 3. Test Individual Endpoints
Use the IDs from step 2 to test specific endpoints:

```python
# Example: Testing Get Specific Inbound in V1
inbound_id = "6655dc82c953bf1009e52be6"  # From [3.1]
# Uncomment [3.2]
```

### 4. Test Sequential Operations
Some operations are sequential:

```python
# V1 Example: Add → Get → Update → Delete Lead
# 1. Uncomment [5.1] Add Lead → get lead_id
# 2. Uncomment [5.2] Get Lead by ID → verify
# 3. Uncomment [5.5] Update Lead → modify
# 4. Uncomment [5.7] Delete Leads → cleanup
```

## What the Examples Show

### V1 Example Shows:
- ✅ All V1 endpoints with correct parameters
- ✅ Proper use of `outbound_id` and `inbound_id`
- ✅ V1-specific methods like `make_call()`
- ✅ How to search calls/leads with date ranges
- ✅ How to manage inbound and outbound separately

### V2 Example Shows:
- ✅ All V2 endpoints with correct parameters
- ✅ Proper use of `pearl_id` (unified identifier)
- ✅ V2-specific Pearl operations
- ✅ Enhanced analytics with call type
- ✅ Unified pearl management

## Expected Output

### With Fake API Key:
```
[ERROR] Expecting value: line 1 column 1 (char 0)
```
This is normal - API authentication fails.

### With Real API Key:
```
[OK] Account Name: Your Company
[OK] Credit Balance: 100.50
[OK] Total Agents: 5
```

### Commented Sections:
```
>> Uncomment code above and set pearl_id to test
```
This means the section is ready but commented - uncomment to test.

## Tips

### 1. Test Incrementally
Don't uncomment everything at once. Test one section at a time.

### 2. Save Real IDs
When you get IDs from "Get All" methods, save them in variables at the top:
```python
# Real IDs from your account
PEARL_ID = "6655dc82c953bf1009e52be6"
INBOUND_ID = "abc123..."
OUTBOUND_ID = "def456..."
```

### 3. Error Handling
All examples include try/except blocks. If you get an error, the script will continue.

### 4. Sequential Testing
Some operations depend on previous ones:
- Create a lead before updating it
- Get IDs before using them in specific calls
- Delete test data at the end

## Quick Reference

### V1 Class Usage:
```python
pearl.api_version = "v1"
pearl.Inbound.get_all()      # Works
pearl.Outbound.get_all()     # Works
pearl.Pearl.get_all()        # Error - V2 only
```

### V2 Class Usage:
```python
pearl.api_version = "v2"
pearl.Pearl.get_all()        # Works
pearl.Inbound.get_all()      # Error - V1 only
pearl.Outbound.get_all()     # Error - V1 only
pearl.Outbound.add_lead()    # Works (uses pearl_id)
```

## Need Help?

Check the output messages:
- `[OK]` - Method executed successfully
- `[ERROR]` - Something went wrong (check error message)
- `>>` - Section is commented, uncomment to test

## Ready to Deploy?

After testing all endpoints:
1. Update version in `setup.py` to 1.0.7
2. Build the package: `python setup.py sdist bdist_wheel`
3. Upload to PyPI: `twine upload dist/nlpearl-1.0.7*`

---

**Both example files are ready to run!** Just set your API key and start testing. 🎉

