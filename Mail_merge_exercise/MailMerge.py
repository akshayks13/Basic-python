#To send mail to the people according to their roles

import csv


with open('/Users/akshayks/Desktop/VS code/Mail_merge_exercise/contacts.csv','r') as contacts:
    csvreader=csv.reader(contacts)
    f=next(csvreader)  #To remove the starting column name for accessing only names
    for row in csvreader:
        if row[-1]=='Event Reminder':
            with open('/Users/akshayks/Desktop/VS code/Mail_merge_exercise/templates/event_reminder.txt','r') as mail1:
                data=mail1.read()
                data=data.replace('{{event_name}}',row[-2])
                data=data.replace('{{event_date}}','10-10-23')
                data=data.replace('{{recipient_name}}',row[0])
                data=data.replace('{{event_time}}','4:00')
                data=data.replace('{{event_location}}','Tokyo')
                data=data.replace('{{organizer_name}}','Virat')
                data=data.replace('{{organizer_contact_info}}','BLAh BLAH')
                print(data)
                mail1.close()
        
        elif row[-1]=='Customer Service Follow-Up':
            with open('/Users/akshayks/Desktop/VS code/Mail_merge_exercise/templates/customer_service_followup.txt','r') as mail2:
                data=mail2.read()
                data=data.replace('{{company_name}}',"Google")
                data=data.replace('{{customer_name}}',row[0])
                data=data.replace('{{product_or_service_used}}',"Google Cloud")
                data=data.replace('{{customer_service_rep_name}}',"Larry Page")
                data=data.replace('{{customer_service_contact_info}}',"123-45-67")
                print(data)
                mail2.close()

        elif row[-1]=='Newsletter Subscription Confirmation':
            with open('/Users/akshayks/Desktop/VS code/Mail_merge_exercise/templates/newsletter_subscription_confirmation.txt','r') as mail3:
                data=mail3.read()
                data=data.replace('{{newsletter_name}}',"Times of India")
                data=data.replace('{{subscriber_name}}',row[0])
                data=data.replace('{{newsletter_topics}}',"Sports")
                data=data.replace('{{editor_name}}',"Alt Watman")
                data=data.replace('{{newsletter_contact_info}}',"123-45-67")
                print(data)
                mail3.close()
        
        elif row[-1]=='Business Meeting Invitation':
            with open('/Users/akshayks/Desktop/VS code/Mail_merge_exercise/templates/business_meeting_invitation.txt','r') as mail4:
                data=mail4.read()
                data=data.replace('{{meeting_date}}',"13-05-2023")
                data=data.replace('{{recipient_name}}',row[0])
                data=data.replace('{{your_company_name}}',"Google")
                data=data.replace('{{meeting_location}}',"San Fransisco")
                data=data.replace('{{meeting_agenda}}',"row[-2]")
                data=data.replace('{{your_position}}',"CEO")
                data=data.replace('{{your_name}}',"Akshay")
                print(data)
                mail4.close()

        elif row[-1]=='Job Interview Confirmation':
            with open('/Users/akshayks/Desktop/VS code/Mail_merge_exercise/templates/job_interview_confirmation.txt','r') as mail5:
                data=mail5.read()
                data=data.replace('{{company_name}}',"Google")
                data=data.replace('{{appliacant_name}}',row[0])
                data=data.replace('{{job_title}}',row[1])
                data=data.replace('{{interview_date}}',"13-05-2023")
                data=data.replace('{{interview_time}}',"4:00 pm")
                data=data.replace('{{office_address}}',"San Fransisco")
                data=data.replace('{{hr_representative_name}}',"Sam")
                data=data.replace('{{hr_representative_position}}',"CEO")
            
        else:
             break

    







    
