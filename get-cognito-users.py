import boto3
import csv
import argparse

CSV_FILE_NAME = 'cognito_users.csv'

parser = argparse.ArgumentParser(description='filtered list of cognito users into csv')
parser.add_argument('-attr', '--attributes', type=str, nargs='+', metavar='', help='required attributes', required=True)
parser.add_argument('-pool', '--user_pool_id', type=str, help='User pool ID', required=True)
parser.add_argument('-f', '--file-name', type=str, help="CSV File name")
args = parser.parse_args()

if args.attributes:
     REQUIRED_ATTRIBUTES = list(args.attributes)

if args.user_pool_id:
    USER_POOL_ID = args.user_pool_id

if args.file_name:
    CSV_FILE_NAME = args.file_name

try:
    client = boto3.client('cognito-idp')
    CSV_NEW_LINE = {REQUIRED_ATTRIBUTES[i]: '' for i, v in enumerate(REQUIRED_ATTRIBUTES)}

    paginator = client.get_paginator('list_users')
    response_iterator = paginator.paginate(
            UserPoolId=USER_POOL_ID
            )


    with open(CSV_FILE_NAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=CSV_NEW_LINE)
        writer.writeheader()
        csv_lines = []    
    
        for page in response_iterator:
            for user in page['Users']:
                """ Fetch Required Attributes Provided """
                for requ_attr in REQUIRED_ATTRIBUTES:
                    CSV_NEW_LINE[requ_attr] = ''
                    if requ_attr in user.keys():
                        CSV_NEW_LINE[requ_attr] = str(user[requ_attr])
                        continue
                    for usr_attr in user['Attributes']:
                        if usr_attr['Name'] == requ_attr:
                            CSV_NEW_LINE[requ_attr] = str(usr_attr['Value'])

                csv_lines.append(",".join(CSV_NEW_LINE.values()) + '\n')

            file.writelines(csv_lines)
except Exception as err:
    print(f'ERROR: {err}')
