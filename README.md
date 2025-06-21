# get-cognito-users
Export user records from cognito to CSV

## Installation

Create VENV
```
# Windows
  python -m virtualenv env
  .\env\Scripts\activate
```
```
# Mac
  virtualenv venv
  source venv/bin/activate
```

Install required libraries
```
pip3 install -r requirements.txt
```

Run script
```
python3 get-cognito-users.py -f exported_users.csv --user-pool-id <PoolIdExample> -attr <name email, etc...>
```

Filter only admin users
```
pass to the script the argument --is-admin:
python3 get-cognito-users.py -f exported_users.csv --user-pool-id <PoolIdExample> -attr <name email, etc...> --is-admin
```

**You can use any attribute that exists in your cognito user pool (custom or predefined)** 


### Script Arguments

- `-pool` or `--user-pool-id` [__Required__]
- `-attr` or `--export-attributes` [__Required__]
- `-f` or `--file-name` [__Optional__]
- `--is-admin` [__Optional__]


