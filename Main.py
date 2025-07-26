from Functions import *
import argparse

def main():
    # define the command line interface
    parser = argparse.ArgumentParser(description='TaskLite - A simple task management CLI tool')

    sub_parser = parser.add_subparsers(dest='command')

    add_parser = sub_parser.add_parser('add', help='Add a new task')
    add_parser.add_argument('taskName', type=str, help='Name of the task to add')

    list_parser = sub_parser.add_parser('list', help='List tasks')
    list_parser.add_argument('--all', action='store_true', help='List all tasks')
    list_parser.add_argument('--status', type=str, choices=['todo', 'in-progress', 'done'], help='List tasks by status')

    modify_parser = sub_parser.add_parser('modify', help='Modify the description of an existing task')
    modify_parser.add_argument('id', type=int, help='ID of the task to modify')
    modify_parser.add_argument('description', type=str, help='New description for the task')

    update_parser = sub_parser.add_parser('update', help='Update the status of an existing task')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('status', type=str, choices=['todo', 'in-progress', 'done'], help='New status for the task')

    delete_parser = sub_parser.add_parser('delete', help='Delete an existing task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')

    args = parser.parse_args()

    # execute the command based on the parsed arguments
    try:
        if args.command == 'add':
            add_task(args.taskName)
        elif args.command == 'list':
            if args.all:
                list_all()
            elif args.status:
                list_by_status(args.status) 
        elif args.command == 'modify':
            modify_task(args.id, args.description) 
        elif args.command == 'update':
            update_status(args.id, args.status) #TODO: not working
        elif args.command == 'delete':
            delete_task(args.id)
        else:
            print('Invalid command. Use --help for list of commands.')
            parser.print_help()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()