# File: /core/flask_server.py
# Purpose: Serve the webpage using Flask

# Import required modules
import os
import sys
import pdb
import logging
import configparser
import urllib2
import json
from webfinger import finger
import oxdpython
from oxdpython import Client
from flask import Flask, redirect, render_template
import uris.authorize
import uris.login_callback
import uris.logout

# Create the Flask app
app = Flask(__name__)

# Set the configuration file
config = os.getcwd() + "/config.cfg"

# Set the oxd client
oxd_client = oxdpython.Client(config)

# Fetch the configuration information
op_openid_conf_response = urllib2.urlopen("https://rp.certification.openid.net:8080/mod_auth_openidc/rp-response_type-code/.well-known/openid-configuration") # QUICK FIX, REPLACE WITH VALUE FROM CONFIG FILE

# Read the OP's configuration
op_openid_conf = op_openid_conf_response.read()

# Define the process_op_config() function
def process_op_config():
	# Function: process_op_config()
	# Purpose: Process the OP's /.well-known/openid-configuration and return important values
	# Arguments: None
	
	
	
	# Attempt to get the OP configuration
	try:
		# Fetch the configuration information
		op_openid_conf_response = urllib2.urlopen("https://rp.certification.openid.net:8080/mod_auth_openidc/rp-response_type-code/.well-known/openid-configuration") # QUICK FIX, REPLACE WITH VALUE FROM CONFIG FILE

		# Read the OP's configuration
		op_openid_conf = op_openid_conf_response.read()
	except IOError:
		# Display an error message and exit
		print("[E] Error getting OP's OpenID configuration from /.well-known/openid-configuration. Please ensure that your OP is running properly and try again.")
		exit(0)
		
		
	# Parse the JSON response
	parsed_json = json.loads(op_openid_conf)
	
	# Set and display important values
	print("[I] Endpoints:")
	authorization_endpoint = parsed_json["authorization_endpoint"] # The authorization endpoint
	print("[+] Authorization Endpoint: {}".format(authorization_endpoint))
	registration_endpoint = parsed_json["registration_endpoint"] # The registration endpoint
	print("[+] Registration Endpoint: {}".format(registration_endpoint))
	token_endpoint = parsed_json["token_endpoint"] # The token endpoint
	print("[+] Token Endpoint: {}".format(token_endpoint))
	userinfo_endpoint = parsed_json["userinfo_endpoint"] # The userinfo endpoint
	print("[+] UserInfo Endpoint: {}".format(userinfo_endpoint))


# Route and define the index() function
@app.route("/")
def index():
	# Function: index()
	# Purpose: Act as the index directory of the website and register site
	# Arguments: None
	
	# Set the oxd client
	oxd_client = oxdpython.Client(config)
	
	# Register the site
	global oxd_id 
	oxd_id = oxd_client.register_site()
	
	# Specify the authorization URL
	auth_url = oxd_client.get_authorization_url()

	# Parse the OP servers configuration
	process_op_config()
	
	# Specify the path of the index file
	webpage_index_path = "oxd-rp-certification-python/resources/site/index.html"
	
	# Open the index file
	webpage_index = open(webpage_index_path, "r")
	
	# Return the contents of the file
	return webpage_index.read()
	
# Route and define the test_1() function
@app.route("/test_1/", methods=["POST", "GET"])
def test_1():
	# Function: test_1()
	# Purpose: Serve as the first test, preforming a simple Authorization Code Flow
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-response_type-code"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-response_type-code.txt"
	
	# Fetch the authorization URL
	#authorization_url = oxd_client.get_authorization_url()
 
# Route and define the test_2() function
@app.route("/test_2/", methods=["POST", "GET"])
def test_2():
	# Function: test_2()
	# Purpose: Serve as the second test, requesting claims using scope values
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-scope-userinfo-claims"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-scope-userinfo-claims.txt"
	
# Route and define the test_3() function
@app.route("/test_3/", methods=["POST", "GET"])
def test_3():
	# Function: test_3()
	# Purpose: Serve as the third test, passing a 'nonce' value in the authentication request and validating it
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-nonce-invalid"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-nonce-invalid.txt"
	
# Route and define the test_4() function
@app.route("/test_4/", methods=["POST", "GET"])
def test_4():
	# Function: test_4()
	# Purpose: Serve as the fourth test, using 'client_secret_basic' to authenticate 
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-token_endpoint-client_secret_basic"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-token_endpoint-client_secret_basic.txt"
	
# Route and define the test_5() function
@app.route("/test_5/", methods=["POST", "GET"])
def test_5():
	# Function: test_5()
	# Purpose: Serve as the fifth test, requesting an ID token and verifying its signature with a key provided by the issuer token
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-id_token-kid-absent-single-jwks"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-id_token-kid-absent-single-jwks.txt"
	
# Route and define the test_6() function
@app.route("/test_6/", methods=["POST", "GET"])
def test_6():
	# Function: test_6()
	# Purpose: Serve as the sixth test, request an ID token and verify its 'iat' value
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-id_token-iat"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-id_token-iat.txt"
	
# Route and define the test_7() function
@app.route("/test_7/", methods=["POST", "GET"])
def test_7():
	# Function: test_7()
	# Purpose: Serve as the seventh test, request an ID token and verify its 'aud' value
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/rp-id_token-aud"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-id_token-aud.txt"
	
# Route and define the test_8() function
@app.route("/test_8/", methods=["POST", "GET"])
def test_8():
	# Function: test_8()
	# Purpose: Serve as the eighth test, requesting an ID token and verifying its signature with multiple keys from the issuer
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-id_token-kid-absent-multiple-jwks"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-id_token-kid-absent-multiple-jwks.txt"
	
# Route and define the test_9() function
@app.route("/test_9/", methods=["POST", "GET"])
def test_9():
	# Function: test_9()
	# Purpose: Serve as the ninth test, using code flow to retrieve an unsigned ID token
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-id_token-sig-none"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-id_token-sig-none.txt"

# Route and define the test_10() function
@app.route("/test_10/", methods=["POST", "GET"])
def test_10():
	# Function: test_10()
	# Purpose: Serve as the tenth test, requesting a signed ID token and verifying it using keys from the issuer
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-id_token-sig-rs256"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-id_token-sig-rs256.txt"
	
# Route and define the test_11() function
@app.route("/test_11/", methods=["POST", "GET"])
def test_11():
	# Function: test_11()
	# Purpose: Serve as the eleventh test, requesting an ID token and verifying it has a 'sub' value
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-id_token-sub"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-id_token-sub.txt"
	
# Route and define the test_12() function
@app.route("/test_12/", methods=["POST", "GET"])
def test_12():
	# Function: test_12()
	# Purpose: Serve as the twelvth test, requesting an ID token and verifying it with keys from the issuer
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-id_token-bad-sig-rs256"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-id_token-bad-sig-rs256.txt"
	
# Route and define the test_13() function
@app.route("/test_13/", methods=["POST", "GET"])
def test_13():
	# Function: test_13()
	# Purpose: Serve as the thirteenth test, retrieving an ID token and verifying its 'iss' value
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-id_token-issuer-mismatch"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-id_token-issuer-mismatch.txt"
	
# Route and define the test_14() function
@app.route("/test_14/", methods=["POST", "GET"])
def test_14():
	# Function: test_14()
	# Purpose: Serve as the fourteenth test, making a userinfo request and verifying the 'sub' value by comparing it to the 'sub' value of the ID token
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-userinfo-bad-sub-claim"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-userinfo-bad-sub-claim.txt"
	
# Route and define the test_15() function
@app.route("/test_15/", methods=["POST", "GET"])
def test_15():
	# Function: test_15()
	# Purpose: Serve as the fifteenth test, passing the access token while using the "Bearer" authentication scheme during a userinfo request
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-userinfo-bad-sub-claim"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-userinfo-bad-sub-claim.txt"
