import boto3
import csv
import argparse

parser = argparse.ArgumentParser(description='Filtered list of Cognito users into CSV')
parser.add_argument('-attr', '--attributes', type=str, nargs='+', metavar='', help='Required attributes', required=True)
parser.add_argument('-pool', '--user_pool_id', type=str, help='User pool ID', required=True)
parser.add_argument('-f', '--file-name', type=str, help='CSV file name', default='cognito_users.csv')
parser.add_argument('--is-admin', action='store_true', help='Include only users with custom:role=admin')
args = parser.parse_args()

REQUIRED_ATTRIBUTES = args.attributes
USER_POOL_ID = args.user_pool_id
CSV_FILE_NAME = args.file_name
FILTER_ADMIN = args.is_admin

try:
    client = boto3.client('cognito-idp')

    paginator = client.get_paginator('list_users')
    response_iterator = paginator.paginate(UserPoolId=USER_POOL_ID)

    with open(CSV_FILE_NAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=REQUIRED_ATTRIBUTES)
        writer.writeheader()

        for page in response_iterator:
            for user in page['Users']:
                # Create dict of user attributes
                attr_map = {attr['Name']: attr['Value'] for attr in user.get('Attributes', [])}

                # Apply optional admin filter
                if FILTER_ADMIN and attr_map.get('custom:role', '').lower() != 'admin':
                    continue

                # Prepare row
                row = {attr: '' for attr in REQUIRED_ATTRIBUTES}

                # Fill from top-level user keys
                for attr in REQUIRED_ATTRIBUTES:
                    if attr in user:
                        row[attr] = str(user[attr])

                # Fill from attributes map
                for attr in REQUIRED_ATTRIBUTES:
                    if attr in attr_map:
                        row[attr] = attr_map[attr]

                writer.writerow(row)

except Exception as err:
    print(f'ERROR: {err}')