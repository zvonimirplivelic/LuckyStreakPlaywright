from playwright.sync_api import Page, expect

def test_successful_qa_job_application(page: Page) -> None:
    
    page.goto("https://luckystreaklive.com/career/qa-engineer/")
    
    ## Allow cookies
    page.get_by_role("button", name="Allow all").click()
    
    ## Validate advert
    expect(page.locator("h1")).to_contain_text("QA Engineer")
    
    ## Fill the form
    page.get_by_placeholder("Name").fill("")
    page.get_by_placeholder("Surname").fill("")
    page.get_by_placeholder("Phone").fill("")
    page.get_by_placeholder("Email").fill("")
    page.get_by_placeholder("Message").fill("This is automated job application with Python Playwright")
    
    page.get_by_text("Upload CV").click()
    page.get_by_label("Upload CV").set_input_files("")
    
    page.locator("#form-field-experience").get_by_text("I have work experience in").click()
    page.get_by_text("I agree to transfer of my").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("The form was sent")).to_be_visible()
    