#!/usr/bin/env python


import argparse
import pandas as pd
import json
from pathlib import Path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--gitter_users', required=True, help="Path to JSON file with Gitter users")
    parser.add_argument('--out', required=True, help="Path to output CSV file")
    args = parser.parse_args()

    # load json file
    if not Path(args.gitter_users).is_file():
        raise ValueError("%s does not exist" % args.gitter_users)
    with open(args.gitter_users, 'r') as gitter_users_f:
        gitter_users = [json.loads(line) for line in gitter_users_f]
    
    # convert dict into a data frame
    gitter_users_df = (pd.DataFrame(gitter_users)
        .drop(['id', 'url', 'avatarUrl', 'avatarUrlMedium', 'avatarUrlSmall', 'v', 'gv'], axis=1)
        .query('username != "tnabtaf"')
        .query('username != "bebatut"')
        .query('username != "annefou"')
        .query('username != "beatrizserrano"')
        .query('username != "assuntad23"')
        .rename(columns= {
            'displayName': 'Name',
            'username': 'Gitter'
        })
        .reindex(columns=['Name','Gitter']))
    print("Gitter users")
    print(gitter_users_df.head())
    print(len(gitter_users_df))

    # get google sheet
    url = "https://docs.google.com/spreadsheets/d/1so0j5WaPnKoRXiyLo-2mByX32XRJ1oIDXUbV6lQKw2Q/export?format=csv&gid=0"
    participants_df = (pd.read_csv(url)
        .fillna(''))
    print("Google sheet")
    print(participants_df.head())
    print(len(participants_df))

    # merge both df and save it to a file
    participants_df = (participants_df.merge(gitter_users_df, how="outer")
        .sort_values('Gitter')
        .drop_duplicates(subset='Gitter'))
    print("All participants")
    print(participants_df.head())
    print(len(participants_df))
    participants_df.to_csv(args.out, index=False)
