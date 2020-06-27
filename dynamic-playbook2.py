import argparse
import sys
import os
from jinja2 import Environment, FileSystemLoader
parser = argparse.ArgumentParser(
    description='Parser to install programs on dockers')
parser.add_argument('--tasks', dest="tasks", default=None,
                    type=str, help="tasks for remote dockers", required=False)
args = parser.parse_args()
tasks = args.tasks

def main(tasks):
    listOfTasks = tasks.split(",")
    for i in listOfTasks:
        print(i)
    tempFile = 'playbook.yml.j2'
    file_loader = FileSystemLoader(".")
    env = Environment(loader=file_loader)
    test = True
    template = env.get_template(tempFile)
    output = template.render(roles=listOfTasks)
    with open("playbook.yml", "w") as f:
        f.write(output)
main(tasks)