'''Let us say we have 3 events - create user,update user,delete user.
And three types of notifications - email, log, sms'''

from collections import defaultdict
event_notifications = defaultdict(list)

def add_events(eventname,fn):
    event_notifications[eventname].append(fn)

def push_notification(eventname,username):
    for fn in event_notifications[eventname]:
        fn(username)

## The three email functions
def email_user_creation(username):
    print(f'Emailed - Created User - {username}')

def email_user_update(username):
    print(f'Emailed - Updated User - {username}')

def email_user_delete(username):
    print(f'Emailed - Deleted User - {username}')

## The three log functions
def log_user_creation(username):
    print(f'Logged - Created User - {username}')

def log_user_update(username):
    print(f'Logged - Updated User - {username}')

def log_user_delete(username):
    print(f'Logged - Deleted User - {username}')

## The three sms functions
def sms_user_creation(username):
    print(f'SMS  - Created User - {username}')

def sms_user_update(username):
    print(f'SMS - Updated User - {username}')

def sms_user_delete(username):
    print(f'SMS - Deleted User - {username}')


def create_user(username:str):
    print(f'User {username} created')
    push_notification('create_user',username)

def update_user(username:str):
    print(f'User {username} updated')
    push_notification('update_user',username)

def delete_user(username:str):
    print(f'User {username} deleted')
    push_notification('delete_user',username)


if __name__=='__main__':
    
    add_events('create_user',email_user_creation)
    add_events('create_user',log_user_creation)
    add_events('create_user',sms_user_creation)

    add_events('update_user',email_user_update)
    add_events('update_user',log_user_update)
    add_events('update_user',sms_user_update)

    add_events('delete_user',email_user_delete)
    add_events('delete_user',log_user_delete)
    add_events('delete_user',sms_user_delete)

    print(event_notifications)
    create_user('Satyajit')
    update_user('Satyajit')
    delete_user('Satyajit')


    



