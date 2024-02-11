#___AICP Internship Task 2___#

import pandas as pd

#_____1_____
Data = [1, 4, 9, 6, 7]
index = ['a', 'x', 'c', '2', 'e']

result = pd.Series(Data, index=index, dtype = 'int64')
print(result)

#_____2_____

Data_dic = {"Bilal": 42, "Ayesha": 38, "Hadia": 39}
result_dic = pd.Series(Data_dic, dtype = 'int64')
print(result_dic)

#_____3_____

Data_frame = {
    "Day": ["1/1/2017", "1/2/2017", "1/3/2017", "1/4/2017", "1/5/2017", "1/6/2017"],
    "Temperature": [32, 35, 28, 24, 32, 31],
    "Windspeed": [6, 7, 2, 7, 4, 2],
    "Event": ["Rain", "Sunny", "Snow", "Snow", "Rain", "Sunny"]
}

display_df = pd.DataFrame(Data_frame)
print(display_df)

#_____4_____

opt_index = ['a', 'b', 'c', 'd', 'e', 'f']
display_df.index = opt_index
print(display_df)

#_____5_____

Tem_Stats = display_df["Temperature"].agg(["mean", "max", "min"])
print(Tem_Stats)

#_____6_____

path = 'D:\Career\Internships\AICP_2.0\Data_1\people.csv'
col = ["First Name", "Sex", "Email", "Phone", "Job Title"]
skip_rows = [1,5]

C_df = pd.read_csv(path, usecols=col, skiprows=skip_rows)
display = C_df.head()
print(display)

C_df = C_df.set_index(["Sex", "Job Title"], inplace=True)

C_df.to_csv('D:\Career\Internships\AICP_2.0\Data_1\Apeople.csv')

#_____7_____

path = 'D:\Career\Internships\AICP_2.0\Data_1\SampleWork.xlsx'
E_col = [0, -1]
E_s_rows=[2]

E_df = pd.read_excel(path, sheet_name=0 ,usecols=E_col, skiprows=E_s_rows, header=1)

E_df.to_excel('D:\Career\Internships\AICP_2.0\Data_1\ASampleWork.xlsx', index=False)

#_____8_____

data = {
    "Name": ["Sonia", "Bilal", "Hifza", "Kabir", "Jazim"],
    "Age" : [27, 24, 22, 32, 23],
    "Address": ["Lahore", "Karachi", "Sialkot", "Peshawar", "lhr"],
    "Qualification": ["Msc", "MA", "MCA", "Phd", "bsc"]
}

AICP_DF = pd.DataFrame(data)
df1 = AICP_DF[["Name", "Qualification"]]

Height = [5.1, 6.2, 5.1, 5.2, 5.1]
AICP_DF['Height'] = Height

AICP_DF.set_index("Name", inplace=True)

R_hifza = AICP_DF.loc["Hifza"]
R_index_3 = AICP_DF.iloc[2]

AICP_DF.drop("Bilal", inplace=True)

print("AICP_DF: ")
print(AICP_DF)
print("\nf1:")
print(df1)
print("\nRow with index Hifza: ")
print(R_hifza)
print("\nRow with index 3:")
print(R_index_3)