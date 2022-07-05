import boto3

client = boto3.client('cloudformation')

def get_current_stacks():
    stacks = client.list_stacks().get("StackSummaries")
    existing_stacks = []
    for stack in stacks:
        if stack.get("StackStatus") not in ("DELETE_COMPLETE"):
            existing_stacks.append(stack.get("StackName"))
        print(stack)
    return existing_stacks


####################OPTIONAL going throught eh iterator function################
s_names = (get_current_stacks())
print ('Current stacks: ', s_names)
stacks =iter(s_names)

while True:
    try:
        stack = next (stacks)
        print(stack)
    except StopIteration:
        break
# print(stack)

def get_stack_resources():
    resources = client.list_stack_resources(StackName= stack).get('StackResourceSummaries')
    stack_resources = []
    for resource in resources:
        if resource.get("ResourceStatus") not in ("DELETE_COMPLETE"):
            stack_resources.append(resource.get("PhysicalResourceId"))
        print (resource)
    return stack_resources
s_resources = get_stack_resources() 
print ('Here are the active resources for the stack :',s_resources)

def get_resource_tags():
    tags = client.describe_stacks(StackName= stack).get('Stacks')
    stack_tags = []
    for tag in tags:
      tag.get("Tags")
    return stack_tags
s_tags = get_resource_tags()
print ('Here are the tags:', s_tags)

####################OPTIONAL going through the iterator function################

def handler(event, context):
    s_names = (get_current_stacks())
    print ('Current stacks: ', s_names)
    s_resources = get_stack_resources()
    print ('Here are the active resources for the stack :',s_resources)
    s_tags = get_resource_tags()
    print ('Here are the tags:', s_tags)
    return s_names, s_resources, s_tags

