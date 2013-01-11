
import sys
import re

preamble = ['Introductory part of a bill, constitution that sets out in detail the underlying facts and assumptions, and explains its intent and objectives.','It describes the philosophy of the constitution.','It is a preface to the constitution.','Preamble of India is a unique piece of document. It is the soul and spirit of the constitution.']
people = ['Power rests in the hands of the people of India']
philosophy = ['A system of values by which one abides.','A system of thought based on or involving such enquiry.','A certain kind of thinking.','A set of ideas or beliefs relating to a particular field or activity.']

synonyms = { }
synonyms = {'preamble': preamble,'people' : people, 'philosophy' : philosophy } 

noResponse = ('Sorry, I did not understand your question.','Can you please elaborate more?')

print "Welcome to Justitia! How can I help you?"

words = [ ]
var = 1
matched = 0
responseIndex = 0
noResponseIndex = 0
temp = ""
oldKey = ""

while var==1:
      sentence = sys.stdin.readline()
      words = re.findall(r'\w+',sentence)
      #print words

      for key in synonyms:
          for searchKey in words:
              if searchKey == key:
                  temp = key
                  break
                  

                  
      if  temp!="":
            temp_list = synonyms[temp]
            size = len(temp_list)
            if oldKey == temp:
                if responseIndex < size-1:
                    responseIndex = responseIndex + 1
                    print temp_list[responseIndex]
                
                else:
                    print "Hmm.. Sorry! Thats all I know!"
            else:
                responseIndex = 0
                print temp_list[responseIndex]
                oldKey = temp
                
            temp=""
      else:
            #print "dont know"
            if noResponseIndex < len(noResponse):
                print noResponse[noResponseIndex]
                noResponseIndex = noResponseIndex + 1
            else:
                noResponseIndex = 0
                print noResponse[noResponseIndex]
                noResponseIndex = noResponseIndex + 1

            
