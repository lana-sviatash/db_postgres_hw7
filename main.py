import argparse
from crud import create_record, update_record, list_records, remove_record, MODELS

parser = argparse.ArgumentParser(description="DB CRUD")
parser.add_argument(
    "--action",
    "-a",
    choices=["create", "list", "update", "remove"],
    required=True,
    help="Action to perform",
)
parser.add_argument(
    "--model",
    "-m",
    choices=list(MODELS.keys() + [m.capitalize() for m in MODELS.keys()]),
    required=True,
    help="Model to perform action on",
)

parser.add_argument("--id", type=int, help="ID of the record")
parser.add_argument("--name", "-n", help="Name of the record")

args = parser.parse_args()


def main():
    if not args.action or not args.model:
        print("Please provide both action and model arguments.")
        parser.print_help()
        return
    
    if args.action == "create":
        create_record(args.model, name=args.name)
    elif args.action == "list":
        list_records(args.model)
    elif args.action == "update":
        update_record(args.model, args.id, name=args.name)
    elif args.action == "remove":
        remove_record(args.model, args.id)


if __name__ == "__main__":
    main()
