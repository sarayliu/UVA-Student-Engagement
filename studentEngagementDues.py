import pandas as pd
import matplotlib.pyplot as plt
import re

data = pd.read_csv('raw_data.csv', encoding = "ISO-8859-1")
# with open('raw_data.csv', 'rb') as pd:
#   data = pd.read_csv('raw_data.csv')
#print(data)

data.rename(
    columns={
        'Membership Type':
        'MembershipType',
        'Approximate year the organization was founded at UVA':
        'YearFoundedUVA',
        'Total number of Members (approximate)':
        'TotalMembers',
        'Please list your primary sources of funding (SAF,fundraisers,national organizations,alumni,departments,etc.)':
        'FundingSource',
        'Not including SAF,approximately how much money does your organization fundraise per academic year?':
        'MoneyFundraisedAnnually',
        'Approximate membership dues per academic year (if zero,please write "zero")':
        'AnnualDues',
        'Please list 3-5 Primary Events/Programs that your CIO hosts each year. If you do not have annual recurring events,please list some of the events/programs you hosted this past year.':
        'PrimaryEvents',
        'Approximately,how much money do members spend out of pocket per academic year,not including dues,for your CIO activities? (write the number,don\'t include $)':
        'OutOfPocketExpenses',
        'Does???ÿthis organization require an application or an interview/audition process to join?':
        'ApplicationProcess',
        'How frequently does???ÿthis organization meet?':
        'MeetingFrequency',
        'Approximately how many hours/week do non-exec members spend on your organization\'s activities (meetings,events,planning,etc.)?':
        'HoursSpentByNonExec',
        'When does???ÿthis organization elect new officers?':
        'WhenNewOfficersElected',
        'When does???ÿthis organization do recruitment/membership intake?':
        'WhenRecruitment',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Marketing':
        'AdditionalResourceMarketing',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Planning Events':
        'AdditionalResourcePlanningEvents',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Reserving Spaces':
        'AdditionalResourceReservingSpaces',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Fundraising/Budgeting/Co-Sponsorships':
        'AdditionalResourceFundraising',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Transitioning Officers':
        'AdditionalResourceTransitioningOfficers',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Recruiting New Members':
        'AdditionalResourceRecruiting',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Delegation':
        'AdditionalResourceDelegation',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Community Building/Icebreakers':
        'AdditionalResourceCommunity',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Motivating Members':
        'AdditionalResourceMotivatingMembers',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Holding Members Accountable':
        'AdditionalResourceMemberAccountability',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Developing a Mission/Vision':
        'AdditionalResourceDevelopMission',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Collaboration (with other CIOs,the community,faculty/staff,etc.)':
        'AdditionalResourceCollaboration',
        'Please check any of the following areas that your organization would most like additional resources on (try for a minimum of 3 or if not interested,select NONE). - Other':
        'AdditionalResourceOther',
        'Are you the 2020-2021 incoming President OR a 2020-2021 returning member/officer????ÿ':
        'IncomingOrReturning',
        'Are you a first time President?':
        'FirstTimePresident'
    },
    inplace=True)
#data.head(3)
print(data.describe())
print(list(data.columns))
print("Number of NaN: ", data.isna().sum())
#isna(): This function takes a scalar or array-like object and indicates whether values are missing (NaN in numeric arrays, None or NaN in object arrays, NaT in datetimelike).

#print(data['AdditionalResourceFundraising'].value_counts())
#FUNDING AND NUMBER OF MEMBERS
#print(data[['FundingSource', 'TotalMembers']])

#FUNDING AND MEMBER DUES
#print(data[['FundingSource', 'AnnualDues']])

#FUNDING AND APPLICATION PROCESS
#print(data[['FundingSource', 'ApplicationProcess']])

#FUNDING AND ACTIVITIES/EVENTS
#print(data[['FundingSource', 'PrimaryEvents']])
print("-------------------------------------")
print("Funding Sources Value Counts: ")
#print(data['FundingSource'].value_counts())
print(data['FundingSource'])
# print(data['FundingSource'].value_counts().index.tolist())
print(data['FundingSource'].value_counts().to_json())
# print(data['AnnualDues'][252])

# print("-------------------------------------")
# print("Application Process Value Counts: ")
# print(data['ApplicationProcess'].value_counts())

'''dues = 0
for s in data['FundingSource'].tolist():
  if "dues" in s.lower():
    dues = dues+1
print(dues)'''

'''
~~~~ATTENTION ATTENTION ATTENTION~~~~~~~
-----------------
ANN's TRY BUT ITS STILL NOT GOOD
- NOT IN THIS CODE but I added "keep_default_na = False" to reading the file since it read n/a as NaN, which is wrong
- I assumed "no response" and "-" as actual NaN values
- Uppercased everything
- Split each string but "," and "AND" to have a list as column value
- used regex to extract some common funding sources
- had some more regex because regex is awful
- the listed .apply() cases of regex is for actual regex expressions
- the dict patterns of regex is just for matching specific words
- sorted each list alphabetically
- joined the sources together (if there were multiple) with a semicolon and no space

PROBLEMS
- Still a lot of left overs, not sure what we'll do to categorize them as?
- What're we going to do about the cases with multiple sources? Is there anyway to categorize such as "more than 2 sources, containing saf"?
- Some of them are weird and start with semicolons, which means that somehow the strings were split with an empty string before one of the delimiters... except that shouldn't be the case?

-----------------
'''
df= pd.DataFrame()
# print("df: ")
# print(df)
df['FundingSource']= data['FundingSource'][0:643].str.upper()
df['MembershipType']= data['MembershipType'][0:643].str.upper()
print(df['MembershipType'])
df['Dues']= data['AnnualDues'][0:643].str.upper()
print(df['Dues'])
df = df[df != "NO RESPONSE"].dropna()
# print(df)
# print("-------------------------------------")
df['FundingSource'] =  df['FundingSource'].apply(lambda x: re.sub(r' AND',',', str(x)))
df['FundingSource'] =  df['FundingSource'].apply(lambda x: [w for w in re.split(r', |,', str(x).strip())])
df['FundingSource'] =  df['FundingSource'].apply(lambda x: [re.sub(r'^.*GRANT.*$', 'GRANTS', str(y)) for y in x])
df['FundingSource'] =  df['FundingSource'].apply(lambda x: [re.sub(r'^.*DONATION.*$', 'DONATIONS', str(y)) for y in x])
df['FundingSource'] =  df['FundingSource'].apply(lambda x: [re.sub(r'^.*ALUMNI.*$', 'ALUMNI', str(y)) for y in x])
df['FundingSource'] =  df['FundingSource'].apply(lambda x: [re.sub(r'^.*DUE.*$', 'DUES', str(y)) for y in x])
df['FundingSource'] =  df['FundingSource'].apply(lambda x: [re.sub(r'^.*SHOW.*$', 'SHOWS', str(y)) for y in x])
df['FundingSource'] =  df['FundingSource'].apply(lambda x: [re.sub(r'^.*LAW SCHOOL.*$', 'LAW SCHOOL FOUNDATION', str(y)) for y in x])
#df =  [re.split(r', ', str(x)) for x in df]
# print(df)
#df = df.apply(lambda x: [re.sub(r"FUNDRAISING|FUNDRAISER","FUNDRAISERS",str(y)) for y in x])
dict = {"FUNDRAISING":"FUNDRAISERS",
        "FUNDRAISER":"FUNDRAISERS",
        "NATIONAL ORGANIZATION":"NATIONAL ORGANIZATIONS",
    "MEMBERSHIP DUES":"DUES",
        "CLUB DUES":"DUES",
        "STUDENT DUES":"DUES",
        "LAW SCHOOL": "LAW SCHOOL FOUNDATION",
        "THE LAW SCHOOL FOUNDATION": "LAW SCHOOL FOUNDATION",
        "THE LAW SCHOOL": "LAW SCHOOL FOUNDATION",
    "N/A": "NONE",
 #       ".*ALUMNI.*": "ALUMNI",
    "UVA PARENT'S FUND": "PARENTS FUND",
        "PARENT'S FUND": "PARENTS FUND",
       "UVA PARENTS' FUND": "PARENTS FUND",
        "PARENTS' FUND": "PARENTS FUND",
       "PARENT FUND": "PARENTS FUND"}
    #   ".*GRANT.*": "GRANTS"
pattern = re.compile('|'.join(r'^' + re.escape(key) + r'$' for key in dict.keys()))
df['FundingSource'] = df['FundingSource'].apply(lambda x: [pattern.sub(lambda m: dict[m.group()], y) for y in x])
df['FundingSource'] = df['FundingSource'].apply(lambda x: ";".join(sorted(x)))
# print(df['FundingSource'].value_counts().to_json())


# ANN'S GRAPHING CODE
# ---------------------------
saf = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "SAF")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "SAF")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "SAF")].count()]
# print(saf)

fundraisers = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "FUNDRAISERS")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "FUNDRAISERS")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "FUNDRAISERS")].count(),]

dues = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "DUES")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "DUES")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "DUES")].count()]

none = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "NONE")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "NONE")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "NONE")].count()]

lsf = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "LAW SCHOOL FOUNDATION")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "LAW SCHOOL FOUNDATION")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "LAW SCHOOL FOUNDATION")].count()]

alumni = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "ALUMNI")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "ALUMNI")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "ALUMNI")].count()]

grants = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "GRANTS")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "GRANTS")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "GRANTS")].count()]

national = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "NATIONAL ORGANIZATIONS")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "NATIONAL ORGANIZATIONS")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "NATIONAL ORGANIZATIONS")].count()]

fundraisersSaf = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "FUNDRAISERS;SAF")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "FUNDRAISERS;SAF")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "FUNDRAISERS;SAF")].count()]

duesFundraisers = [df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY UNDERGRADUATE STUDENTS") & (df['FundingSource'] == "DUES;FUNDRAISERS")].count(),
      df['MembershipType'][(df['MembershipType'] == "PREDOMINANTLY GRADUATE STUDENTS") & (df['FundingSource'] == "DUES;FUNDRAISERS")].count(),
       df['MembershipType'][(df['MembershipType'] == "BOTH UNDERGRADUATE AND GRADUATE STUDENTS") & (df['FundingSource'] == "DUES;FUNDRAISERS")].count()]

# index = ['Undergraduate', 'Graduate', 'Both']
# dfplot = pd.DataFrame({'SAF': saf, 'Fundraisers': fundraisers, 'Dues': dues, 'None': none, 'Law School Foundation': lsf, 'Alumni': alumni, 'Grants': grants, 'National Organizations': national,
#                       'Fundraisers and SAF': fundraisersSaf, 'Dues and Fundraisers': duesFundraisers}, index = index)
# ax = dfplot.plot.bar(stacked=True)
# ax.set(ylim=(0, 200))


# plt.title("Distribution of Funding Sources with respect to Club Membership Type")
# plt.xlabel("Club Membership Type")
# plt.ylabel("Number of Clubs")
# plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# #~~~~~TRANSPOSED STACKED BAR CHART~~~~~~~~~

# dfplott = dfplot.transpose()
# ax = dfplott.plot.bar(stacked=True)
# ax.set(ylim=(0, 100))

# plt.title("Distribution of Club Membership Types with respect to Funding Sources")
# plt.xlabel("Funding Source Combinations")
# plt.ylabel("Number of Clubs")
# plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
# plt.show();


# Dues
# print(df['FundingSource'].value_counts().keys())
# print(data['AnnualDues'].values())
# xaxis = data['AnnualDues'].values()
# yaxis = df['FundingSource'].value_counts().keys()
# width = 0.35
# fig, ax = plt.subplots()
# ax.bar(xaxis, yaxis, width, label = 'Dues Range')
# ax.set_ylabel('Funding Source')
# ax.set_ylabel('Dues Range')
# ax.set_title('Funding Sources for Various Dues Ranges')
# ax.legend()
# plt.show()

# for value in df.itertuples():
df.loc[df['Dues'] == 'ZERO', 'Dues'] = 0
df.loc[df['Dues'] == 'zero', 'Dues'] = 0
df.loc[df['Dues'] == 'There are no mandatory dues. However, we do ask for members to contribute $10 a semester, if possible.', 'Dues'] = 0
df.loc[df['Dues'] == 'THERE ARE NO MANDATORY DUES. HOWEVER, WE DO ASK FOR MEMBERS TO CONTRIBUTE $10 A SEMESTER, IF POSSIBLE.', 'Dues'] = 0
df.loc[df['Dues'] == 'ZERO (STARTING IN FALL 2020)', 'Dues'] = 0
# print(df['Dues'][252])
for value in df['Dues']:
    if isinstance(value, str):
        # print(value)
        # if(value == '$200 '):
            # print(value[len(value) - 1])
        # if value == 'THERE ARE NO MANDATORY DUES. HOWEVER WE DO ASK FOR MEMBERS TO CONTRIBUTE $10 A SEMESTER, IF POSSIBLE.':
        #     print('yay')
        #     df.loc[df['Dues'] == value, 'Dues'] = 0
        #     value = 0
        if value[len(value) - 1] == ' ':
            df.loc[df['Dues'] == value, 'Dues'] = value[:len(value) - 1]
            value = value[:len(value) - 1]
        if ',' in value:
            idxComma = value.find(',')
            df.loc[df['Dues'] == value, 'Dues'] = value[:idxComma] + value[idxComma+1:]
            value = value[:idxComma] + value[idxComma+1:]
        if '-' in value:
            idxDash = value.find('-')
            low = value[0:idxDash]
            if ' ' in value:
                idxSpace = value.find(' ')
                high = value[idxDash+1:idxSpace]
            else:
                high = value[idxDash+1:]
            if low[0] == '$':
                low = int(low[1:])
            elif low.lower() == 'zero':
                low = 0
            else:
                low = int(low)
            if high[0] == '$':
                high = high[1:]
            high = int(high)
            df.loc[df['Dues'] == value, 'Dues'] = int((low + high)/2)  
            value = int((low + high)/2)  
            continue
        if value[0] == '$':
            value2 = value[1:]
            # print(value)
            value2 = int(float(value2))
            df.loc[df['Dues'] == value, 'Dues'] = value2
print('CLEANED DUES')
df['Dues'] = df['Dues'].astype(int)
print(df['Dues'])
# print(df['Dues'].dtype)
# print(df['FundingSource'])

saf2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "SAF")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "SAF")].count(),
       df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "SAF")].count()]

fundraisers2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "FUNDRAISERS")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "FUNDRAISERS")].count(),
       df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "FUNDRAISERS")].count(),]

dues2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "DUES")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "DUES")].count(),
       df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "DUES")].count()]

none2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "NONE")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "NONE")].count(),
       df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "NONE")].count()]

lsf2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "LAW SCHOOL FOUNDATION")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "LAW SCHOOL FOUNDATION")].count(),
       df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "LAW SCHOOL FOUNDATION")].count()]

alumni2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "ALUMNI")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "ALUMNI")].count(),
       df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "ALUMNI")].count()]

grants2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "GRANTS")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "GRANTS")].count(),
       df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "GRANTS")].count()]

national2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "NATIONAL ORGANIZATIONS")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "NATIONAL ORGANIZATIONS")].count(),
      df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "NATIONAL ORGANIZATIONS")].count()]

fundraisersSaf2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "FUNDRAISERS;SAF")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "FUNDRAISERS;SAF")].count(),
       df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "FUNDRAISERS;SAF")].count()]

duesFundraisers2 = [df['Dues'][(df['Dues'] == 0) & (df['FundingSource'] == "DUES;FUNDRAISERS")].count(),
      df['Dues'][(df['Dues'] > 0) & (df['Dues'] < 50) & (df['FundingSource'] == "DUES;FUNDRAISERS")].count(),
       df['Dues'][(df['Dues'] > 50) & (df['FundingSource'] == "DUES;FUNDRAISERS")].count()]

index2 = ['$0', '\$0 - \$50', '$50+']
dfplot2 = pd.DataFrame({'SAF': saf2, 'Fundraisers': fundraisers2, 'Dues': dues2, 'None': none2, 'Law School Foundation': lsf2, 'Alumni': alumni2, 'Grants': grants2, 'National Organizations': national2,
                      'Fundraisers and SAF': fundraisersSaf2, 'Dues and Fundraisers': duesFundraisers2}, index = index2)
ax2 = dfplot2.plot.bar(stacked=True)
ax2.set(ylim=(0, 200))


plt.title("Distribution of Funding Sources with respect to Dues")
plt.xlabel("Annual Dues")
plt.ylabel("Number of Clubs")
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()

#~~~~~TRANSPOSED STACKED BAR CHART~~~~~~~~~

dfplott2 = dfplot2.transpose()
ax2 = dfplott2.plot.bar(stacked=True)
ax2.set(ylim=(0, 100))

plt.title("Distribution of Annual Dues with respect to Funding Sources")
plt.xlabel("Funding Source Combinations")
plt.ylabel("Number of Clubs")
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()