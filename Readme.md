# Installing and Setting Up the Project
## 1. Prerequisite apps
Make sure to have these app installed:
* **Python**
* **Node.js**
* **Git/Github** (optional)

## 2. Clone the project
On the terminal, cd to prefered directory then type
```shell
git clone https://github.com/Squishyblox/ProjectA.git
```
if you don't have git just download the project's zip file and extract to your prefered location.
## 3. Installing Dependencies
You WILL have to do this for every fresh repo clone.
In the project folder there will be **two** subfolders:
 * ***backend***: to host the API using *Django*
 * ***frontend***: to host the frondend using *Node.js*
### 3.1 Python
cd into ***backend***
```shell
python -m pip install -r requirements.txt
```
### 3.2 Node.js
cd into ***frontend***
```shell
npm install
```
## 4. Running the Project
### 4.1 Development Mode
cd into ***backend***
```shell
python manage.py runserver
```
cd into ***frontend***
```shell
npm run dev
```
Visit [http://localhost:5173/](http://localhost:5173/) to view the webapp
### 4.1 Production Mode
cd into ***backend***
```shell
python manage.py runserver
```
cd into ***frontend***
```shell
npm run build
npm run preview
```
Visit [http://localhost:4173/](http://localhost:4173/) to view the webapp



## Screenshots 
![image](./frontend/screenshots/home.png?raw=true)
![image](./frontend/screenshots/login.png?raw=true)
![image](./frontend/screenshots/staff.png?raw=true)
![image](./frontend/screenshots/staffedit.png?raw=true)
![image](./frontend/screenshots/services.png?raw=true)
![image](./frontend/screenshots/serviceedit.png?raw=true)
![image](./frontend/screenshots/inventory.png?raw=true)
