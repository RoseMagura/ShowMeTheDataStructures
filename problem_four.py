class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return recursion(user, group)

def recursion(user, group):
    print('checking for ', str(user), 'in', str(group.get_name()))
    users = group.get_users()
    if user in users:
        return True
    else:
        groups = group.get_groups()
        for g in groups:
            bool = recursion(user, g)
            if bool:
                return bool
        return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group('sub_child_user', parent)) # True
print(is_user_in_group('sub_child_user', child)) # True
print(is_user_in_group('sub_child_user', sub_child)) # True
print(is_user_in_group('sub_child_usr', parent)) # False
print(is_user_in_group('sub_child_user', Group('random_group'))) # False

