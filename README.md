# Calendar_bot
Calendar bot is a dsicord bot that syncs with Google Calendar.It can be used as a personal companion for to Google Calendar on discord or as a event management service that syncs with Google Calendar

## Installation
Ensure the python package manager [pip](https://pip.pypa.io/en/stable/) is updated to the latest stable build

Run the following commands to install the required dependencies

``` bash
pip install --upgrade google-api-python-client google-auth-httplib2  google-auth-oauthlib
pip install discord
pip install python-dateutil
```
## Usage
### Setup
Navigate to the directory where calendar_bot is located
create a .env file and enter your discord bot token in this format:
```bash
DISCORD_TOKEN = {your bot token here}
```
This is the environment variable that main_bot.py acceses the bot token from
Then run this command:
```bash
python3 main_bot.py
```
The CLI will display an authentication link.Visit this link,and login with your Google Account.grant all permissions and then copy the authentication code and paste it into the CLI like this:
```bash
Enter authentication code:{Authentication Code Here}
```
Setup is complete.You will not need to login the next time you run this bot.

### Bot commands
#### $eventstoday
Use the command like this:
```bash
$eventstoday {number of events displayed}
       OR
$eventstoday
```
Displays all upcoming events for the current date and time.
Has an optional {number of events displayed} argument.The default number of events displayed is 5.
#### $eventstommorow
Similiar to $eventstoday

Use the command like this:
```bash
$eventstommorow {number of events displayed}
       OR
$eventstommorow
```
Displays all upcoming events for the next day
#### $eventsyesterday
Similiar to $eventstoday

Use the command like this:
```bash
$eventsyesterday {number of events displayed}
       OR
$eventsyesterday
```
Displays all past events for the previous day
## Contributing
Pull requests are accepted.Please open an issue if you find a bug or have an idea for a feature.
## License
[MIT](https://choosealicense.com/licenses/mit/)






