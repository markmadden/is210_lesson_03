#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' task 4 homework week 3 Mark Madden '''

DAY = raw_input('What day is it?')
TIME = int(raw_input('What time is it as a 4-digin number without colons (eg. 1215)?'))
if DAY.lower()[:3] in ['sat','sun'] or TIME < 600:
    SNOOZE = True
else:
    SNOOZE = False


print ['Beep! Beep! Beep! Beep! Beep!', ''][bool(SNOOZE)]
