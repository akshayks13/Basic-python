def add_event_details(**kwargs):
    #@start-editable@

    event_details = {
       'name': 'Unnamed Event',
        'type': 'General',
        'date': 'N/A',
        'location': 'N/A'
    #@end-editable@
    }

    for key, default_value in event_details.items():
        kwargs[key] = kwargs.get(key) or default_value

    return event_details

def add_guests(*args):
    guests = []
    #@start-editable@

    for guest_info in args:
        name, gender, contact = guest_info.split(',')
    #@end-editable@
        guests.append({"name": name, "gender": gender, "contact": contact})
    return guests

def allocate_resources(rates, **kwargs):
    resources = {}
    total_cost = 0
    #@start-editable@

    for item, quantity in kwargs.items():
        cost = rates.get(item) * int(quantity)
    #@end-editable@
        total_cost += cost
        resources[item] = quantity
    return resources, total_cost

def has_special_requests(*args):
    #@start-editable@
    if args[0]=='None':
        answer = False
    #@end-editable@
    else:
        answer = True
    return answer

'''def create_event_summary(event_dict):
    summary = [
        f"Event: {event_dict.get('details', {}).get('event_type', 'General')}",
        #@start-editable@
        
        f"Male Guests: {______________________________}",
        f"Female Guests: {______________________________}",
        f"Total Resource Expense: ${__________________________}",
        f"Special Requests: {______________________________}"
        #@end-editable@
    ]
    return "\n".join(summary)'''

def create_event_summary(event_dict):
    m=0
    f=0
    Event=event_dict.get('details', {}).get('event_type', 'General')
    Specialreq=event_dict.get('has_special_requests')
    for guest in event_dict.get('guests'): 
        if guest['gender'] == ' Male':
            m+=1
    # for guest in event_dict.get('guests'):
    #     if guest['gender'].lower() == 'female':
        else:
            f+=1
    
    Totalexp=event_dict.get('resource_info').get('total_cost')
    print("Event:",Event)
    print("Male Guests:",m)
    print("Female Guests:",f)
    print("Special Requests:",Specialreq)

    
    


# Driver code
if __name__ == "__main__":
    event_description = {}

    # Example input:
    # Tech Conference, Conference, 2023-09-15, Silicon Valley
    # John Doe, Male, john@example.com; Jane Smith, Female, jane@example.com
    # Chairs, 150; Projectors, 2; Microphones, 5
    # Vegan Menu, Wheelchair Access
    
    #@start-editable@

    event_name, event_type, event_date, event_location = input().split(',')
    #event_name, event_type, event_date, event_location = map(str,input().split())

    #@end-editable@
    event_description['details'] = add_event_details(name=event_name, event_type=event_type, date=event_date, location=event_location)

    #@start-editable@

    guests = input().split(';')
    #end-editable@
    event_description['guests'] = add_guests(*guests)

    resources_input = input().split("; ")
    resources_input = [resource.split(", ") for resource in resources_input]
    #@start-editable@
  
    resources_input_dict = {item: quantity for item, quantity in resources_input}
    #@end-editable@
    resource_rates = {"Chairs": 5, "Tables": 10, "Projectors": 100, "Microphones": 15}    
    #@start-editable@

    event_description['resource_info'], total_cost = allocate_resources(resource_rates, **resources_input_dict)
    #@end-editable@
    event_description['resource_info']["total_cost"] = total_cost
    
    special_requests = input().split(", ")
    event_description['special_requests'] = special_requests
    #@start-editable@

    event_description['has_special_requests'] = has_special_requests(*special_requests)
    #@end-editable@
    
    # print(event_description)
    create_event_summary(event_description)

