"""
Complete V2 API Usage Example
All available endpoints in API V2

To use this example:
1. Set your API key below
2. Uncomment the sections you want to test
3. Replace placeholder IDs with real ones from your account
"""
import nlpearl as pearl
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================
pearl.api_key = "your_api_key_here"  # <-- SET YOUR API KEY
pearl.api_version = "v2"  # This is the default

print("=" * 60)
print("NLPearl API V2 - Complete Usage Example")
print("=" * 60)
print(f"API Version: {pearl.api_version}")
print(f"API URL: https://api.nlpearl.ai/v2")
print("=" * 60)

# ============================================================
# 1. ACCOUNT
# ============================================================
print("\n### 1. ACCOUNT ###")
print("-" * 60)

# Get Account Information
print("\n[1.1] Get Account")
try:
    account_info = pearl.Account.get_account()
    print(f"[OK] Account Name: {account_info['name']}")
    print(f"[OK] Credit Balance: {account_info['creditBalance']}")
    print(f"[OK] Total Agents: {account_info['totalAgents']}")
    print(f"[OK] Status: {account_info['status']}")
except Exception as e:
    print(f"[ERROR] Error: {e}")

# ============================================================
# 2. CALL OPERATIONS
# ============================================================
print("\n### 2. CALL OPERATIONS ###")
print("-" * 60)

# Get Call Information
print("\n[2.1] Get Call")
# call_id = "your_call_id_here"  # <-- REPLACE WITH REAL CALL ID
# try:
#     call_info = pearl.Call.get_call(call_id)
#     print(f"[OK] Call ID: {call_info['id']}")
#     print(f"[OK] Status: {call_info['status']}")
#     print(f"[OK] Duration: {call_info['duration']} seconds")
#     print(f"[OK] From: {call_info['from']}")
#     print(f"[OK] To: {call_info['to']}")
#     print(f"[OK] Conversation Status: {call_info['conversationStatus']}")
#     print(f"[OK] Overall Sentiment: {call_info.get('overallSentiment')}")
#     print(f"[OK] Call Transferred: {call_info.get('isCallTransferred')}")
#     if call_info.get('tags'):
#         print(f"[OK] Tags: {', '.join(call_info['tags'])}")
#     if call_info.get('summary'):
#         print(f"[OK] Summary: {call_info['summary']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set call_id to test")

# Delete Calls
print("\n[2.2] Delete Calls")
# call_ids = ["call_id_1", "call_id_2"]  # <-- REPLACE WITH REAL CALL IDs
# try:
#     result = pearl.Call.delete_calls(call_ids)
#     print(f"[OK] Calls deleted: {result}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set call_ids to test")

# ============================================================
# 3. PEARL OPERATIONS (V2 ONLY)
# ============================================================
print("\n### 3. PEARL OPERATIONS (V2 ONLY) ###")
print("-" * 60)

# Get All Pearls
print("\n[3.1] Get All Pearls")
try:
    pearls = pearl.Pearl.get_all()
    print(f"[OK] Total Pearls: {len(pearls)}")
    for p in pearls:
        type_name = "Inbound" if p['type'] == 1 else "Outbound" if p['type'] == 2 else "Unknown"
        print(f"  - {p['name']} (ID: {p['id']}, Type: {type_name}, Status: {p['status']})")
except Exception as e:
    print(f"[ERROR] Error: {e}")

# Get Specific Pearl
print("\n[3.2] Get Specific Pearl")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# try:
#     pearl_details = pearl.Pearl.get(pearl_id)
#     print(f"[OK] Name: {pearl_details['name']}")
#     print(f"[OK] Status: {pearl_details['status']}")
#     print(f"[OK] Phone Number: {pearl_details.get('phoneNumber', 'N/A')}")
#     print(f"[OK] Total Agents: {pearl_details['totalAgents']}")
#     print(f"[OK] Today's Calls: {pearl_details.get('totalTodayCalls', 0)}")
#     print(f"[OK] Ongoing Calls: {pearl_details.get('totalOngoingCalls', 0)}")
#     print(f"[OK] Calls in Queue: {pearl_details.get('totalOnQueue', 0)}")
#     
#     # For Outbound type
#     if pearl_details.get('totalLeads'):
#         print(f"[OK] Total Leads: {pearl_details['totalLeads']}")
#         print(f"[OK] Completed Leads: {pearl_details.get('totalLeadsCompleted', 0)}")
#         print(f"[OK] Successful Leads: {pearl_details.get('totalLeadsSuccess', 0)}")
#         print(f"[OK] Budget Total: {pearl_details.get('budgetTotal', 'N/A')}")
#         print(f"[OK] Budget Consumed: {pearl_details.get('budgetConsumed', 0)}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id to test")

# Set Pearl Active Status
print("\n[3.3] Set Pearl Active/Inactive")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# try:
#     # Activate
#     status = pearl.Pearl.set_active(pearl_id, is_active=True)
#     print(f"[OK] Activated: Status = {status}")
#     
#     # Deactivate
#     status = pearl.Pearl.set_active(pearl_id, is_active=False)
#     print(f"[OK] Deactivated: Status = {status}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id to test")

# Get Ongoing Calls
print("\n[3.4] Get Pearl Ongoing Calls")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# try:
#     ongoing = pearl.Pearl.get_ongoing_calls(pearl_id)
#     print(f"[OK] Ongoing Calls: {ongoing['totalOngoingCalls']}")
#     if 'totalOnQueue' in ongoing:
#         print(f"[OK] Calls in Queue: {ongoing['totalOnQueue']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id to test")

# Get Pearl Calls
print("\n[3.5] Get Pearl Calls")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# try:
#     calls = pearl.Pearl.get_calls(
#         pearl_id,
#         from_date=datetime(2024, 1, 1),
#         to_date=datetime(2024, 1, 31),
#         skip=0,
#         limit=10,
#         sort_prop="startTime",
#         is_ascending=False,
#         tags=["important"],  # Optional
#         statuses=[100, 130],  # Optional: 100=Success, 130=Completed
#         search_input="test"  # Optional
#     )
#     print(f"[OK] Total Calls Found: {calls['count']}")
#     for call in calls.get('results', [])[:5]:
#         print(f"  - Call {call['id']}: Status={call['status']}, Duration={call['duration']}s")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id to test")

# Get Pearl Analytics
print("\n[3.6] Get Pearl Analytics")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# try:
#     analytics = pearl.Pearl.get_analytics(
#         pearl_id,
#         from_date="2024-01-01T00:00:00.000Z",
#         to_date="2024-01-31T23:59:59.999Z"
#     )
#     
#     # Call Type (1=Inbound, 2=Outbound)
#     call_type = analytics.get('callType')
#     print(f"[OK] Call Type: {'Inbound' if call_type == 1 else 'Outbound' if call_type == 2 else 'Unknown'}")
#     
#     # Status Overview
#     overview = analytics['callsStatusOverview']
#     print(f"[OK] Total Calls: {overview['totalCalls']}")
#     print(f"[OK] Total Leads: {overview['totalLeads']}")
#     print(f"[OK] Successful: {overview['successful']}")
#     print(f"[OK] Unsuccessful: {overview['unsuccessful']}")
#     print(f"[OK] Need Retry: {overview['needRetry']}")
#     print(f"[OK] Completed: {overview['completed']}")
#     print(f"[OK] Unreachable: {overview['unreachable']}")
#     
#     # Sentiment Overview
#     sentiment = analytics['callsSentimentOverview']
#     print(f"[OK] Sentiment - Positive: {sentiment['positive']}, Neutral: {sentiment['neutral']}, Negative: {sentiment['negative']}")
#     
#     # Events Count
#     events = analytics['callEventsCounts']
#     print(f"[OK] Messages Taken: {events['takeMessageCount']}")
#     print(f"[OK] SMS Sent: {events['smsSentCount']}")
#     print(f"[OK] Calls Transferred: {events['callTransferredCount']}")
#     print(f"[OK] Calendars Booked: {events['calendarBookedCount']}")
#     print(f"[OK] Emails Sent: {events['emailSentCount']}")
#     
#     # Pickup Rate (for Outbound)
#     if analytics.get('callsPickupRateTimeLine'):
#         print(f"[OK] Has Pickup Rate Timeline: Yes")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id to test")

# ============================================================
# 4. LEAD MANAGEMENT (V2 - Uses pearl_id)
# ============================================================
print("\n### 4. LEAD MANAGEMENT (V2) ###")
print("-" * 60)

# Add Lead
print("\n[4.1] Add Lead")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# try:
#     new_lead = pearl.Outbound.add_lead(
#         pearl_id,  # Note: pearl_id in V2, not outbound_id!
#         phone_number="+1234567890",
#         external_id="ext_test_v2_123",
#         time_zone_id="Pacific Standard Time",
#         call_data={
#             "firstName": "Alice",
#             "lastName": "Smith",
#             "email": "alice.smith@example.com",
#             "company": "Tech Innovations Inc"
#         }
#     )
#     print(f"[OK] Lead Created: {new_lead}")
#     lead_id = new_lead.get('leadId')
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id to test")

# Get Lead by ID
print("\n[4.2] Get Lead by ID")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# lead_id = "your_lead_id"  # <-- REPLACE WITH REAL LEAD ID
# try:
#     lead = pearl.Outbound.get_lead_by_id(pearl_id, lead_id)
#     print(f"[OK] Lead ID: {lead['id']}")
#     print(f"[OK] Phone Number: {lead['phoneNumber']}")
#     print(f"[OK] External ID: {lead.get('externalId', 'N/A')}")
#     print(f"[OK] Time Zone: {lead.get('timeZone', 'N/A')}")
#     print(f"[OK] Status: {lead['status']}")
#     print(f"[OK] Created: {lead['created']}")
#     print(f"[OK] Call Data: {lead.get('callData', {})}")
#     print(f"[OK] Collected Data: {lead.get('collectedData', {})}")
#     
#     # Last Call Info
#     if lead.get('lastCall'):
#         last_call = lead['lastCall']
#         print(f"[OK] Last Call ID: {last_call.get('id')}")
#         print(f"[OK] Last Call Duration: {last_call.get('duration')}s")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id and lead_id to test")

# Get Lead by External ID
print("\n[4.3] Get Lead by External ID")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# external_id = "ext_test_v2_123"  # <-- REPLACE WITH REAL EXTERNAL ID
# try:
#     lead = pearl.Outbound.get_lead_by_external_id(pearl_id, external_id)
#     print(f"[OK] Lead ID: {lead['id']}")
#     print(f"[OK] Phone Number: {lead['phoneNumber']}")
#     print(f"[OK] Status: {lead['status']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id and external_id to test")

# Get Lead by Phone Number
print("\n[4.4] Get Lead by Phone Number")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# phone_number = "+1234567890"  # <-- REPLACE WITH REAL PHONE NUMBER
# try:
#     lead = pearl.Outbound.get_lead_by_phone_number(pearl_id, phone_number)
#     print(f"[OK] Lead ID: {lead['id']}")
#     print(f"[OK] Phone Number: {lead['phoneNumber']}")
#     print(f"[OK] Status: {lead['status']}")
#     print(f"[OK] External ID: {lead.get('externalId', 'N/A')}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id and phone_number to test")

# Update Lead
print("\n[4.5] Update Lead")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# lead_id = "your_lead_id"  # <-- REPLACE WITH REAL LEAD ID
# try:
#     updated_lead = pearl.Outbound.update_lead(
#         pearl_id,
#         lead_id,
#         phone_number="+9876543210",  # Optional
#         external_id="updated_v2_ext_id",  # Optional
#         time_zone_id="Eastern Standard Time",  # Optional
#         status=100,  # Optional: 100=Success
#         call_data={"notes": "Updated in V2", "priority": "high"}  # Optional
#     )
#     print(f"[OK] Lead Updated: {updated_lead['id']}")
#     print(f"[OK] New Status: {updated_lead['status']}")
#     print(f"[OK] New Phone: {updated_lead['phoneNumber']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id and lead_id to test")

# Search Leads
print("\n[4.6] Search Leads")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# try:
#     leads = pearl.Outbound.get_leads(
#         pearl_id,
#         skip=0,
#         limit=10,
#         sort_prop="created",
#         is_ascending=False,
#         statuses=[1, 10],  # Note: V2 uses 'statuses' (plural)
#         search_input="Alice"  # Optional
#     )
#     print(f"[OK] Total Leads Found: {leads['count']}")
#     for lead in leads.get('results', [])[:5]:
#         print(f"  - Lead {lead['id']}: Phone={lead['phoneNumber']}, Status={lead['status']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id to test")

# Delete Leads by ID
print("\n[4.7] Delete Leads by ID")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# lead_ids = ["lead_id_1", "lead_id_2"]  # <-- REPLACE WITH REAL LEAD IDs
# try:
#     result = pearl.Outbound.delete_leads(pearl_id, lead_ids)
#     print(f"[OK] Leads Deleted: {result}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id and lead_ids to test")

# Delete Leads by External ID
print("\n[4.8] Delete Leads by External ID")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# external_ids = ["ext_v2_id_1", "ext_v2_id_2"]  # <-- REPLACE WITH REAL EXTERNAL IDs
# try:
#     result = pearl.Outbound.delete_leads_by_external_id(pearl_id, external_ids)
#     print(f"[OK] Leads Deleted by External ID: {result}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id and external_ids to test")

# ============================================================
# 5. MEMORY MANAGEMENT
# ============================================================
print("\n### 5. MEMORY MANAGEMENT ###")
print("-" * 60)

# Reset Memory
print("\n[5.1] Reset Customer Memory")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# phone_number = "+1234567890"  # <-- REPLACE WITH REAL PHONE NUMBER
# try:
#     result = pearl.Pearl.reset_memory(pearl_id, phone_number)
#     print(f"[OK] Memory Reset: {result}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id and phone_number to test")

# Alternative: reset_customer_memory (same as reset_memory)
print("\n[5.2] Reset Customer Memory (Alternative)")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# phone_number = "+1234567890"  # <-- REPLACE WITH REAL PHONE NUMBER
# try:
#     result = pearl.Pearl.reset_customer_memory(pearl_id, phone_number)
#     print(f"[OK] Memory Reset: {result}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id and phone_number to test")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("V2 API Testing Complete!")
print("=" * 60)
print("\nEndpoints Tested:")
print("  1. Account: get_account()")
print("  2. Call: get_call(), delete_calls()")
print("  3. Pearl: get_all(), get(), set_active(), get_calls(),")
print("            get_ongoing_calls(), get_analytics()")
print("  4. Leads: add_lead(), get_lead_by_id(), get_lead_by_external_id(),")
print("            get_lead_by_phone_number(), update_lead(), get_leads(),")
print("            delete_leads(), delete_leads_by_external_id()")
print("  5. Memory: reset_memory(), reset_customer_memory()")
print("\nTotal: 17 endpoints")
print("\nKey V2 Features:")
print("  - Unified Pearl entity (replaces Inbound/Outbound separation)")
print("  - Uses pearl_id instead of outbound_id/inbound_id")
print("  - Enhanced analytics with call type information")
print("  - Sentiment analysis included")
print("  - Pickup rate timeline for outbound campaigns")
print("=" * 60)

# ============================================================
# V2 vs V1 DIFFERENCES
# ============================================================
print("\n### V2 vs V1 KEY DIFFERENCES ###")
print("-" * 60)
print("1. ID Parameter:")
print("   V1: outbound_id / inbound_id")
print("   V2: pearl_id")
print()
print("2. Pearl Entity:")
print("   V1: Separate Inbound and Outbound classes")
print("   V2: Unified Pearl class")
print()
print("3. Lead Operations:")
print("   V1: pearl.Outbound.add_lead(outbound_id, ...)")
print("   V2: pearl.Outbound.add_lead(pearl_id, ...)")
print()
print("4. Analytics:")
print("   V1: pearl.Outbound.get_analytics(outbound_id, ...)")
print("   V2: pearl.Pearl.get_analytics(pearl_id, ...)")
print()
print("5. Not Available in V2:")
print("   - Inbound.get_all() >> Use Pearl.get_all()")
print("   - Outbound.get_all() >> Use Pearl.get_all()")
print("   - Outbound.make_call() >> Different mechanism")
print("   - Outbound.get_call_requests() >> Not in V2")
print()
print("6. New in V2:")
print("   - Pearl.get_all() - Get all pearls (inbound + outbound)")
print("   - Pearl.get_analytics() - Unified analytics")
print("   - Enhanced sentiment analysis")
print("   - Call type information in analytics")
print("=" * 60)
