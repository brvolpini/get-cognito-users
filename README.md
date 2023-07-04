# get-cognito-users
Export user records from cognito to csv

## Installation

Run:

```
source venv/bin/activate
```

```
pip3 install -r requirements.txt
```

```
python3 get-cognito-users.py -f exported_users.csv --user-pool-id <PoolIdExample> -attr <name email, etc...>
```

You can use any attribute that exists in your cognito user pool (custom or prefefined)


### Script Arguments

- `-pool` or `--user-pool-id` [__Required__]
- `-attr` or `--export-attributes` [__Required__]
- `-f` or `--file-name` [__Optional__]

