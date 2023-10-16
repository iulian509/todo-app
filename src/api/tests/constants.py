# Test data
TEST_INPUT = {"title": "TestTitle", "priority": 1}
TEST_UPDATE_INPUT = {"title": "UpdatedTitle", "priority": 5}
TEST_INVALID_INPUT = {"title": "TestTitle", "priority": 0}
TEST_ID = 1
TEST_WRONG_ID = 3
TEST_RESPONSE = {"id": TEST_ID, **TEST_INPUT}
TEST_UPDATE_RESPONSE = {"id": 1, **TEST_UPDATE_INPUT}
