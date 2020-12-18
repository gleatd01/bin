import numpy as np
import pandas

d = pandas.read_csv("stats.csv", index_col="name")

d.loc['Griffin':'Daredevil','type']='Frigates'
d.loc['Cormorant Guardian':'Catalyst Covert Ops','type']='Destroyers'
d.loc['Moa Guardian':'Vigilant','type']='Cruisers'
d.loc['Ferox Guardian':'Brutix','type']='Battle Cruisers'
d.loc['Scorpion':'Vindicator','type']='Battle Ships'
d.loc['Tayra':'Venture III','type']='Industrial Ships'

d_frig=d[d.type.eq('Frigates')]
d_des=d[d.type.eq('Destroyers')]
d_cru=d[d.type.eq('Cruisers')]
d_bc=d[d.type.eq('Battle Cruisers')]
d_bs=d[d.type.eq('Battle Ships')]
d_ind=d[d.type.eq('Industrial Ships')]
