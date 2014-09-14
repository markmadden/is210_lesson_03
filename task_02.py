#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' by mark madden for week3 homework '''

BP_STATUS = int(raw_input('Type your numeric systolic blood pressure please: '))
if BP_STATUS < 90:
    print "Your status is currently: Low."
elif BP_STATUS < 120 and BP_STATUS > 89:
    print "Your status is currently: Ideal."
elif BP_STATUS < 140 and BP_STATUS > 119:
    print "Your status is currently: Warning!"
elif BP_STATUS < 160 and BP_STATUS > 139:
    print "Your status is currently: High."
elif BP_STATUS > 159:
    print "Your status is currently: Emergency!"
else:
    print "You entered an invalid input."
    
