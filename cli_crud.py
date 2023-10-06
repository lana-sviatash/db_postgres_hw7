import argparse
from crud import create_record, update_record, get_all_records, remove_record

parser = argparse.ArgumentParser(description='DB CRUD')

# Adding action and model arguments
parser.add_argument('--action', '-a', help='Command: create, update, list, remove')
parser.add_argument('--model', '-m')
parser.add_argument('--id', type=int, help='ID of the record')
parser.add_argument('--name', '-n', help='Name for the record')

arguments = parser.parse_args()

action = arguments.action
model = arguments.model
_id = arguments.id
name = arguments.name


def main():
    if not action or not model:
        print("Please provide both action and model arguments.")
        parser.print_help()
        return
    
    match action:
        case 'create':
            create_record(model, name)
        case 'update':
            update_record(model, _id, name)
        case 'list':
            recs = get_all_records(model)
            for rec in recs:
                print(rec)
        case 'remove':
            remove_record(model, _id)
        case _:
            print("Unknown action")



if __name__ == "__main__":
    main()
