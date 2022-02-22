#!/usr/bin/env python3
import random


def generate(min_gen, max_gen, gen_entities):
     data = []
     i = 1
     while (i < gen_entities):
          data.append(random.randint(min_gen, max_gen))
          i += 1
     return data
     


def openfile():
     pass


def file_append():
     pass


def closefile():
     pass


def sayhello():
     print("Hello world !")

