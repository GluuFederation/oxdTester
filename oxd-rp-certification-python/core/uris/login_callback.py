# File: /oxd-rp-certification-python/core/uris/authorize.py
# Purpose: Act as the /authorize/ path

# Import required modules
import os
import sys
import oxdpython
from flask import request, make_response

# Define the generate_response() function
def generate_response(oxd_client):
	# Function: generate_response()
	# Purpose: Callback for /authorize/
	# Arguments:
	#	oxd_client - The oxd client
	
	# Fetch the code and state from Flask request
	code = request.args.get('code')
	state = request.args.get('state')
	
	# Set the tokens and claims
	tokens = oxd_client.get_tokens_by_code(code, state)
	claims = oxd_client.get_user_info(tokens['access_token'])
	
	# Set the response to the home screen
	response = make_response(render_template("oxd-rp-certification-python/resources/site/index.html"))
	
	# Set the cookies
	response.set_cookie('sub', claims['sub'][0])
	response.set_cookie('session_id', request.args.get('session_id'))
	
	# Return the response
	return response
