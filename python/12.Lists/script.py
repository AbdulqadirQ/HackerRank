def execute_commands(the_list, command, *args):
    arg_list = ','.join(args)
    exec('the_list.{}({})'.format(command, arg_list))

n = int(input())
the_list = []
for _ in range(n):
    command, *args = input().split()
    if command == 'print':
        print(the_list)
    else:
        execute_commands(the_list, command, *args)