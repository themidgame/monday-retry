A package that retries failed Monday API requests.

**STEPS TO USE**:
1. pip install git+https://github.com/themidgame/monday-retry@{version}
2. `monday_retry.monday import Monday`
3. `monday = Monday({monday_api_token})`
4. To initiate error tracking in Mixpanel `monday.initiate_tracking_with_mixpanel(mixpanel_token)`
5. `response = monday.make_monday_call_with_retry(query, timeout=20, retry_count=3)`


Note:
1. _timeout_ and _retry_count_ are optional and both default to 30 and 2 respectively
2. Error tracking is optional

    # **HAPPY MONDAY!**