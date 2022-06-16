# week-5-project

## Getting started

I got things rolling by creating a kanban board to get a scope of what features I wanted and needed for the website.

<img width="1440" alt="Screenshot 2022-05-27 at 13 25 21" src="https://user-images.githubusercontent.com/77740652/174102859-8e14d110-6782-4a13-8b6e-358554709590.png">

After that I got strted with creating the app. Firstly I made myself a development VM. Then made the basic CRUD functionality of the website.

<img width="1440" alt="Screenshot 2022-05-27 at 11 36 34" src="https://user-images.githubusercontent.com/77740652/174103612-597200da-ca86-4dac-8d2a-305f23acadd7.png">


## Risk assessment

Here is my risk assessment for this project as is only a library website I found there to be few risks involved and they were ealiy mittigated by exporting both my database uri and sectret key.

<img width="999" alt="Screenshot 2022-06-16 at 16 43 31" src="https://user-images.githubusercontent.com/77740652/174110629-67cdd336-9a44-44ec-ad32-5f8f18a63a7d.png">


## Redesigning

I soon realised that I had gotten quite ambitous wanting to add a login and and register page to the website and decided shortly after to bench this for now and potentially return to the idea if I had time.

<img width="1295" alt="Screenshot 2022-06-04 at 10 36 58" src="https://user-images.githubusercontent.com/77740652/174104068-ca548feb-742b-4f5f-816f-5d49ba19ed99.png">

<img width="957" alt="Screenshot 2022-06-04 at 10 49 29" src="https://user-images.githubusercontent.com/77740652/174104138-f45ad590-f066-4f17-b8cf-d1f64c94940d.png">

The original idea was to create a bookshop but agian after realising the time limitations of the project I decided to redesisgn the website to function as a library with basic CRUD functionality.

Here is some of the code I decided to scrap.

<img width="760" alt="Screenshot 2022-06-04 at 10 49 24" src="https://user-images.githubusercontent.com/77740652/174104591-cf160611-ce6a-46ee-889f-87cefd849c66.png">

This is what my routes folder looked like after redesigning the website.

<img width="1104" alt="Screenshot 2022-06-04 at 10 49 36" src="https://user-images.githubusercontent.com/77740652/174104741-094f7206-9992-452e-9faf-f7a8f92f6267.png">

I had an image of how I wanted the website to look in my head so added some css and images to get the look I wanted.

<img width="289" alt="Screenshot 2022-06-16 at 16 26 42" src="https://user-images.githubusercontent.com/77740652/174105397-5fcbc869-cd6c-46cf-b2da-ce607db936f8.png">

<img width="534" alt="Screenshot 2022-06-16 at 16 26 52" src="https://user-images.githubusercontent.com/77740652/174105420-901b2268-2027-45fd-9e45-0c9b5103e133.png">

<img width="1440" alt="Screenshot 2022-05-27 at 13 51 44" src="https://user-images.githubusercontent.com/77740652/174105459-85196aa8-6cdd-4da1-a3f0-e167a3a86912.png">


## Unit Testing

I started with making my test_app.py and my test base.

<img width="619" alt="Screenshot 2022-06-16 at 16 31 43" src="https://user-images.githubusercontent.com/77740652/174106488-31854616-f232-4ca2-9a85-065f6509aa38.png">

Here are the tests. 

<img width="617" alt="Screenshot 2022-06-16 at 16 31 53" src="https://user-images.githubusercontent.com/77740652/174107064-176a5d75-cc75-4fed-86da-5f6f4706c2c3.png">

And here is the pytest coverage report.

<img width="1025" alt="Screenshot 2022-06-16 at 16 34 59" src="https://user-images.githubusercontent.com/77740652/174107276-d3ad2002-1603-4f71-add4-fdbcb457e7bf.png">


## Jenkins

First I created a jenkins VM.

<img width="1061" alt="Screenshot 2022-05-31 at 09 13 37" src="https://user-images.githubusercontent.com/77740652/174107856-47467698-e43b-4f9c-9e11-8445f595d1f1.png">

I then proceeded to get Jenkins installed and running on that Virtual Machine.

<img width="1186" alt="Screenshot 2022-05-31 at 09 44 40" src="https://user-images.githubusercontent.com/77740652/174108355-7bdddb0f-80f7-46e5-b593-8d6e4143b5e7.png">

<img width="1364" alt="Screenshot 2022-06-16 at 09 56 43" src="https://user-images.githubusercontent.com/77740652/174108459-e69e3c99-184d-47f1-abc9-204b2f3b21ca.png">

I also added a coverage html and GitHub Webhook.

<img width="1128" alt="Screenshot 2022-06-16 at 09 59 22" src="https://user-images.githubusercontent.com/77740652/174108676-29adad31-ad56-4e3a-81dc-62e812599bb8.png">

<img width="1145" alt="Screenshot 2022-06-16 at 10 08 30" src="https://user-images.githubusercontent.com/77740652/174109169-a276e813-34fe-4799-99de-a7f597b7674e.png">


## Selenium

I was having problems using selenium on my current VM and Adam pointed out that the chromium browser didn't work properly with the Ubuntu version 20.04.

<img width="900" alt="Screenshot 2022-06-16 at 16 49 19" src="https://user-images.githubusercontent.com/77740652/174112478-b37c46de-fa26-41bf-89c3-58e19b2c6b3a.png">

So I set up a seperate selenium VM. 

<img width="793" alt="Screenshot 2022-06-16 at 16 50 26" src="https://user-images.githubusercontent.com/77740652/174112652-6efb75d3-aa65-417b-98eb-d62780ed3e01.png">

And after doing so I was able to get the selenium tests working corretcly.

<img width="742" alt="Screenshot 2022-06-16 at 16 52 33" src="https://user-images.githubusercontent.com/77740652/174113083-35ffe4df-344a-478e-a600-6839f706b137.png">

