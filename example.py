import sys
import json
import time
import jiralib as jira

def ts():
  '''Return current timestamp in milliseconds (as an int).'''
  return int(round(time.time() * 1000))

def main():
  if len(sys.argv) != 2:
    raise Exception('Pass assignee as arg; example: python example.py user1234')
  with open('enclave/enclave.json', 'r') as f: cfg = json.load(f)
  jira_spec = cfg['jira-spec']
  project_key = 'SANDBOX'
  issue_kind = 'Enrollment'
  summary = 'This is a test ticket -- ' + str(ts())
  description = 'A test ticket.'
  assignee = sys.argv[1]
  print 'Will create ticket and assign to ' + assignee
  print jira.create_issue(jira_spec
                         ,project_key
                         ,issue_kind
                         ,summary
                         ,description 
                         ,assignee)
  print 'Done'

if __name__ == '__main__':
  main()

