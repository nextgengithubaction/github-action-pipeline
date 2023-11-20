import requests
import time
import sys

# Check if both environment and tag are provided as command line arguments
if len(sys.argv) < 3:
    print("Usage: python script.py <environment> <tag>")
    sys.exit(1)

# Extract environment and tag from command line arguments
environment = sys.argv[1]
tag = sys.argv[2]

# Initial request to trigger deployment
initial_url = 'https://app.harness.io/gateway/pipeline/api/webhook/custom/6vtQtaXZSKS1O_dvIEhK-Q/v3?accountIdentifier=1DNqO1mMS2G3HdY8XG2nGg&orgIdentifier=default&projectIdentifier=default_project&pipelineIdentifier=dotnet_deployment&triggerIdentifier=initiate_harness_deployment'
initial_payload = {'environment': environment, 'tag': tag}
initial_headers = {'Content-Type': 'application/json'}
initial_response = requests.post(initial_url, json=initial_payload, headers=initial_headers).json()

# Extracting apiUrl from the response and cleaning leading/trailing spaces
api_url = initial_response['data']['apiUrl'].strip()

# Wait for 3 seconds before initiating the second API call
time.sleep(3)

# Set timeout and interval for checking pipeline status
timeout_seconds = 300  # 5 minutes
check_interval_seconds = 2

# Timestamp when the script started
start_time = time.time()

while True:
    # Second request using the cleaned apiUrl
    try:
        second_response = requests.get(api_url, headers={'x-api-key': 'pat.1DNqO1mMS2G3HdY8XG2nGg.655816c3326e3c4c594d34bb.rA9amhFekqF3lDJu3UaM'}, timeout=10)
        second_response_json = second_response.json()

        if second_response.status_code == 200:
            pipeline_status = second_response_json.get('data', {}).get('executionDetails', {}).get('pipelineExecutionSummary', {}).get('status', '')
            print("Pipeline execution status =", pipeline_status)
        else:
            print(f"Error {second_response.status_code}: {second_response.text}")

        # Check pipeline execution status
        pipeline_status = second_response_json.get('data', {}).get('executionDetails', {}).get('pipelineExecutionSummary', {}).get('status', '')
        if pipeline_status == 'Success':
            print("Deployment succeeded at", time.strftime('%Y-%m-%d %H:%M:%S'))
            break
        elif time.time() - start_time > timeout_seconds:
            print("Timeout exceeded. Pipeline execution did not succeed within the specified time.")
            break

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    # Wait for the specified interval before checking again
    time.sleep(check_interval_seconds)
