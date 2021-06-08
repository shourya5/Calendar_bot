
from cal_setup import get_calendar_service

def get_list_event(eventnumber,tmin,tmax):
    service = get_calendar_service()
    # Call the Calendar API


    events_result = service.events().list(calendarId='primary',
                                        timeMin=tmin,
                                        timeMax=tmax,
                                        maxResults=eventnumber,
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    print(events)
    dictlist = []
    if not events:
        print('No upcoming events found.')
    print(f'Getting List of {len(events)} events')
    for event in events:

        end = event['end'].get('dateTime', event['end'].get('date'))
        #end_time = datetime.strftime(dtparse(end), format=tmfmt)
        start = event['start'].get('dateTime', event['start'].get('date'))
        #start_time = datetime.strftime(dtparse(start), format=tmfmt)
        event_title_summary = event['summary']
        event_description = event['description']
        html_link = event['htmlLink']
        dictlist.append({'start_datetime': start,
                        'end_datetime':end,
                        'eventtitle' : event_title_summary,
                        'html_link' : html_link,
                        'event_desc': event_description})
    return(dictlist)

