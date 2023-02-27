#!/usr/bin/python3
import os, argparse, json

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--list', action='store_true', help='create user if not found')
  parser.add_argument('--host', dest='host', help='port to connect to')

  args = parser.parse_args()


  if args.list:
    x = {
      "deploy": {
        "hosts": [os.getenv('SERVER')],
        "vars": {"deploy_version": os.getenv('VERSION')}
      }
    }
    print(json.dumps(x))
  

  if args.host:
    y = {
      "deploy_version": os.getenv('VERSION')
    }
    print(json.dumps(y))
