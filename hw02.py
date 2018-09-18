#

#1
drax = {}
##1a
###  1C6_H10_O5 + 5 O2 -> 6 CO2 + 5 H2O
### 2C15_H11_0 + 34.5 O2 -> 30 CO2 + 11 H20
C = {'mass': 12} 
O = {'mass': 16}
H = {'mass': 1}

coal = {'mj/kg':29.3}
coal['mass'] = (C['mass'] * 15 ) + (H['mass'] * 11) + (O['mass'] * 1)
wood = {'mj/kg': 15.0}
wood['mass'] = (C['mass'] * 6) + (H['mass'] * 10) + (O['mass'] * 5)
co2 = {'mass': 44}

## wood = {'mass': 98.15}

###( 1 mol coal / 207g coal) * (30 co2 / 2 mol coal) * (44g co2 / 1 mol co2) * (1 kg / 1000 g ) * (1000 g / 1 kg)
coal['kg_co2/kg_coal'] = ( 1 / coal['mass']) * ( 30 / 2 ) * (co2['mass'] / 1 ) * (1000 / 1) * (1 / 1000)
coal['kg_co2/gj_t'] = coal['kg_co2/kg_coal'] * ( 1 / coal['mj/kg']) * (1000 / 1 )

###( 1 mol coal / 207g coal) * (30 co2 / 2 mol coal) * (44g co2 / 1 mol co2) * (1 kg / 1000 g ) * (1000 g / 1 kg)
wood['kg_co2/kg_wood'] = ( 1 / wood['mass']) * ( 30 / 2) * (co2['mass'] / 1 ) * ( 1000 / 1 ) * (1 / 1000)
wood['kg_co2/gj_t'] = wood['kg_co2/kg_wood'] * ( 1 / wood['mj/kg'] )  * (1000 / 1 )

print(coal['kg_co2/gj_t'])
print(wood['kg_co2/gj_t'])
## ANSWERS 109 kg CO2 / 1 GJ coal, 4 kg CO2 / 1 GJ wood

#1b
drax['coal_eff'] = 0.37 
drax['biomass_eff'] = 0.33
gj_kwh = 1 / 277.7

coal['kg_co2/kwh_e'] = (coal['kg_co2/gj_t'] / drax['coal_eff'] ) * gj_kwh
wood['kg_co2/kwh_e'] = (wood['kg_co2/gj_t'] / drax['biomass_eff'] ) * gj_kwh

print(coal['kg_co2/kwh_e'])
print(wood['kg_co2/kwh_e'])
## ANSWERS 1.1 kg co2/kwh_e coal, 3 kg co2 / kwh_e wood. Based on this data alone, it will not be. However this does not account for the source of the carbon. While the total emissions is higher for biomass, it is using co2 that is already in the modern carbon cycle. The coal is introducing 'stored' carbon that has not been present in the modern carbon cycle.

##1c
drax['coal_tonnes_y'] = 9.1e6
drax['nameplate_mw'] = 4.0e3
kg_tonnes = 1000 / 1
kwh_mj = 1 / 3.6
kwh_mwh = 1000 / 1 
drax['coal_kwh_y_e'] = drax['coal_tonnes_y'] * kg_tonnes * coal['mj/kg'] * kwh_mj * drax['coal_eff']
drax['coal_cap_factor'] = (drax['coal_kwh_y_e'] / kwh_mwh) / (drax['nameplate_mw'] * 8760 )
## ANSWERS capacity factor before 2014: 0.78

##1d
drax['biomass_tonnes_y'] = 13.8e6
drax['new_unit'] = {'cap_factor': 80.0}
drax['biomass_kwh_y_e'] =  drax['biomass_tonnes_y'] * kg_tonnes * wood['mj/kg'] * kwh_mj * drax['biomass_eff']

drax['new_unit']['nameplate_mw'] = ( drax['coal_kwh_y_e'] - drax['biomass_kwh_y_e'] ) * (1 / 8760 ) * (1 / kwh_mwh) / 0.80  # <--- too high?
## ANSWERS 1200 MW

##1e
j_gj = 10e9
kwh_j = 1 / 3.6e6
mw_kw = 1 / 10e3
tonne_tons = 1 / 1.102
ng_mj_kg = 50.0
j_mj = 10e6 
kg_tonne = 10e3 / 1
chp = {'eff':0.80, 'ng_in_tons_hr': 2.7, 'e_out_mw': 25, 'heat_out_gj_hr': 16}
qth_mw = chp['heat_out_gj_hr'] *  j_gj * kwh_j * mw_kw
qfuel = chp['ng_in_tons_hr'] * tonne_tons * kg_tonne * ng_mj_kg *  j_mj * kwh_j * mw_kw
a = 0.80
no = (chp['e_out_mw'] + qth_mw)  / qfuel
eee = chp['e_out_mw'] / (qfuel - (qth_mw / a )) ## <-- Seems to be off by factor of 1
## ANSWERS 

#4
##4a
from math import e, log
countries = { 'us':{'energy_yr_mtoe':{2007:2321, 2017:2235}, 'co2_yr_mtonnes':{2007: 5581, 2017: 5088}}, 
              'br':{'energy_yr_mtoe':{2007:230, 2017:294}, 'co2_yr_mtonnes':{2007: 351, 2017: 467}},
              'ru':{'energy_yr_mtoe':{2007:673, 2017:698}, 'co2_yr_mtonnes':{2007: 1528, 2017: 1525}},
              'in':{'energy_yr_mtoe':{2007:450, 2017:754}, 'co2_yr_mtonnes':{2007: 1366, 2017: 2344}},
              'cn':{'energy_yr_mtoe':{2007:2150, 2017:3132}, 'co2_yr_mtonnes':{2007: 7215, 2017: 9233}}
            }

def energy_r(energy_2007, energy_2017):
    math.log(energy_2017 / energy_2007) / 10

