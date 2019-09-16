import json
import requests

__all__ = ['create_issue'
          ,'do_transition'
          ,'set_assignee'
          ,'add_watcher'
          ]

def create_issue(jira_spec
                ,project_key
                ,issue_kind
                ,summary
                ,description
                ,assignee=None
                ,additional_fields=None):
  '''Create a brand new Jira issue and return a result.
  Arguments:
    - jira_spec: see readme.
    - project_key: Jira project as a string.
    - issue_kind: string (often is custom to the proj or Jira installation)
    - summary: The issue's title as a string.
    - description: text to go into the issue's Description field;
        if None, the 'description' key-value pair won't be included.
    - assignee: username the issue will be assigned to. If None, skips.
    - additional_fields: an optional map containing additional key-value 
                         pairs you want to include in the JSON payload 
                         fields substructure. If None, skips.
  Returns a map with two keys: HTTP status (int) and payload (string).
  HTTP status of 201 means success.  
  '''
  post_data = {"fields": {"project": {"key": project_key}
                         ,"issuetype": {"name": issue_kind}
                         ,"summary": summary
                         #,"description": description}
                         } }
  if description:
    post_data['fields']['description'] = description
  if assignee:
    post_data['fields']['assignee'] = {"name": assignee}
  if additional_fields:
    # Merge additional map into post_data's 'fields' map.
    post_data['fields'].update(additional_fields.copy())
  result = requests.post(
              jira_spec['issue-url']
             ,auth=(jira_spec['user'], jira_spec['pass'])
             ,json=post_data)
  return {'status': result.status_code
         ,'payload': result.text}

def do_transition(jira_spec, issue_id, transition_id):
  '''Change the status of an issue (in Jira this action is
  called a 'transition').
  Arguments:
    - jira_spec: see readme.
    - issue_id: the ticket ID (e.g., "SANDBOX-1234")
    - transition_id: the id (as a string) of the transition to carry out. 
  You can view all available statuses via: 
    GET /rest/api/2/issue/{issueIdOrKey}/transitions
  Returns a map with two keys: HTTP status (int) and payload (string).
  HTTP status of 204 means success.  
  '''
  post_data = {'transition': {'id': transition_id}}
  url = jira_spec['issue-url'] + issue_id + '/transitions'
  result = requests.post(
               url
               ,auth=(jira_spec['user'], jira_spec['pass'])
               ,json=post_data)
  return {'status': result.status_code
         ,'payload': result.text}

def set_assignee(jira_spec, issue_id, assignee):
  '''Assign ticket to a particular user.
  Arguments:
    - jira_spec: see readme.
    - issue_id: the ticket ID (e.g., "SANDBOX-1234")
    - assignee: username of new assignne
  Returns a map with two keys: HTTP status (int) and payload (string).
  HTTP status of 204 means success.  
  Note: underlying REST endpoint uses PUT for this.
  '''
  put_data = {'name': assignee}
  url = jira_spec['issue-url'] + issue_id + '/assignee'
  result = requests.put(
               url
               ,auth=(jira_spec['user'], jira_spec['pass'])
               ,json=put_data)
  return {'status': result.status_code
         ,'payload': result.text}

def add_watcher(jira_spec, issue_id, username):
  '''
  Add a watcher to a ticket.
  Args:
    - jira_spec: see README
    - issue_id: the ticket ID (e.g., "SANDBOX-1234")
  As for the underlying API call:
  https://docs.atlassian.com/software/jira/docs/api/REST/6.4.1/#d2e5428
  /rest/api/2/issue/{issueIdOrKey}/watchers
  API returns 204 for success; otherwise, 400/401/404
  '''
  data = username
  url = jira_spec['issue-url'] + issue_id + '/watchers'
  result = requests.post(
               url
               ,auth=(jira_spec['user'], jira_spec['pass'])
               ,json=data)
  return {'status': result.status_code
         ,'payload': result.text}

