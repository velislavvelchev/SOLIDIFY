# 🧠 SOLIDIFY
### SOLIDIFY is a Django application inspired by neuroscience that  helps users build and maintain their habit routines, by grouping them into categories and events that can be scheduled into a calendar.

Access the application [here](https://solidify-e4esdsgbdabdadhh.italynorth-01.azurewebsites.net/)

## 🚀 Features


### 🗝️ Authentication

- **Register**: Users can sign up by entering their email, username, password, and password confirmation. Error messages are shown if any input is invalid.
- **Login**: Users can log in to their account after it has been created.
- **Logout**: Users can log out of their accounts after they have been logged in.

#### Login Page

- Allows the user to log in and displays relevant error message.

<img width="701" height="349" alt="image" src="https://github.com/user-attachments/assets/e8de35d7-2015-4836-9d87-dac47c3247d4" />



#### Register

- Provides a registration form to the user and displays relevant error messages.

<img width="701" height="376" alt="image" src="https://github.com/user-attachments/assets/b2959b00-c1ba-4930-a937-9b81f6b1fa00" />




### 🎩 Header

**User Unauthenticated**:
	- **Log In**: Displays a login button if the user is not logged in.
	- **Sign Up**: Displays a sign up button if the user is not logged in.


**User Authenticated**:
	Dropdowns ⤵️:
		- **Account**:  
			- Profile Details
			- Edit Profile
			- Logout
		- **Categories**:
			- All Categories
			- Create Category
		- **Habits**: 
			- All Habits
			- Create Habit
		- **Routines**:
			- All Routines
			- Create Routine
	Single-click navigation pages ⛓️:
		- **Schedule Routine**
		- **Calendar**


- UI if the user is not logged in:
 <img width="1037" height="64" alt="image" src="https://github.com/user-attachments/assets/28a4c4bb-9fe6-40de-8d48-530d36c2e313" />

- UI if the user is logged in:

<img width="815" height="64" alt="image" src="https://github.com/user-attachments/assets/b809a56b-38aa-4da6-a633-766e9403a401" />


### 👨‍💻 Footer

- Links to `Log In` and `Sign Up` if the user is not logged in, links to `Profile`, `Edit Profile` if the user is authenticated.
- Links to `Habits`, `Dopamine`, `Calendar`, in the `SOLIDIFY`section.
- Links to `Homepage`, `About Us`, `Contact Us`, in the `Learn More` section.
- Links to social media in the `Follow Us` section

<img width="1527" height="179" alt="image" src="https://github.com/user-attachments/assets/f2c91692-5fdb-436c-bca9-8f81617edeb6" />


### 🏠 Home

- A page that renders text dynamically introducing the user to the purpose of the application.
- Can be access regardless of the authentication of the user.

<img width="704" height="343" alt="image" src="https://github.com/user-attachments/assets/6ea2eac2-9b1d-4b59-93b4-5c229d59ddd6" />


### 📑 Create Category Page

- Displays relevant error messages and imposes restrictions such as 

<img width="720" height="374" alt="image" src="https://github.com/user-attachments/assets/f149d074-e6e4-4993-8cc1-3bc8bd9ff161" />

- Prompts the user to select a category from a dropdown menu which will eventually be used to group their habits and  routines.
- Prompts the user to select minimum habits that would be included in this category.

<img width="672" height="583" alt="image" src="https://github.com/user-attachments/assets/c2e89e0d-71e3-49a9-887b-764de5ccbe90" />


### 📊 All Categories Page

- Displays all existing category objects that belong to this user.
- Provides functionality to delete an existing category.
- Leads to Details page for the respective category
- Leads to Edit page for the respective category.


<img width="712" height="378" alt="image" src="https://github.com/user-attachments/assets/b4fcfe1c-9639-4cf6-b11e-384ed7bf87e7" />


### 🪂 Category Details Page

- Displays the description of the respective category
- If not description was provided upon creation, defaults to *'Not Provided'*

<img width="701" height="359" alt="image" src="https://github.com/user-attachments/assets/c3eadba4-b471-47a9-89bd-3c333ff13b8f" />


### 🖋️ Category Edit Page

- Allows the user to edit their existing category object.
- Displays warning message if they try to change a category type of an existing category.
- Displays the relevant error messages. For example, if the user already has category of this type.

<img width="705" height="351" alt="image" src="https://github.com/user-attachments/assets/240a494c-3291-41d0-8f57-b14bb327b9c3" />


<img width="705" height="338" alt="image" src="https://github.com/user-attachments/assets/b9c288c0-956e-45aa-848a-c24bf04ce45a" />



### 📑 Create Habit Page

- Allows the user to create a habit and attach a category object to it.
- The user must select dopamine type and name the habit (required fields)


<img width="731" height="359" alt="image" src="https://github.com/user-attachments/assets/1ad57840-2e69-4db0-9f0e-3781ec3cd979" />



### 📊 All Habits Page

- Displays all existing habit objects that belong to this user.
- Provides functionality to delete an existing habit.
- Leads to Details page for the respective habit.
- Leads to Edit page for the respective habit.

<img width="702" height="375" alt="image" src="https://github.com/user-attachments/assets/d613d195-bf5f-4de6-9399-7a61a86c7c2d" />



### 🪂 Habit Details Page

- Displays the description of the respective habit
- If not description was provided upon creation, defaults to *'Not Provided'*

<img width="695" height="419" alt="image" src="https://github.com/user-attachments/assets/49e91821-760b-4115-853f-3dca2df776bb" />


### 🖋️ Habit Edit Page

- Allows the user to edit their existing habit object.
- Displays the relevant error messages.

<img width="690" height="386" alt="image" src="https://github.com/user-attachments/assets/09fc85a4-d042-451f-8dc8-77144a41be29" />


### 🖋️ Profile Edit Page

- Allows the user to edit their existing profile (automatically created upon register)

<img width="693" height="424" alt="image" src="https://github.com/user-attachments/assets/0f6765fe-8a79-425b-b8a8-73971654bdfa" />


### 🪂 Profile Details Page

- Allows the user the see the details of their profile (allows you to see the picture of Boyko 😂)

<img width="708" height="493" alt="image" src="https://github.com/user-attachments/assets/1b32c553-0bb5-4a3e-a3b2-7c543dbbd339" />


### 🚀 Schedule Routine Page

- Allows the user to schedule an existing routine that they previously created
- Provides start and end time for the routine
- Recurrence functionality which allows the user to repeat the same routine - daily, weekly, monthly
- Provides 'repeat interval' - every week/day/month, every other week/day/month etc.
- Displays relevant error messages if the routine collides with any existing events/recurrent events
- Displays relevant error messages in case of date mismatches - e.g. routine scheduled in the past.

<img width="695" height="581" alt="image" src="https://github.com/user-attachments/assets/b4ac709d-e889-4639-b72a-6b3b70ce7fa2" />


### 🧠 Calendar Page

- Displays all of the scheduled routine objects for this user and their recurrences (if any)
- Allows the user to use different calendar grids - month/week/day
- Allows the user to see the routine details by clicking on the routine
- Allows editing of the routine, by dragging it into a different calendar slot
- Displays relevant error message if the calendar slot is already taken
- Displays warning message for the user who tries to drag a recurring routine

<img width="687" height="427" alt="image" src="https://github.com/user-attachments/assets/6834cd81-cdc9-4911-8b6c-8adb2e5ac39c" />


<img width="697" height="502" alt="image" src="https://github.com/user-attachments/assets/8408b6f3-f70f-4a4e-96b2-69e4826a597d" />


<img width="695" height="450" alt="image" src="https://github.com/user-attachments/assets/0c363625-8e06-4031-b776-3288f9a080ee" />


<img width="700" height="415" alt="image" src="https://github.com/user-attachments/assets/4a4d5425-5742-461f-aed1-27649ed1fb67" />


<img width="681" height="466" alt="image" src="https://github.com/user-attachments/assets/07ce60ea-caf8-4952-aa6e-3862c63c2b0f" />


<img width="694" height="457" alt="image" src="https://github.com/user-attachments/assets/0856e036-c695-4bf7-a358-61c8cd05c308" />


<img width="699" height="507" alt="image" src="https://github.com/user-attachments/assets/9d3e6bdf-df2d-4d98-a367-104f2904c97e" />


## 💉Technologies

- **Python**: Core language for functionality.
- **Django**: Python-based framework.
- **Django REST**: Python-based framework.
- **PostgreSQL**: Database system.
- **JavaScript**: Language for functionalities on the front-end.
- **FullCalendarJS**: Calendar basic grid functionality.
- **RRulePlugin**: Creating rules on the calendar.
- **HTML**: Language for the structure of the templates.
- **CSS**: Styling the application.
- **Azure**: Deployment platform.
- **Whitenoise**: Serves static files.
- **Gunicorn**: WSGI server.
- **Nginx**: Web server (DEV only).
- **Docker**: Container stack (DEV only).


## 🧑‍🔬Users for Testing

**Superuser** 🏋️‍♂️
User: superadmin@admin.com
PW: superadmin

**Admin** 💂‍♂️
User: admin@admin.com
PW: admin

**Regular User** 👨‍🦯
User: veli@gmail.com
PW: 123veli123


## 🚀 Running the app locally

### Prerequisites

- Python and Django installed.

### 🦑 Installation


1. Clone the repository:
    
    ```shell
    git clone https://github.com/velislavvelchev/SOLIDIFY
    ```
    
2. Create and activate venv
   
3. Install requirements.txt:
    
    ```shell
    pip install -r requirements.txt
    ```
4. Start the project:
    

    ```shell
    python manage.py runserver
    ```
