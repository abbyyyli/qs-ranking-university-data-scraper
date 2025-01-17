from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd







def decline_terms_and_conditions_popup(driver):
#Wait until the popup is visivle
    time.sleep(10)
    #Try to close with the popup button
    try:
            # Close the popup
            popup_close_button = driver.find_element(By.XPATH, '//*[@id="popup-buttons"]/button[1]')
            popup_close_button.click()
    except Exception as e:
        print("Popup not found or already closed:", e)
    time.sleep(2)

def close_remaining_popups(driver):
    #Cancel 2 popups.
    try:
        # Wait until the popup is visible
        time.sleep(90)

        popup = driver.find_element(By.XPATH, f"//div[contains(@class,'modal-content')]")
        print('Found the first popup!')
        # Select the "Academic" radio button
        academic_radio_button = popup.find_element(By.XPATH, f"//input[contains(@type,'radio') and contains(@name,'role')and contains(@value,'Academic')]")
        academic_radio_button.click()

        # Locate and click the submit button
        submit_button = popup.find_element(By.XPATH, "//button[@data-dismiss='modal']")
        submit_button.click()
        time.sleep(2)

        #second popup
        popup = driver.find_element(By.XPATH, f"//div[contains(@class,'modal-content')]")
        print('Found the second popup!')
        cross_button = popup.find_element(By.XPATH, '//*[@id="success_survey"]/div/div/div[1]/img')
        cross_button.click()

        time.sleep(2)
    except Exception as e:
        print("Popup not found or already closed:", e)

# If not set a stopage value, the function will continue till the end of website
def keep_hitting_load_more_button(driver,stopage=None):
    # KEEP HITTING THE LOAD MORE BUTTON
    count = 0
    while True:
        try:
                # Close the popup
                popup_close_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn ') and contains(@class , 'btn-primary') and contains(@class , 'loadmorebutton')]")
                popup_close_button.click()
                print('Page Count -',count)
        except Exception as e:
            print("'Load more button' not found or already closed:", e)
            break
        
        if stopage!=None and count==stopage:
             break
        time.sleep(3)
        count+=1


def scroll_back_to_top(driver):
    #scroll back to top
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)
    print('Let the Scraping begin')






def collect_data(driver,rows,inner_id_name):
    master_list = [] # data from every row will be turned into a dictionary and get appended into this list
    for i in range(len(rows)):
        print('Now I am at row ----->',i,'of',len(rows))
        info_dict={
            'University':'',
            'Country':''

        }
        curr_row = rows[i]
        curr_row_item = curr_row.text.split('\n')
        nid_value = curr_row.get_attribute('nid')
        info_dict.update({curr_row_item[0].split()[0]:curr_row_item[0].split()[1]})
        info_dict.update({curr_row_item[1].split(':')[0]:curr_row_item[1].split(':')[1].strip()})
        info_dict['University'] = curr_row_item[2]
        info_dict['Country'] = curr_row_item[3].split(', ')[1]
        info_dict.update({curr_row_item[-4]:curr_row_item[-3]})
        info_dict.update({curr_row_item[-2]:curr_row_item[-1]})
        time.sleep(1)

        for name in inner_id_name[1:]:
            
            time.sleep(1)
            learning_experience_tab = curr_row.find_element(By.XPATH, f"//a[contains(@class,'nav-link') and contains(@id ,'{name}-{nid_value}') and contains(@data-toggle, 'tab') ]")
            
            learning_experience_tab.click()
            time.sleep(1)


            
            curr_row_elem_obj = driver.find_element(By.ID,f"{name}-{nid_value}-tab")
            curr_row_elem_obj_list = curr_row_elem_obj.text.split('\n')
            if curr_row_elem_obj_list[0] == 'Sustainability Score':
                info_dict.update({curr_row_elem_obj_list[0]:curr_row_elem_obj_list[1]})
            else:
                for curr_row_elem_obj_list_idx in range(0,len(curr_row_elem_obj_list),2):
                    info_dict.update({curr_row_elem_obj_list[curr_row_elem_obj_list_idx]:curr_row_elem_obj_list[curr_row_elem_obj_list_idx+1]})
        


            time.sleep(1)

        master_list.append(info_dict)
    return master_list


def generate_csv_from_data(master_list,file_name='qs_university_ranking_2024'):
    df = pd.DataFrame(master_list)
    # Save the DataFrame to a CSV file
    df.to_csv(f'{file_name}.csv', index=False)


def main():
    inner_id_name = ['research-discovery','learning-experience','employability','global-engagement', 'sustainability']
    driver = webdriver.Chrome()
    start_page = 0 # You can change this as per your requirement
    url = f"https://www.topuniversities.com/world-university-rankings/2024?page={start_page}"
    driver.maximize_window()
    driver.get(url)

    decline_terms_and_conditions_popup(driver)
    close_remaining_popups(driver)
    keep_hitting_load_more_button(driver)

    rankings = driver.find_element(By.ID, 'ranking-data-load')
    rows = rankings.find_elements(By.XPATH,"//div[contains(@class,'ind ') and contains(@class , 'main')]")
    print('Total University found ---------->',len(rows))

    scroll_back_to_top(driver)
    master_list = collect_data(driver,rows,inner_id_name)
    generate_csv_from_data(master_list)
    time.sleep(5)
    driver.close()




if __name__ == "__main__":
     main()
