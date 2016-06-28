import requests
import config
import json
import random import randit
from templates.txt import TextTemplate
heads = open(heads.txt,r+)
tails = open(tails.txt, r+)
def process(input,entites=none):
  output ={}
  try:
  answer = randit(1,2)
  if answer == 1:
    output['input']= input
    output['output']= TextTemplate(choice(heads)).get_message()
    output['success']= true
  if answer == 2:
    output['input']= input
    output['output']= TextTemplate(choice(tails)).get_message()
    output['success']= true
execpt:
  output['success']= false
return output
 
  
      
  

    
  
  
