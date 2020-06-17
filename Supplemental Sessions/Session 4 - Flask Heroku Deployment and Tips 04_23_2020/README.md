# Heroku Flask Deployment Session

## In this session we went over in detail:
    1. Creating Python Environment
    2. Setting up our dependencies in the environment and Procfile/ requirements.txt 
    3. Deploying to Heroku
    4. Heroku Tips and Tricks

## Here are some commands/steps you may need:

1. `conda create -n your_env python=3.6`
2. `conda activate your_env`
3. `pip install flask`
4. `pip install gunicorn`
5. `pip freeze > requirements.txt`
6. Procfile needs to be named `Procfile` Note the Capital P.
7. This should go into your Procfile `web: gunicorn flaskfilename:app`
8. Add, commit, push to heroku `git push heroku master`
9. Open Heroku Flask deployment site using `heroku open`


 You can run the virtual bash on heroku using following:
 `heroku run bash`


### Link to Video : https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=989413cf-16c1-454f-bdab-aba600fb42da