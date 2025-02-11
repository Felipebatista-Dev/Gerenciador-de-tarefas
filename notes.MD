# later I'll decide whether to send these notes to the README

# task tracker
- manage my task list
- show a task as in progress or completed
- list all tasks
- list all completed tasks
- list ongoing tasks
- list unstarted tasks
- my task list should be in a json file

# classes
- add
- update
- delete
- show status
- list

# features
- add, delete or update tasks
- show the status of a given task
- list completed, in progress, or unstarted tasks
- list all tasks

{"washingdishes": "completed", "sweepinghouse": "inprogress", "studying": "inprogress", "payingbills": "notstarted", "shopping": "completed", "gym": "inprogress", "shaving": "notstarted", "cleaningroom": "completed", "throwingtrashout": "inprogress", "cleaningcomputer": "notstarted", "trabalho": "not started"}

pyinstaller --onefile --add-data "tasklist.json;." main.py