import numpy as np
import pandas

d = pandas.read_csv("stats.csv", index_col="name")
bp = pandas.read_csv("blueprints.csv", index_col="Name")

ship_id=0
material_id=0;

for ship_id in range(229):
    ship=d.index[ship_id];
    d.loc[ship,'Total Cost']=0;
    if ship == 'Condor' or ship == 'Merlin' or ship == 'Kestrel' or ship == 'Heron' or ship == 'Slasher' or ship == 'Rifter' or ship == 'Breacher' or ship == 'Probe' or ship == 'Executioner' or ship == 'Tormentor' or ship == 'Magnate'  or ship == 'Punisher' or ship == 'Atron' or ship == 'Tristan'  or ship == 'Incursus'  or ship == 'Imicus':
        continue
    elif  ship == 'Cormorant' or ship == 'Corax Trainer' or ship == 'Thrasher' or ship == 'Talwar Trainer' or ship == 'Coercer' or ship == 'Dragoon Trainer' or ship == 'Catalyst' or ship == 'Algos Trainer' or ship == 'Caracal Trainer' or ship == 'Moa Trainer' or ship == 'Stabber Trainer' or ship == 'Rupture Trainer' or ship == 'Omen Trainer' or ship == 'Maller Trainer' or ship == 'Vexor Trainer' or ship == 'Thorax Trainer' or ship == 'Venture Trainer':
        continue
    else:
        for material_id in range(51):
            d.loc[ship,bp.index[material_id]]=bp.loc[bp.index[material_id],ship];
    for material_id in range(51-9):
        resource=d.loc[ship,d.columns[material_id+9]]
        resource=resource.replace(',','')
        d.loc[ship,'Total Cost']=d.loc[ship,'Total Cost']+int(resource)*d.loc[d.columns[material_id+9],'buy']
