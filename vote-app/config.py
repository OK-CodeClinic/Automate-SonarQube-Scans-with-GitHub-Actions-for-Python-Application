## Auth: Kehinde Omokungbe

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'admin'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'tesfk2G5zOlghIaj5oLp'
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'vote-git.cdiywwmgitzb.us-west-2.rds.amazonaws.com'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'voting_system'
