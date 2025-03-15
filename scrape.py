from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from datetime import datetime, timedelta
from datetime import datetime
import os
import pandas as pd
import time


username_creds = ''    # username/email
password_creds = ''    # password
file_path = "output.csv" # file name

def appendData(file_path2, data):
    temp_file = 'temp_file.csv'
   
    if os.path.isfile(file_path2):
        df = pd.read_csv(file_path2, encoding='utf-8')
    else:
        df = pd.DataFrame()
 
    df_new_row = pd.DataFrame([data])
    df = pd.concat([df, df_new_row], ignore_index=True)

    try:      
        df.to_csv(temp_file, index=False, encoding='utf-8')
    except Exception as e:
      
        print(f"An error occurred while saving the temporary file: {str(e)}")
        return False

    try:        
        os.replace(temp_file, file_path2)
    except Exception as e:

        print(f"An error occurred while replacing the original file: {str(e)}")
        return False

    return True



def extract_tc_from_post(post):
    
    tc_pattern = r'TC:\s*(\d+)'
    match = re.search(tc_pattern, post)

    if match:
        tc_value = int(match.group(1)+"000")
        return tc_value
    else:
        tc_pattern2 = r'TC : \s*(\d+)'
        match2 = re.search(tc_pattern2,post)
        if match2:
            tc_value = int(match2.group(1)+"000")
            return tc_value
        else:
            tc_pattern3 = r'TC \s*(\d+)'
            match3 = re.search(tc_pattern3,post)
            if match3:
                tc_value = int(match3.group(1)+"000")
                return tc_value
            else:
                tc_pattern4 = r'Tc: \s*(\d+)'
                match4 = re.search(tc_pattern4,post)
                if match4:
                    tc_value = int(match4.group(1)+"000")
                    return tc_value
                else:
                    tc_pattern5 = r'Tc \s*(\d+)'
                    tc_pattern6 = r'tc \s*(\d+)'
                    match5 = re.search(tc_pattern5,post)
                    match6 = re.search(tc_pattern6,post)
                    if match5 or match6:
                        tc_value = int(match5.group(1)+"000") or int(match6.group(1)+"000")
                        return tc_value
        return None

def calculate_date_from_string(input_string):
    
    today = datetime.now().date()

    if input_string[-1] == 'h':
      
        hours_to_subtract = int(input_string[:-1])
        result_date = today - timedelta(hours=hours_to_subtract)
    elif input_string == 'Yesterday':
        
        result_date = today - timedelta(days=1)
    elif input_string[-1] == 'd':
       
        days_to_subtract = int(input_string[:-1])
        result_date = today - timedelta(days=days_to_subtract)
    elif ',' in input_string:
      
        result_date = datetime.strptime(input_string, '%b %d, %Y').date()
    else:
        try:
            
            result_date = datetime.strptime(input_string, '%b %d').date()

          
            if result_date.month > today.month or (result_date.month == today.month and result_date.day >= today.day):
               
                result_date = result_date.replace(year=today.year - 1)
            else:
                
                result_date = result_date.replace(year=today.year)
        except ValueError:
           
            raise ValueError("Invalid input string format")

    return result_date

def check_post_type(post_text):
    indians_issue = ['Indian', 'indian', 'desi', 'Desi', 'India', 'Indians', 'indians', 'india']
    immigration_issues = ['immigrant', 'Immigrant', 'moved to', 'moved from', 'H1-B', 'H1B', 'h1b','Immigration','immigration','visa','Visa','h1','h4','i140s','i140']
    therapist_issue = ['Therapist', 'therapist', 'session', 'Session', 'sessions', 'Therapists', 'therapists']
    toxic_manager = ['Toxic manager', 'Toxic Manager', 'Manager', 'manager', 'toxic manager']
    loneliness = ['alone', 'Alone', 'lonely', 'loneliness', 'abandoned']
    imposter_syndrome = ['imposter','imposter syndrome','irrelevant','Imposter','Imposter syndrome']
    bullying = ['rude', 'bully', 'bullying', 'Bully', 'Bullying', 'Rude', 'bullied', 'Bullied']
    family_issues = ['parents', 'Parents', 'Parent', 'parent', 'Mother', 'mother', 'mom', 'father', 'Father', 'dad', 'family', 'Family', 'in laws', 'in-laws','sibling','brother','sister','siblings','brothers','sisters']
    layoff = ['layoff', 'layoffs', 'laid off', 'downsizing', 'Layoff', 'Layoffs', 'Laid off']
    burnout = ['burnout','burntout','Burnout','Burntout']
    addiction = ['addicted','addiction','Addicted','Addiction']

    keyword_lists = {
        "Indians Issue": indians_issue,
        "Family Issue": family_issues,
        "Therapist Issue": therapist_issue,
        "Toxic Manager": toxic_manager,
        "Loneliness": loneliness,
        "Bullying": bullying,
        "Immigration Issue": immigration_issues,
        "Layoff Issue": layoff,
        "Imposter Syndrome": imposter_syndrome,
        "Burnout": burnout,
        "Addiction": addiction
    }

    for key, keywords in keyword_lists.items():
        if any(keyword in post_text for keyword in keywords):
            return key

    return 'Others'

def check_keywords(post_text):

    if 'Stress' in post_text or 'stress' in post_text:
        return 'Stress'
    if 'Burnout' in post_text or 'burnout' in post_text or 'Burntout' in post_text or 'burntout' in post_text:
        return 'Burnout'
    if 'Addiction' in post_text or 'addicted' in post_text or 'Addicted' in post_text or 'addicted' in post_text:
        return 'Addiction'
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



driver = webdriver.Chrome(executable_path='chromedriver.exe') # replace with your path to the chromedriver


driver.get("https://www.teamblind.com/topics/Mental-Health")

log_in = driver.find_element(By.CSS_SELECTOR,"button.btn_logIn")
log_in.click()
time.sleep(0.2)



username = driver.find_element(By.CSS_SELECTOR,"input[placeholder$='Enter your work email.']")
username.send_keys(username_creds)
time.sleep(0.2)

password = driver.find_element(By.CSS_SELECTOR,"input[placeholder$='Password']")
password.send_keys(password_creds)
time.sleep(0.2)

submit_btn = driver.find_element(By.XPATH,"//strong[.='Log in']/parent::button")
submit_btn.click()
time.sleep(5)

for i in range(0,600):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)


# time.sleep(1200)

all_elements = driver.find_elements(By.XPATH,"//ul[@class='lst one_channel']/li[@class='word-break']")
print(len(all_elements))

for idx in range(4875,len(all_elements)):

    try:
        post_auth_company = driver.find_element(By.XPATH,f"//ul[@class='lst one_channel']/li[@class='word-break'][{idx+1}]/div[@class='writer']/a/div/span[1]").text.replace(' /','').strip()
    except:
        post_auth_company = ''
    try:
        post_auth_name = driver.find_element(By.XPATH,f"//ul[@class='lst one_channel']/li[@class='word-break'][{idx+1}]/div[@class='writer']/a/div/span[@class='name']").text.strip()
    except:
        post_auth_name = ''
    try:
        date_scraped = driver.find_element(By.XPATH,f"//ul[@class='lst one_channel']/li[@class='word-break'][{idx+1}]/div[@class='info']/div[last()]/a[1]").text.strip()
    except:
        date_scraped = ''
    try:
        num_comments = driver.find_element(By.XPATH,f"//ul[@class='lst one_channel']/li[@class='word-break'][{idx+1}]/div[@class='info']/a[3]").text.replace(',','').strip()
        if num_comments[-1] == 'K' and '.' in num_comments:
            num_comments = int(num_comments.replace('.','').replace('K','00'))
        else:
            num_comments = int(num_comments)
    except:
        num_comments = ''
    try:
        num_views = driver.find_element(By.XPATH,f"//ul[@class='lst one_channel']/li[@class='word-break'][{idx+1}]/div[@class='info']/a[1]").text.replace(',','').strip()
        if num_views[-1] == 'K' and '.' in num_views:
            num_views = int(num_views.replace('.','').replace('K','00'))
        else:
            num_views = int(num_views)       
    except:
        num_views = ''
    try:
        num_likes = driver.find_element(By.XPATH,f"//ul[@class='lst one_channel']/li[@class='word-break'][{idx+1}]/div[@class='info']/a[2]").text.replace(',','').strip()
        if num_likes[-1] == 'K' and '.' in num_likes:
            num_likes = int(num_likes.replace('.','').replace('K','00'))
        else:
            num_likes = int(num_likes)     
    except:
        num_likes = ''
    try:
        post_link = driver.find_element(By.XPATH,f"//ul[@class='lst one_channel']/li[@class='word-break'][{idx+1}]/a").get_attribute('href')
    except:
        continue
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(post_link)
    time.sleep(2)  
    print(post_link)
    try:
        post_title = driver.find_element(By.XPATH,f"//div[@class='tit_area']/h1").text.strip()
    except:
        post_title = ''
    try:
        post_content = driver.find_element(By.CSS_SELECTOR,"p#contentArea").text.replace('\n','').strip()
    except:
        time.sleep(3)
        try:
            post_content = driver.find_element(By.CSS_SELECTOR,"p#contentArea").text.replace('\n','').strip()
        except:
            post_content = ''
    driver.close() 
    driver.switch_to.window(driver.window_handles[0])
    try:
        tc_value = extract_tc_from_post(post_content)
    except:
        tc_value = ''
    try:
        date = calculate_date_from_string(date_scraped)
    except:
        date = ''
    try:
        type_of_post = check_post_type(post_content)
    except:
        type_of_post = ''
    
    try:
        keyword_used = check_keywords(post_content)
    except:
        keyword_used = ''
    
    data = {   
        "Post Author Company": post_auth_company,
        "Post Author Name": post_auth_name,
        "Post Title": post_title,
        "Post Text": post_content,
        "TC": tc_value,        
        "Date": date,
        "Number of Comments": num_comments,
        "Number of Views": num_views,
        "Number of Likes": num_likes,
        "Type of Post": type_of_post,
        "Keyword Used": keyword_used
    }
    print(data)
    appendData(file_path,data)
    
