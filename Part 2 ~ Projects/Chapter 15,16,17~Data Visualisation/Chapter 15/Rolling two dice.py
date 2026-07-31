import pygal
from DieClass import Die
die_1=Die()
die_2=Die()
results=[]
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
hist=pygal.Bar()
hist.title="Results of rolling two D6 dice 1000 times."
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add("D6 + D6",frequencies)
hist.render_to_file('dice_visual.svg')

##The Two Inputs of add()
# As seen on line 19 of your script (hist.add("D6 + D6", frequencies)), the function takes two mandatory parameters:
# The Label ("D6 + D6"): The first input is always a string. It tells pygal what name to attach to this data package. It handles two jobs:
#            It creates the legend title at the top left of your preview screen.
#            It displays inside the interactive pop-up tooltip when you hover your mouse pointer over any of the rendered bars.
# The Dataset (frequencies): The second input is your array or list of values. pygal iterates over each number in this list and creates a corresponding vertical bar. The heights of the bars directly reflect the numerical values inside this list.


