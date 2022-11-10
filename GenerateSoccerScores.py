# Wt's "Statistics trump soccerknowledge" Soccer tournament scores script
import random

country_list = [ "Brazilië", "België", "Argentinië", "Frankrijk", "Engeland", "Italië", "Spanje", "Nederland", "Portugal", "Denemarken", "Duitsland", "Kroatië", "Mexico", "Uruguay", "Zwitserland", "USA", "Colombia", "Senegal", "Wales", "Iran"
]

def number_of_ranked_countries(c1, c2):
  # returns how many of the countries (c1, c2) are ranked in the top 20
  n = 0
  if c1 in country_list:
    n += 1
  if c2 in country_list:
    n += 1
  return n

def get_country_rank(country):
  #returns position in top 20 list of supplied country
  for i in range(0, len(country_list)):
    if country_list[i] == country:
      return i
  return 1000000 #not in list? return terrible rank


def choose_win_draw():
  #randomly choose win or draw with weighted chance
  win_draw = [[26, "draw"], [100, "win"]]
  r = random.randint(1,100)
  for result in win_draw:
    if r <= result[0]:
      return result[1]

def choose_draw_result():
  #randomly choose draw score with weighted chance
  draw_result = [[45, "1-1"], [77, "0-0"], [96, "2-2"], [100, "3-3"]]
  r = random.randint(1,100)
  for result in draw_result:
    if r <= result[0]:
      return result[1]

def choose_win_result():
  #randomly choose win score with weighted chance
  win_result = [[26,"1-0"], [47,"2-1"], [64,"2-0"], [74,"3-1"], [83,"3-0"], [89,"3-2"], [93,"4-0"], [97,"4-1"], [100,"4-2"]]
  r = random.randint(1,100)
  for result in win_result:
    if r <= result[0]:
      return result[1]
  
def calculate_match_result(c1, c2):
  #determine result of match between c1 and c2

  if number_of_ranked_countries(c1, c2) == 1:
    #match of ranked country agains unranked country. Ranked country always wins
  
    #choose weighted result:
    score = choose_win_result()
  
    #make sure best country gets winning score:
    #if best country is c2, flip the score
    if (c2 in country_list):
      score = score[::-1]
    
  elif number_of_ranked_countries(c1,c2) == 2:
    # both countries are ranked. Statistically predict draw or win. 
    # if result is win, highest ranked country wins
    win_draw = choose_win_draw()
    if (win_draw == "draw"):
      score = choose_draw_result()
    else: #result == "win"    
      score = choose_win_result()
  
      #if best country is c2, flip score:
      if get_country_rank(c2) < get_country_rank(c1):
        score = score[::-1]
        
  else: #both countries unranked. Just use statistics:
    win_draw = choose_win_draw()
    if (win_draw == "draw"):
      score = choose_draw_result()
    else: #result == "win"    
      score = choose_win_result()
      
      #50% chance to flip result
      if (random.randint(1,2) == 2):
        score = score[::-1]    
  
  print(c1 + ' - ' + c2 + ":")
  print(score)
  print()
  return(score)

#while True:
#  c1 = input("Land 1: ")
#  c2 = input("Land 2: ")

#  calculate_match_result(c1,c2)


speelschema_ronde_1 = [["Qatar","Ecuador"],["Engeland","Iran"],["Senegal","Nederland"],["USA","Wales"],["Argentinië","Saudi Arabië"],["Denemarken","Tunesië"],["Mexico","Polen"],["Frankrijk","Australië"],["Marokko","Kroatië"],["Duitsland","Japan"],["Spanje","Costa Rica"],["België","Canada"],["Zwitserland","Kameroen"],["Uruguay","Zuid Korea"],["Portugal","Ghana"],["Brazilië","Servië"],["Wales","Iran"],["Qatar","Senegal"],["Nederland","Ecuador"],["Engeland","USA"],["Tunesië","Australië"],["Polen","Saudi Arabië"],["Frankrijk","Denemarken"],["Argentinië","Mexico"],["Japan","Costa Rica"],["België","Marokko"],["Kroatië","Canada"],["Spanje","Duitsland"],["Kameroen","Servië"],["Zuid Korea","Ghana"],["Brazilië","Zwitserland"],["Portugal","Uruguay"],["Ecuador","Senegal"],["Nederland","Qatar"],["Wales","Engeland"],["Iran","USA"],["Australië","Denemarken"],["Tunesië","Frankrijk"],["Saudi Arabië","Mexico"],["Polen","Argentinië"],["Kroatië","België"],["Canada","Marokko"],["Japan","Spanje"],["Costa Rica","Duitsland"],["Ghana","Uruguay"],["Zuid Korea","Portugal"],["Kameroen","Brazilië"],["Servië","Zwitserland"]]

for match in speelschema_ronde_1:
  calculate_match_result(match[0],match[1])