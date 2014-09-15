#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' by mark madden for week3 homework '''

SYSTOLIC = int(raw_input('Type your numeric systolic blood pressure please: '))
if SYSTOLIC < 90:
    BP_STATUS = "low"
elif SYSTOLIC < 120 and SYSTOLIC > 89:
    BP_STATUS = "ideal"
elif SYSTOLIC < 140 and SYSTOLIC > 119:
    BP_STATUS = "warning"
elif SYSTOLIC < 160 and SYSTOLIC > 139:
    BP_STATUS = "high"
elif SYSTOLIC > 159:
    BP_STATUS = "emergency"
print "Your status is currently: {0}".format(BP_STATUS)
