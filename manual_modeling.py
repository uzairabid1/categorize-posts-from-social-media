import pandas as pd


def check_post_type(post_text):
    indians_issue = ['Indian', 'indian', 'desi', 'Desi', 'India', 'Indians', 'indians', 'india']
    immigration_issues = ['immigrant', 'Immigrant', 'moved to', 'moved from', 'H1-B', 'H1B', 'h1b','Immigration','immigration','visa','Visa','h1','h4','i140s','i140']
    therapist_issue = ['Therapist', 'therapist', 'session', 'Session', 'sessions', 'Therapists', 'therapists','therapy sucks','therapy issue' ]
    toxic_manager = ['Toxic manager', 'Toxic Manager', 'Manager', 'manager', 'toxic manager']
    loneliness = ['alone', 'Alone', 'lonely', 'loneliness', 'abandoned','No Friends','no friends','No friends']
    imposter_syndrome = ['imposter','imposter syndrome','irrelevant','Imposter','Imposter syndrome']
    bullying = ['rude', 'bully', 'bullying', 'Bully', 'Bullying', 'Rude', 'bullied', 'Bullied']
    family_issues = ['family issue','parents issue','dad issue','father issue']
    layoff = ['layoff', 'layoffs', 'laid off', 'downsizing', 'Layoff', 'Layoffs', 'Laid off']
    print(post_text)
    keyword_lists = {
        "Indians Issue": indians_issue,
        "Therapist Issue": therapist_issue,
        "Toxic Manager": toxic_manager,
        "Family Issues": family_issues,
        "Loneliness": loneliness,
        "Bullying": bullying,
        "Immigration Issue": immigration_issues,
        "Layoff Issue": layoff,
        "Imposter Syndrome": imposter_syndrome
    }

    for key, keywords in keyword_lists.items():
        if any(keyword in post_text for keyword in keywords):
            return key

    return 'Others'

def check_keywords(post_text):

    if 'Stress' in post_text or 'stress' in post_text:
        return 'Stress'
    if 'Burnout' in post_text or 'burnout' in post_text or 'burntout' in post_text:
        return 'Burnout'
    if 'Depressed' in post_text or 'depressed' in post_text:
        return 'Depressed'
    if 'Anxiety' in post_text or 'anxiety' in post_text or 'anxious' in post_text:
        return 'Anxiety'
    if 'Therapy' in post_text or 'therapy' in post_text:
        return 'Therapy'
    if 'Irrelevant' in post_text or 'irrelevant' in post_text:
        return 'Irrelevant'
    if 'Autism' in post_text or 'autism'  in post_text:
        return 'Autism'
    if 'ADHD' in post_text or 'adhd' in post_text:
        return 'ADHD'
    if 'PTSD' in post_text or 'ptsd' in post_text:
        return 'PTSD'
    if 'sad' in post_text or 'SAD' in post_text:
        return 'Sad'
    if 'mentalhealth' in post_text or 'Mental Health' in post_text or 'Mentalhealth' in post_text:
        return 'Mental Health'
    if 'Trauma' in post_text or 'trauma' in post_text:
        return 'Trauma'
    
    return 'Others' 


df = pd.read_csv('backup_output/updated_posts.csv')

for index, row in df.iterrows():
    post_text = row['Post Text'] 

    try:
        post_type = check_post_type(post_text)
    except:
        post_type = ''
    try:
        keywords_used = check_keywords(post_text)
    except:
        keywords_used = ''
    df.at[index, 'Type of Post'] = post_type
    df.at[index, 'Keyword Used'] = keywords_used

df.to_csv('backup_output/updated_posts.csv', index=False)