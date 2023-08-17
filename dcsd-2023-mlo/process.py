import os
import pandas as pd
from collections import defaultdict

def process_files(directory):
    raw_data = {
        '2007': {},
        '2008': {},
        '2009': {},
        '2010': {},
        '2011': {},
        '2012': {},
        '2013': {},
        '2014': {},
        '2015': {},
        '2016': {},
        '2017': {},
        '2018': {},
        '2019': {},
        '2020': {},
        '2021': {},
        '2022': {},
        '2023': {}
    }

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xls'):
                raw_data[os.path.basename(root)[-4:]][file] = pd.read_excel(os.path.join(root, file))

    processed_data = {
        'Instructional_Salaries': defaultdict(list),
        'Instructional_Employee Benefits': defaultdict(list),
        'Instructional_Purchased Services': defaultdict(list),
        'Instructional_Supplies & Materials': defaultdict(list),
        'Instructional_Capital Outlay': defaultdict(list),
        'Instructional_Other': defaultdict(list),
        'Other_Community Services': defaultdict(list),
        'Other_Other': defaultdict(list),
        'Support_Pupils': defaultdict(list),
        'Support_Instructional Staff': defaultdict(list),
        'Support_General Administration': defaultdict(list),
        'Support_School Administration': defaultdict(list),
        'Support_Operations & Maintenance': defaultdict(list),
        'Support_Pupil Transporation': defaultdict(list),
        'Support_Food Services': defaultdict(list),
        'Support_Other': defaultdict(list),
        'Total': defaultdict(list),
        'Teacher Turnover Rate': defaultdict(list),
        'Teacher Growth Rate': defaultdict(list)
    }

    districts = ['MAPLETON 1', 'ADAMS COUNTY 14', 'BENNETT 29J', 'STRASBURG 31J', 'ALAMOSA RE-11J', 'SANGRE DE CRISTO RE-22J', 'ENGLEWOOD 1', 'SHERIDAN 2', 'CHERRY CREEK 5', 'LITTLETON 6', 'DEER TRAIL 26J', 'ADAMS-ARAPAHOE 28J', 'BYERS 32J', 'ARCHULETA COUNTY 50 JT', 'WALSH RE-1', 'PRITCHETT RE-3', 'SPRINGFIELD RE-4', 'VILAS RE-5', 'CAMPO RE-6', 'LAS ANIMAS RE-1', 'BOULDER VALLEY RE 2', 'BUENA VISTA R-31', 'SALIDA R-32', 'KIT CARSON R-1', 'CHEYENNE COUNTY RE-5', 'CLEAR CREEK RE-1', 'NORTH CONEJOS RE-1J', 'SANFORD 6J', 'SOUTH CONEJOS RE-10', 'CENTENNIAL R-1', 'SIERRA GRANDE R-30', 'CROWLEY COUNTY RE-1-J', 'DELTA COUNTY 50(J)', 'DENVER COUNTY 1', 'DOLORES COUNTY RE NO.2', 'DOUGLAS COUNTY RE 1', 'EAGLE COUNTY RE 50', 'KIOWA C-2', 'BIG SANDY 100J', 'ELBERT 200', 'AGATE 300', 'CALHAN RJ-1', 'HARRISON 2', 'WIDEFIELD 3', 'FOUNTAIN 8', 'COLORADO SPRINGS 11', 'CHEYENNE MOUNTAIN 12', 'MANITOU SPRINGS 14', 'ACADEMY 20', 'ELLICOTT 22', 'PEYTON 23 JT', 'HANOVER 28', 'LEWIS-PALMER 38', 'EDISON 54 JT', 'MIAMI/YODER 60 JT', 'CANON CITY RE-1', 'COTOPAXI RE-3', 'GARFIELD RE-2', 'GARFIELD 16', 'EAST GRAND 2', 'GUNNISON WATERSHED RE1J', 'HINSDALE COUNTY RE 1', 'HUERFANO RE-1', 'LA VETA RE-2', 'JEFFERSON COUNTY R-1', 'EADS RE-1', 'PLAINVIEW RE-2', 'ARRIBA-FLAGLER C-20', 'STRATTON R-4', 'BETHUNE R-5', 'BURLINGTON RE-6J', 'LAKE COUNTY R-1', 'DURANGO 9-R', 'BAYFIELD 10 JT-R', 'IGNACIO 11 JT', 'POUDRE R-1', 'TRINIDAD 1', 'PRIMERO REORGANIZED 2', 'HOEHNE REORGANIZED 3', 'AGUILAR REORGANIZED 6', 'BRANSON REORGANIZED 82', 'KIM REORGANIZED 88', 'LIMON RE-4J', 'KARVAL RE-23', 'VALLEY RE-1', 'FRENCHMAN RE-3', 'PLATEAU RE-5', 'DE BEQUE 49JT', 'PLATEAU VALLEY 50', 'MESA COUNTY VALLEY 51', 'MONTEZUMA-CORTEZ RE-1', 'DOLORES RE-4A', 'MANCOS RE-6', 'MONTROSE COUNTY RE-1J', 'WEST END RE-2', 'BRUSH RE-2(J)', 'FORT MORGAN RE-3', 'WELDON VALLEY RE-20(J)', 'WIGGINS RE-50(J)', 'EAST OTERO R-1', 'ROCKY FORD R-2', 'MANZANOLA 3J', 'FOWLER R-4J', 'CHERAW 31', 'SWINK 33', 'OURAY R-1', 'RIDGWAY R-2', 'PLATTE CANYON 1', 'PARK COUNTY RE-2', 'HOLYOKE RE-1J', 'HAXTUN RE-2J', 'ASPEN 1', 'GRANADA RE-1', 'LAMAR RE-2', 'HOLLY RE-3', 'WILEY RE-13 JT', 'PUEBLO CITY 60', 'RANGELY RE-4', 'MONTE VISTA C-8', 'SARGENT RE-33J', 'HAYDEN RE-1', 'STEAMBOAT SPRINGS RE-2', 'SOUTH ROUTT RE 3', 'MOUNTAIN VALLEY RE 1', 'MOFFAT 2', 'CENTER 26 JT', 'TELLURIDE R-1', 'NORWOOD R-2J', 'JULESBURG RE-1', 'SUMMIT RE-1', 'CRIPPLE CREEK-VICTOR RE-1', 'WOODLAND PARK RE-2', 'AKRON R-1', 'ARICKAREE R-2', 'OTIS R-3', 'LONE STAR 101', 'WOODLIN R-104', 'EATON RE-2', 'GREELEY 6', 'PLATTE VALLEY RE-7', 'AULT-HIGHLAND RE-9', 'BRIGGSDALE RE-10', 'PRAIRIE RE-11', 'PAWNEE RE-12', 'YUMA 1', 'WRAY RD-2', 'IDALIA RJ-3', 'LIBERTY J-4']

    for year in ['2007']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']

        for district in districts:
            r_instructional = instructional.index[instructional['DISTRICT/'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]

            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[9])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[10])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[11])

            r_support = support.index[support['DISTRICT/'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[3])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[4])
            processed_data['Support_General Administration'][district].append(d_support.iloc[5])
            processed_data['Support_School Administration'][district].append(d_support.iloc[6])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[7])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[8])
            processed_data['Support_Food Services'][district].append(d_support.iloc[9])
            processed_data['Support_Other'][district].append(d_support.iloc[10])

            r_other = other.index[other['DISTRICT/'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[5])
            processed_data['Other_Other'][district].append(d_other.iloc[6])
            processed_data['Total'][district].append(d_other.iloc[7])

            r_turnover = turnover.index[turnover['Unnamed: 1'] == district].tolist()[0] + 3
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[9])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[5] / d_turnover.iloc[4] - 1)

    for year in ['2008']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']

        for district in districts:
            r_instructional = instructional.index[instructional['DISTRICT/'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]

            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[9])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[10])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[11])

            r_support = support.index[support['DISTRICT/'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[3])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[4])
            processed_data['Support_General Administration'][district].append(d_support.iloc[5])
            processed_data['Support_School Administration'][district].append(d_support.iloc[6])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[7])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[8])
            processed_data['Support_Food Services'][district].append(d_support.iloc[9])
            processed_data['Support_Other'][district].append(d_support.iloc[10])

            r_other = other.index[other['DISTRICT/'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[5])
            processed_data['Other_Other'][district].append(d_other.iloc[6])
            processed_data['Total'][district].append(d_other.iloc[7])

            r_turnover = turnover.index[turnover['Unnamed: 1'] == district].tolist()[0] + 2
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[9])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[5] / d_turnover.iloc[4] - 1)
    
    for year in ['2009', '2010', '2011', '2012']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']

        for district in districts:
            r_instructional = instructional.index[instructional['DISTRICT/'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]
            
            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[9])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[10])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[11])
            
            r_support = support.index[support['DISTRICT/'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[3])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[4])
            processed_data['Support_General Administration'][district].append(d_support.iloc[5])
            processed_data['Support_School Administration'][district].append(d_support.iloc[6])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[7])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[8])
            processed_data['Support_Food Services'][district].append(d_support.iloc[9])
            processed_data['Support_Other'][district].append(d_support.iloc[10])

            r_other = other.index[other['DISTRICT/'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[5])
            processed_data['Other_Other'][district].append(d_other.iloc[6])
            processed_data['Total'][district].append(d_other.iloc[7])

            r_turnover = turnover.index[turnover['Unnamed: 1'] == district].tolist()[0] + 2
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[10])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[5] / d_turnover.iloc[4] - 1)

    for year in ['2013']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']

        for district in districts:
            r_instructional = instructional.index[instructional['DISTRICT/'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]
            
            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[9])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[10])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[11])
            
            r_support = support.index[support['DISTRICT/'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[4])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[5])
            processed_data['Support_General Administration'][district].append(d_support.iloc[6])
            processed_data['Support_School Administration'][district].append(d_support.iloc[7])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[8])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[9])
            processed_data['Support_Food Services'][district].append(d_support.iloc[10])
            processed_data['Support_Other'][district].append(d_support.iloc[11])

            r_other = other.index[other['Unnamed: 2'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[6])
            processed_data['Other_Other'][district].append(d_other.iloc[7])
            processed_data['Total'][district].append(d_other.iloc[8])

            r_turnover = turnover.index[turnover['Unnamed: 1'] == district].tolist()[0] + 2
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[10])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[5] / d_turnover.iloc[4] - 1)

    for year in ['2014']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']

        for district in districts:
            r_instructional = instructional.index[instructional['DISTRICT/'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]

            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[9])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[10])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[11])

            r_support = support.index[support['DISTRICT/'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[4])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[5])
            processed_data['Support_General Administration'][district].append(d_support.iloc[6])
            processed_data['Support_School Administration'][district].append(d_support.iloc[7])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[8])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[9])
            processed_data['Support_Food Services'][district].append(d_support.iloc[10])
            processed_data['Support_Other'][district].append(d_support.iloc[11])

            r_other = other.index[other['Unnamed: 2'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[6])
            processed_data['Other_Other'][district].append(d_other.iloc[7])
            processed_data['Total'][district].append(d_other.iloc[8])

            r_turnover = turnover.index[turnover['Unnamed: 1'] == district].tolist()[0] + 8
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[9])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[4] / d_turnover.iloc[3] - 1)

    for year in ['2015']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']

        for district in districts:
            r_instructional = instructional.index[instructional['DISTRICT/'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]

            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[9])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[10])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[11])

            r_support = support.index[support['DISTRICT/'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[4])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[5])
            processed_data['Support_General Administration'][district].append(d_support.iloc[6])
            processed_data['Support_School Administration'][district].append(d_support.iloc[7])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[8])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[9])
            processed_data['Support_Food Services'][district].append(d_support.iloc[10])
            processed_data['Support_Other'][district].append(d_support.iloc[11])

            r_other = other.index[other['Unnamed: 2'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[6])
            processed_data['Other_Other'][district].append(d_other.iloc[7])
            processed_data['Total'][district].append(d_other.iloc[8])

            r_turnover = turnover.index[turnover['District Name'] == district].tolist()[0] + 8
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[9])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[4] / d_turnover.iloc[3] - 1)

    for year in ['2016']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']
        
        for district in districts:
            r_instructional = instructional.index[instructional['Unnamed: 2'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]

            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[4])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[5])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[9])
            
            r_support = support.index[support['DISTRICT/'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[4])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[5])
            processed_data['Support_General Administration'][district].append(d_support.iloc[6])
            processed_data['Support_School Administration'][district].append(d_support.iloc[7])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[8])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[9])
            processed_data['Support_Food Services'][district].append(d_support.iloc[10])
            processed_data['Support_Other'][district].append(d_support.iloc[11])

            r_other = other.index[other['Unnamed: 2'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[6])
            processed_data['Other_Other'][district].append(d_other.iloc[7])
            processed_data['Total'][district].append(d_other.iloc[8])

            r_turnover = turnover.index[turnover['Orgnazation Name'] == district].tolist()[0] + 8
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[11])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[4] / d_turnover.iloc[3] - 1)

    for year in ['2017']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']

        for district in districts:
            r_instructional = instructional.index[instructional['DISTRICT/'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]

            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[4])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[5])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[9])
            
            r_support = support.index[support['DISTRICT/'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[4])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[5])
            processed_data['Support_General Administration'][district].append(d_support.iloc[6])
            processed_data['Support_School Administration'][district].append(d_support.iloc[7])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[8])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[9])
            processed_data['Support_Food Services'][district].append(d_support.iloc[10])
            processed_data['Support_Other'][district].append(d_support.iloc[11])

            r_other = other.index[other['Unnamed: 2'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[6])
            processed_data['Other_Other'][district].append(d_other.iloc[7])
            processed_data['Total'][district].append(d_other.iloc[8])

            r_turnover = turnover.index[turnover['District Name'] == district].tolist()[0] + 8
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[9])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[4] / d_turnover.iloc[3] - 1)

    for year in ['2018']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']

        for district in districts:
            r_instructional = instructional.index[instructional['Unnamed: 2'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]

            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[4])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[5])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[9])
            
            r_support = support.index[support['Unnamed: 2'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[4])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[5])
            processed_data['Support_General Administration'][district].append(d_support.iloc[6])
            processed_data['Support_School Administration'][district].append(d_support.iloc[7])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[8])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[9])
            processed_data['Support_Food Services'][district].append(d_support.iloc[10])
            processed_data['Support_Other'][district].append(d_support.iloc[11])

            r_other = other.index[other['Unnamed: 2'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[6])
            processed_data['Other_Other'][district].append(d_other.iloc[7])
            processed_data['Total'][district].append(d_other.iloc[8])

            r_turnover = turnover.index[turnover['District Name'] == district].tolist()[0] + 8
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[9])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[4] / d_turnover.iloc[3] - 1)

    for year in ['2019', '2020', '2021']:
        instructional = raw_data[year]['instructional.xls']
        support = raw_data[year]['support.xls']
        other = raw_data[year]['all.xls']
        turnover = raw_data[year]['turnover.xls']
        
        for district in districts:
            r_instructional = instructional.index[instructional['Unnamed: 4'] == district].tolist()[0] + 2
            d_instructional = instructional.iloc[r_instructional]

            processed_data['Instructional_Salaries'][district].append(d_instructional.iloc[6])
            processed_data['Instructional_Employee Benefits'][district].append(d_instructional.iloc[7])
            processed_data['Instructional_Purchased Services'][district].append(d_instructional.iloc[8])
            processed_data['Instructional_Supplies & Materials'][district].append(d_instructional.iloc[9])
            processed_data['Instructional_Capital Outlay'][district].append(d_instructional.iloc[10])
            processed_data['Instructional_Other'][district].append(d_instructional.iloc[11])
            
            r_support = support.index[support['Unnamed: 4'] == district].tolist()[0] + 2
            d_support = support.iloc[r_support]

            processed_data['Support_Pupils'][district].append(d_support.iloc[6])
            processed_data['Support_Instructional Staff'][district].append(d_support.iloc[7])
            processed_data['Support_General Administration'][district].append(d_support.iloc[8])
            processed_data['Support_School Administration'][district].append(d_support.iloc[9])
            processed_data['Support_Operations & Maintenance'][district].append(d_support.iloc[10])
            processed_data['Support_Pupil Transporation'][district].append(d_support.iloc[11])
            processed_data['Support_Food Services'][district].append(d_support.iloc[12])
            processed_data['Support_Other'][district].append(d_support.iloc[13])

            r_other = other.index[other['Unnamed: 4'] == district].tolist()[0] + 2
            d_other = other.iloc[r_other]

            processed_data['Other_Community Services'][district].append(d_other.iloc[8])
            processed_data['Other_Other'][district].append(d_other.iloc[9])
            processed_data['Total'][district].append(d_other.iloc[10])

            r_turnover = turnover.index[turnover['Unnamed: 1'].apply(lambda x: str(x).upper()) == district].tolist()[0] + 8
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[9])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[4] / d_turnover.iloc[3] - 1)

    for year in ['2022', '2023']:
        turnover = raw_data[year]['turnover.xls']

        for district in districts:
            r_turnover = turnover.index[turnover['Unnamed: 1'].apply(lambda x: str(x).upper()) == district].tolist()[0] + 8
            d_turnover = turnover.iloc[r_turnover]

            processed_data['Teacher Turnover Rate'][district].append(d_turnover.iloc[9])
            processed_data['Teacher Growth Rate'][district].append(d_turnover.iloc[4] / d_turnover.iloc[3] - 1)

    return processed_data

def export_to_csv(expenditure_data):
    for expenditure_type, data in expenditure_data.items():
        columns = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        if expenditure_type == 'Teacher Turnover Rate' or expenditure_type == 'Teacher Growth Rate':
            columns = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

        df = pd.DataFrame.from_dict(data, orient='index', columns=columns)
        output_file = f"{expenditure_type}.csv"
        df.to_csv(output_file)

if __name__ == "__main__":
    input_directory = "data"
    expenditure_data = process_files(input_directory)
    export_to_csv(expenditure_data)
