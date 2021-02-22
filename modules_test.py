import os
import json

current_working_dir = os.getcwd()
data_path = f'{current_working_dir}/data'

# the structure we need to return for part A
users_by_module = {
    'auth_module': {},
    'content_module': {}
}

# read and process the files in data folder
for user_file in os.listdir(data_path):
    if user_file.endswith('.json'):
        file_path = f'{data_path}/{user_file}'
        file_content = json.loads(
            open(file_path, 'r', encoding='utf-8').read())

        user = file_content.get('name')

        for module_type, provider in file_content.get('provider').items():
            if module_type == 'auth_module':
                users_by_module['auth_module'].setdefault(
                    provider, []).append(user)

            elif module_type == 'content_module':
                users_by_module['content_module'].setdefault(
                    provider, []).append(user)


# writing the users grouped by modules to a file
results_file = f'{current_working_dir}/users_by_module.json'
if not os.path.exists(results_file):
    os.mknod(results_file)
with open(results_file, 'w') as outfile:
    json.dump(users_by_module, outfile)


# the list of users we return for part B
min_users_modules = []

# now we take advantage of the users_by_module data and iterate over it to get the minimum number of users that use all modules
for provider, users in users_by_module['auth_module'].items():
    # the user we'll use to test the module
    module_user = users[0]
    min_users_modules.append(module_user)
    # now we delete the module_user's content_module cause with it (the user) we're already covering that module
    for provider, users in users_by_module['content_module'].items():
        if module_user in users:
            del users_by_module['content_module'][provider]
            break

# once we've covered all auth_modules, we have to check if there's any content_module still there, and in that case we need that user
for provider, users in users_by_module['content_module'].items():
    min_users_modules.append(users[0])


# writing the list of module users to a file
results_file = f'{current_working_dir}/minimum_users_for_testing_modules.txt'
if not os.path.exists(results_file):
    os.mknod(results_file)
with open(results_file, 'w') as outfile:
    outfile.writelines(str(min_users_modules))
