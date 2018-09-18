#1
##1a
  #Energy is the abilty to do perform work. 
  # Power is the rate at which energy is consumed. i.e. a desktop computer is rated for 1kw of power. Running that 24 hrs will consume 24kwh of energy.

#1b //sig figs 1
nameplate_capacity_mw = 9
record_day = {'kwh':215901.1}
record_day['avg_kw'] = record_day['kwh'] / 24
record_day['avg_mw'] = record_day['avg_kw'] / 1000
capacity_factor = record_day['avg_mw'] / nameplate_capacity_mw

new_nameplate_mwh_yr = 9.5 * 24 * 365
assumed_cap_factor = 0.419

new_total_mwh = new_nameplate_mwh_yr * assumed_cap_factor

ca_pop = 40e6
ca_e_per_cap_mwh_yr = 6.536
turbines  = ca_pop * ca_e_per_cap_mwh_yr * (1 / new_total_mwh)
### ANSWERS capacity factor = 100%,  upgraded mwh = 35,000 mwh, turbines = 7500

#1c
old_fridge_kwh_year = 58.8 * 24 * 365 / 1000
old_fridge_kwh_year
#### ANSWERS 515 kwh/yr

#2
sungrow_plant = {'power_mw':40.0, 'cap_factor':0.27, 'homes_equiv':15000}
sungrow_plant['mw'] = sungrow_plant['power_mw'] * sungrow_plant['cap_factor']
china = {'energy_kwh_yr': 6.31e12}

##2a
avg_home_kw = (sungrow_plant['mw'] / 1000) / sungrow_plant['homes_equiv']
### ANSWER avg home kw = 7.2e-7

##2b
china['res_energy_percent'] = 0.14
china['homes'] = (china['energy_kwh_yr'] * china['res_energy_percent']) * ( 1 / (avg_home_kw * 8760 ))
### ANSWER 1.4e8 homes

##2c
kwh_to_mwh = 1e3
j_to_kwh = 3.6e6
gj_to_j = 1 / 1e9
sungrow_plant['mwh'] = sungrow_plant['mw'] * 24 * 365
sungrow_plant['gj'] = sungrow_plant['mwh'] * kwh_to_mwh *  j_to_kwh * gj_to_j
### ANSWER 3.4e5 GJ

##2e
mwh_to_kwh = 1 / 1000
solar_farms = china['energy_kwh_yr'] * mwh_to_kwh  * (1 / sungrow_plant['mwh'])
### ANSWER 67,000 Solar Farms

##2f
china['fuels_eff'] = 0.30
barrel_kw = 1 / 17000 * 0.3
china['req_oil'] = china['energy_kwh_yr'] * barrel_kw
### ANSWER 1.2e10 Barrels

##2g
nuke_fuel = {'mw_day_per_tonne': 270000}
kwd_to_mwd = 1000 / 1
kwh_to_kwd = 24 / 1
nuke_fuel['kwh_per_kg'] = nuke_fuel['mw_day_per_tonne'] *  kwd_to_mwd * kwh_to_kwd

china['req_nuke_fuel_kg'] = china['energy_kwh_yr'] * (1 / nuke_fuel['kwh_per_kg']) * china['fuels_eff']
### ANSWER 3.3e6 Kg fuel

##2h
wood = {'energy_kg_kwh': 2.7}

china['req_wood_kg'] = china['energy_kwh_yr'] * (1 / wood['energy_kwh']) * china['fuels_eff'] 
### ANSWER 7.8e12 kg wood

##2i
coal = {'energy_kg_kwh':8.1}
china['req_coal_kg'] = china['energy_kwh_yr'] * ( 1 / coal['energy_kwh'] ) * china['fuels_eff'] 
### ANSWER 2.6e12 kg coal

##2j
ng = {'energy_kg_m3': 35.319 }
cuft_to_m3 = 35.314 / 1 
china['req_ng_cuft'] = china['energy_kwh_yr'] * ( 1 / ng['energy_kg_m3'] ) * cuft_to_m3 * china['fuels_eff'] 
### ANSWER 6.8e13 cu-ft

##2k
hydro ={'energy_gallons_j': 6859.9}
china['req_hydro_gallons'] = china['energy_kwh_yr'] * (1 / hydro['energy_gallons_j'] ) * china['fuels_eff'] 
### ANSWER 1.1e15 gallons

##2l
### ANSWER oil = 14.5 Mj/kg, nuclear = 7e6 mj/kg, wood = 4.5 mj/kg, coal = 8.7 mj/kg, nat. gas = 16 mj/kg 

#3
##3a
### ANSWER US/World consumption = 17.3%

##3b 
### ANSWER ALL IN BTU: US. = 3.07e8, guatemala = 1.4e7, india = 1.91E7, Germany = 1.61, Japan = 1.48e8, Ethiopia = 2.34e6, China = 8.60E7

##3c
us_btu_pp = 3.07e8
eth_btu_pp = 2.34e6
problem3_ratio = us_btu_pp / eth_btu_pp
### ANSWER 131: 1 US/Ethopia 

##3d
### ANSWER

##3e
### ANSWER 
#### 1. EI helps establish how energy efficient an economy is. Energy use per capita does not reveal how efficent an economy is at turning that energy into wealth. 
#### 2. That the environmental, policy, or economic conditions have been changing the in the country. If environmental, the climate could be becoming more temperate. Policy could have driven more efficent use of energy through transit or housing code initatives. The economy could be transitioning away from high energy, low profit manufacturing, to a more services based economy.
#### 3. One nation may have stricter policies around energy efficency, a more dense population (smaller homes, shorter commute times, public transit use), a more temporate climate in high producing urban centers, higher levels of automation, or an economy with more low energy services vs something with more heavy industry. All of these could create such a difference. 

#4
##4a Exporer vs Civic
explorer = {'city_mpg': 13, 'hw_mpg': 18}
civic = {'lp100': 4.2}
percent_hwy = 0.70
percent_city = 0.30
gas_dollar = 3.00
miles_yr = 12000
miles_day = miles_yr / 365

explorer['avg_mpg'] = (explorer['city_mpg'] * percent_city ) + (explorer['hw_mpg'] * percent_city)
explorer['daily_gal'] = miles_day / explorer['avg_mpg']
explorer['year_gal'] = miles_yr / explorer['avg_mpg']
explorer['year_cost'] = explorer['year_gal'] * gas_dollar

def lp100km_to_mpg(l):
    us_gal_to_liter = (1 / 3.7)
    km_to_miles = (1 / 0.62)
    gal_to_mile = (l / 100) * us_gal_to_liter * km_to_miles
    return 1 / gal_to_mile

civic['avg_mpg'] = lp100km_to_mpg(civic['lp100'])
civic['daily_gal'] = miles_day / civic['avg_mpg']
civic['year_gal'] = miles_yr / civic['avg_mpg']
civic['year_cost'] = civic['year_gal'] * gas_dollar

efficiency = civic['avg_mpg'] / explorer['avg_mpg']
savings = explorer['year_cost'] - civic['year_cost']
### ANSWER  efficencty = 3.5x, savings ~$15,000

##4b
###4bi
ev = {'num_cars':1e6,'mile_p_kwh':5.0,'yearly_miles':12000}
ice = {'num_cars':1e6, 'mpg':30,'yearly_miles':12000}
ice['year_gallons'] = ice['num_cars'] * ( ice['yearly_miles'] / ice['mpg'])
#### ANSWER gallons saved = 4e8

###4bii

old_fridge = {'power_w':110}
new_fridge = {'increased_eff':0.40}
new_fridge['power_w'] = old_fridge['power_w'] * new_fridge['increased_eff']
new_fridge['year_energy_kwh'] = (new_fridge['power_w'] / 1000) * 24 * 365

ev['year_kwh'] = ev['num_cars'] * (ev['yearly_miles'] / ev['mile_p_kwh'])

req_fridges = ev['year_kwh'] / new_fridge['year_energy_kwh']
#### ANSWER 6.2e6 fridges

###4biii
### ANSWER
#write elsewhwere
#CA's 

##4c
person = {'cal_mi_run':100, 'cal_mi_walk':80, 'cal_mi_bike': 35 }

def miles_per_gallon(cal):
    #first get cal to gal, then flip
    kcal_to_cal = (1/10e3)
    cal_to_J = (1/4.1868)
    J_to_GJ = (10e9/1)
    gj_to_gal = (1/8)
    miles_per_gallon = (1 / cal) * kcal_to_cal * cal_to_J * J_to_GJ * gj_to_gal
    return miles_per_gallon

run_mpg = miles_per_gallon(100)
walk_mpg = miles_per_gallon(80)
bike_mpg = miles_per_gallon(35)

#### ANSWER run = 298 MPG, walk = 373 MPG, bike = 853 MPG

#5
##5a
ab = {'energy_per_year_twh':6.0, 'beer_per_year_gallons': 16.2e9}

ab['power_mw'] = (ab['energy_per_year_twh'] * 1e6) / 8760

power_plant_mw = ab['power_mw'] / 0.66
### ANSWER 1,000 MW

##5b
solar_farm_mw = ab['power_mw'] / 0.17

solar_farm_area_acres = solar_farm_mw * 4.0

acres_to_fbf = 1 / 1.32

solar_farm_area_fbf = solar_farm_area_acres * acres_to_fbf
### ANSWER 12,200 Football fields

##5c
oz_per_gal = 128
bottle_per_oz = 1 / 12

ab['beer_per_year_bottles'] = ab['beer_per_year_gallons'] * oz_per_gal * bottle_per_oz
kwh_to_twh = 1e9 / 1
kwh_to_j = 3.6e6
kj_to_j = 1 / 1000
ab['kj_per_bottle'] = (ab['energy_per_year_twh'] / ab['beer_per_year_bottles']) * kwh_to_twh * kwh_to_j * kj_to_j
### ANSWER 125 kj per bottle 

##5d
stella = {'kcal': 153}
cal_to_kcal = 10e3 / 1 
j_to_cal = 4.1868 / 1

stella['kj'] = stella['kcal'] * cal_to_kcal * j_to_cal * kj_to_j 

energy_ratio = stella['kj'] / ab['kj_per_bottle']
### ANSWER ratio: 1/5 

##5e
cal = {}
kjh_to_wh = 3.6
mw_to_w = 1 / 10e6
cal['students'] = 29311
mw_to_acres = 1 / 4
beers_per_week = 5
cal['school_weeks'] = 32
cal['beer_per_week'] = cal['students'] * (beers_per_week) 
cal['beer_per_school_year'] = cal['beer_per_week'] * cal['school_weeks']
cal['mwh_per_school_year'] = cal['beer_per_school_year'] * ab['kj_per_bottle'] * (1 / kjh_to_wh) * mw_to_w
cal['mw_per_school_year'] = cal['mwh_per_school_year'] / 8760
cal['solar_plant_acres'] = cal['mw_per_school_year'] / 0.17 * (1 / mw_to_acres)
### ANSWER  0.45 acres

