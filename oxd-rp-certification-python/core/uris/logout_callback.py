# File: /oxd-rp-certification-python/core/uris/logout_callback.py
# Purpose: Act as the /logout_callback/ path

# Import required modules
import os
import sys
import oxdpython
from flask import request, make_response, set_cookie

# Define the generate_response() function
def generate_response(oxd_client):
	# Function: generate_response()
	# Purpose: Callback for /logout/
	# Arguments: None
	
	# Create the response
	response = make_response("Logging out...")
	
	# Clear the cookies by setting them to null values
	response.set_cookie('sub', 'null', expires=0)
	response.set_cookie('session_id', 'null', expires=0)

	# Return the response
	return response
