import seaborn as sb
import pandas as pd
import matplotlib.pyplot as mpl

#grab the data set 
df = pd.read_csv('nypd.csv')

print(df.head(10))

#histogram
mpl.figure(figsize=(7,7))
graph1 = sb.histplot(x = 'BORO', data = df, color = "red", stat='count',element='bars')
graph1.set_title('Total Shooting Incidents in the Five Boroughs')
mpl.show()

#line graph 
data1=df[['OCCUR_TIME','Latitude','Longitude','PERP_RACE','VIC_RACE',]]
data1['Time']=data１['OCCUR_TIME'].apply(lambda x:str(x)[0:2])
data1['count']=1
data1a=data1[['Time','count']].groupby('Time',as_index=False)['count'].sum()
data1a=data1a.sort_values('Time',ascending=True)
x=data1a['Time']
y=data1a['count']
mpl.figure(figsize=(13,7))
sb.lineplot(data=data1a,x='Time', y='count',sort=True) 
mpl.title('Time of incident occurrence')
mpl.xlabel('Time')
mpl.ylabel('Count')
mpl.show()


#pie chart 
mpl.figure(figsize=(13,7))
print("Total Counts of Incident Occuring Outside: ",df['LOC_OF_OCCUR_DESC'].value_counts()['OUTSIDE'])
print("Total Counts of Incident Occuring Outside: ",df['LOC_OF_OCCUR_DESC'].value_counts()['INSIDE'])
data = [1474,242]
labels = ['Percent of Incidents: Outside','Percent of Incidents:Inside']
colors = sb.color_palette('pastel')[0:2]
mpl.pie(data,labels = labels,colors=colors,autopct='%.0f%%')
mpl.show()

#Count Plot for Sex of the Victim 
mpl.figure(figsize=(13,7))
graph2 = sb.countplot(x = 'VIC_AGE_GROUP', data = df, color = "orange")
mpl.xlabel('Count by Age of the Victim')
graph2.set_title('Count by Age of the Victim')
mpl.show()

#Count plot for race of the perpetrator  
mpl.figure(figsize=(13,7))
graph2 = sb.countplot(x = 'PERP_RACE', data = df, color = "green")
mpl.xlabel('Count by Race of the Perpetrator')
graph2.set_title('Count by Race of the Perpetrator')
mpl.show()

#scatter plot for the location of incidents 
mpl.figure(figsize=(13,7))
graph3 = sb.scatterplot(y = 'LOC_OF_OCCUR_DESC', x ="BORO", data = df)
mpl.xlabel("Described location of incident")
graph3.set_title('Scatter plot of locations')
mpl.show()

#barplot
#print statistics of the
print("Total Counts of Male Victims: ",df['VIC_SEX'].value_counts()['M'])
print("Total Counts of Female Victims:",df['VIC_SEX'].value_counts()['F'])
# Create the barplot
data = {
    "Gender": ["Male", "Female"],
    "Count": [1503, 242]
}
df = pd.DataFrame(data)
# "tidy" format
df = pd.melt(df, id_vars=["Gender"], value_vars=["Count"], var_name="Variable", value_name="Count")
sb.barplot(x="Gender", y="Count", data=df, color="blue")
mpl.xlabel("Gender")
mpl.ylabel("Count")
mpl.title("Victim Count by Gender")
mpl.show()


