# **GoodsTransportationService**
GoodsTransportationService - A web Application where dealers can book drivers for transporting their Goods, developed for Hackathon.

<strong>Frameworks/Languages Used : </strong> HTML, CSS, Django(Python), Bootstrap, MySQL Database.

## **How to Run**

* Clone the github repository by using the command
```shell
    git clone <REPOSITORY_URL>
```
* Move to the cloned repository by using
```shell
    cd <REPOSITORY_NAME>
```
* Install all the required python libraries by using
```shell
    pip install -r requirements.txt
```
* In settings.py file enter you gmail id and password for OTP support at the end of the file in the commented area
```python
    EMAIL_HOST_USER = # Enter your mail id here
    EMAIL_HOST_PASSWORD = # Enter your password here
```
* Make Migrations
```shell
    python manage.py makemigrations
```
* Migrate
```shell
    python manage.py migrate
```
* Run the Django app by using the command
```shell
    python manage.py runserver
```
* Now Visit the url localhost:8000/ in you browser

### **Features**
- Login
  - User can Login Via email, password
  - User can Login Via email, OTP send to the mail ID
- Signup for both dealer and driver
- Dealer's Home screen will show all the drivers intersted in travilling on the same route
- Dealer can search drivers by state and city
- Driver's Home screen will show all his bookings
- When State is selected all the city of the state will be displayed
