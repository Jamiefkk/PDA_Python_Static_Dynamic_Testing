### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):#self not required as not initialised
    if card.value = 1: #should be == instead of =
      return True
    else #missing : after else
      return False
   
# dif instead of def
  dif highest_card(self, card1 card2): #comma missing after card1
  if card1.value > card2.value:#the next 4 lines of code are on the wrong indent
    return card #should be card1
  else:
    return card2
  


def cards_total(self, cards):
  total #should be total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total #return on wrong indent and no space after of (for looks)
  
```
