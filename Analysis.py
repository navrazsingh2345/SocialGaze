# Importing the necessary libraries
import pandas as pd


# Reading the dataset
df = pd.read_csv("MOCK_DATA.csv")


# Function to detect face accounts
def detect_fake_account(row):

    # Number of followers of the account
    follower_count = row['follower_count'] 

    # Number of following of the account
    following_count = row['following_count']

    # Checking if the account has profile picture or not
    profile_pic = row['profile_pic']

    # Calculating the ratio of follower and following of the account
    ratio = following_count / follower_count  if follower_count != 0 else 0

    # Conditioning for Fake and Real accounts
    if ratio > 2.1 and not profile_pic:
        return 'Fake'
    else:
        return 'Real'


# Function to classify an account to an Influencer or Normal account
def classify_real_account(row):

    # Checking if the account is real
    if row['account_type'] == 'Real':

        # Checking if the account has profile picture or not
        profile_pic = row['profile_pic']

        # Conditioning for Influencer and Real account
        if row['follower_count'] > 2500 and row['following_count'] < row['follower_count'] and profile_pic and row["total_posts"]>=30:
            return 'Influencer'
        else:
            return 'Normal'
    else:
        return 'N/A'


# Function to classify an account if activity of an account is High, Medium or Low
def classify_account_activity(row):

    # Activity of the account
    activity = row['account_activity']

    # Conditioning for activity of account
    if activity >= 14 and row['activity_pm']>=50000:
        return 'High'
    elif activity >= 5 and row['activity_pm']>=20000:
        return 'Medium'
    else:
        return 'Low'


# Calling of all functions to clean the data and analyzing it
df['account_type'] = df.apply(detect_fake_account, axis=1)

df['real_account_type'] = df.apply(classify_real_account, axis=1)

df['activity_level'] = df.apply(classify_account_activity, axis=1)


# Storing the cleaned and analyzed data to another file named "data.csv"
df.to_csv('data.csv', index=False)

# Checking if the analysis is complete without any fault
print("The data has been successfully analyzed and cleaned")

# Printing the top 5 data of the cleaned dataset
print(df.head())