import datetime
from cal_setup import get_calendar_service

def get_list_event(eventnumber = 5):
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=eventnumber, singleEvents=True,
                                        orderBy='startTime').execute()
    print(events_result)
    events = events_result.get('items', [])
    print(events)
    dictlist = []
    if not events:
        print('No upcoming events found.')
    print(f'Getting List of {len(events)} events')
    tmfmt = '%d %B, %H:%M %p' 
    for event in events:
        
        end = event['end'].get('dateTime', event['end'].get('date'))
        #end_time = datetime.strftime(dtparse(end), format=tmfmt)
        start = event['start'].get('dateTime', event['start'].get('date'))
        #start_time = datetime.strftime(dtparse(start), format=tmfmt)
        event_title_summary = event['summary']
        html_link = event['htmlLink']
        dictlist.append({'datetime': start,'eventtitle' : event_title_summary,'html_link' : html_link})
    return(dictlist)

