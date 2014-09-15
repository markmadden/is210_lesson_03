#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' by mark madden for week3 homework '''

SYSTOLIC = int(raw_input('Type your numeric systolic blood pressure please: '))
if SYSTOLIC < 90:
    BP_STATUS = "Low."
elif SYSTOLIC < 120 and SYSTOLIC > 89:
    BP_STATUS = "Ideal."
elif SYSTOLIC < 140 and SYSTOLIC > 119:
    BP_STATUS = "Warning!"
elif SYSTOLIC < 160 and SYSTOLIC > 139:
    BP_STATUS = "High."
elif SYSTOLIC > 159:
    BP_STATUS = "Emergency."
print "Your status is currently: {0}".format(BP_STATUS)
