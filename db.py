# coding: utf-8
import shelve
import requests


class Database:

    def create_db(self):
        db = shelve.open('api_db')
        db.close()


def mode_change():
    return Database().create_db()
