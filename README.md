# Project Four - Caleidoscope - Backend

### [Frontend Repo](https://github.com/xlnl/p4-caleidoscope-frontend)
### [Deployed API](https://caleidscope-api.herokuapp.com)

## Backend Tech Used
* Notion & Github - for project management 
* Figma & LucidCharts - for wireframes & ORM planning
* Flask - for Python micro web framework
* PostgreSQL & Peewee - for migrations & ORM

## General Approach
This was a labor of love! I wanted to create a useful personal management app that drew inspiration from Notion block functionality and (someday) from Google Calendar OAuth to store events into my Google account. 

Until then, it will serve as an entry point for further development and enhancements. 

## Installation Instructions
To install the backend dependencies, please cd into the backend app and do the following:
> virtualenv .env -p python3
>
> source .env/bin/activate
>
> pip3 install -r requirements.txt
>

Run the app like normal:
> python3 app.py


## Models 
### Click [here](https://lucid.app/lucidchart/57f21b8d-268e-4ed4-9422-76779256ba95/edit?shared=true) for the ERD.

## RESTful Routes
| Name                         | Action (CRUD) | Description                                                                                                                                | Notes    | 
|------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|----------| 
| /                            | GET           | Main page with description of the app - landing page                                                                                       | MVP      | 
| /api/v1/user/login                 | POST           | Log-in form                                                                                                                                | MVP      | 
| /api/v1/user/register                | POST          | Post sign-in form to db                                                                                                                    | MVP      | 
| /home                | GET           | renders data for calendar, notes, weather, and horoscope components on one dashboard                                                                                           | MVP      | 
| /api/v1/note/                 | GET          | renders data about existing notes                                                                | MVP      | 
| /api/v1/note/new                       | POST           | post notes data to db                                                                        | MVP      | 
| /api/v1/note/:noteId                     | GET           | renders a single note                                                                                        | MVP      | 
| /api/v1/note/:noteId       | DELETE          | deletes a specific note                                                                                                                   | Stretch      | 
| /api/v1/event/                 | GET          | renders data about existing events                                                                | Stretch      | 
| /api/v1/event/new                       | POST           | post event data to db                                                                        | Stretch      | 
| /api/v1/event/:noteId                     | GET           | renders a single event                                                                                        | Stretch      | 
| /api/v1/event/:noteId       | DELETE          | deletes a specific event                                                                                                                   | Stretch      |

## Major Hurdles & Unsolved Problems 
Handling Flask authentication and troubleshooting with cookies and sessions became a steep learning curve that took a lot more time than expected. I'm still working on fulling utilizing the schedule component on the frontend to have it connect to my events routes. 