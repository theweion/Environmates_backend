import json
import pytest


## Test for 200 status code on user route
def test_response_200(api):
	response = api.get('/')
	assert response.status_code == 200


def test_user_registration_fail(api):
	response = api.post("/users/register", data={"username":"just-the-username"})
	assert response.text == "Something went wrong during registration."
	assert response.status_code == 300

# def test_user_found_from_id(api):
# 	response = api.get("/users/0")
# 	assert response.status_code == 200
# 	assert response.json == {"user":"user"}




# # Check if token has been generated for user
# def test_token_generated(api):
#     # Generate token for user
#     token = api.generateToken(1)
#     # Check if token is valid
#     assert api.verifyToken(token) == True
#     # Check if token is invalid
#     assert api.verifyToken("invalid token") == False
#     # Check if token is valid with wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id
#     assert api.verifyToken(token, user_id=1) == True
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verify