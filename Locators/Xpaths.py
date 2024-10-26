from Utilities import ConfigReader

class LoginFunctionality:

    loginPageLink = ConfigReader.read_configuration("basic info", "url")
    accountIconXpath = "//li[@class='dropdown']/a/i"
    loginIconXpath = "//a[text()='Login']"
    EmailXpath = "//input[@id='input-email']"
    PasswordXpath = "//input[@id='input-password']"
    loginButtonXpath = "//input[@value='Login']"
    firstWarring = "Warning: No match for E-Mail Address and/or Password."
    secondWarring = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
    actual_warringXpath = "//div[@id='account-login']/div[1]"
    logoutXpath = "//li/a[text()='Logout']"

class RegisterFunctionality:

    registerXpath = "//a[text()='Register']"
    firstNameXpath = "//input[@id='input-firstname']"
    lastNameXpath = "//input[@id='input-lastname']"
    emailIdXpath = "//input[@id='input-email']"
    telePhoneNUmberXpath = "//input[@id='input-telephone']"
    passwordXpath = "//input[@id='input-password']"
    conformPasswordXpath = "//input[@id='input-confirm']"
    subscribeNoXpath = "//div/label[2]/input[@name='newsletter']"
    privacyPolicyXpath = "//input[@name='agree']"
    ContinueButtonXpath = "//input[@value='Continue']"
    NextContinueButtonXpath = "//a[@class='btn btn-primary']"
    expected_warringMessage = "Warning: E-Mail Address is already registered!"
    actual_warringMessageXpath = "//div[@id='account-register']/div[1]"

class ChangeUserPasswordFunctionality:

    ChangePasswordXpath = "//a[text()='Change your password']"
    newPasswordXpath = "//input[@name='password']"
    conformPasswordXpath = "//input[@name='confirm']"
    continueButtonXpath = "//input[@value='Continue']"
    backButtonXpath = "//a[text()='Back']"
    successMessageExpectedText = "Success: Your password has been successfully updated."
    successMessageXpath = "//div[@class='alert alert-success alert-dismissible']"
    conformPasswordErrorText = "Password confirmation does not match password!"
    conformPasswordErrorXpath = "//div[text()='Password confirmation does not match password!']"
    newPasswordErrorText = "Password must be between 4 and 20 characters!"
    newPasswordWarringXpath = "//div[text()='Password must be between 4 and 20 characters!']"

class FeaturedProductFunctionality:

    qafoxTitleXpath = "//div[@id='logo']"
    featuredFirstProductXpath = "//div[@class='row']/div[1]/div[1]//div[@class='image'][1]"
    featuredSecondProductXpath = "//div[@class='row']/div[2]/div[1]//div[@class='image'][1]"
    featuredThirdProductXpath = "//div[@class='row']/div[3]/div[1]//div[@class='image'][1]"
    featuredFourthProductXpath = "//div[@class='row']/div[4]/div[1]//div[@class='image'][1]"
    featuredFirstProductTitleNamesXpath = "//div[@class='row']/div[1]/div[1]//div[@class='caption']/h4/a"
    featuredSecondProductTitleNamesXpath = "//div[@class='row']/div[2]/div[1]//div[@class='caption']/h4/a"
    featuredThirdProductTitleNamesXpath = "//div[@class='row']/div[3]/div[1]//div[@class='caption']/h4/a"
    featuredFourthProductTitleNamesXpath = "//div[@class='row']/div[4]/div[1]//div[@class='caption']/h4/a"
    featureProductVerificationTextXpath = "//div[@class='btn-group']/following-sibling::h1"
    addToCartButtonXpath = "//button[@id='button-cart']"
    enterNoOfQuantity = "//input[@id='input-quantity']"
    addToWishListXpath = "//div[1]/button[@data-original-title='Add to Wish List']"
    successfullyAddToCardMessageXpath = "//div[@class='alert alert-success alert-dismissible']"
    successfullyAddToCardMessageExpected = "Success: You have added MacBook to your shopping cart!"
    tempText = ""

class ContactUsFunctionality:

    contactUsXpath = "//ul[@class='list-inline']/li[1]"
    yourNameXpath = "//input[@id='input-name']"
    emailAddressXpath = "//input[@id='input-email']"
    enquiryXpath = "//textarea[@id='input-enquiry']"
    submitButtonXpath = "//input[@type='submit']"
    continueButtonXpath = "//a[text()='Continue']"
    nameExpectedWarringMessage = "Name must be between 3 and 32 characters!"
    nameWarringXpath = "//input[@name='name']/following-sibling::div"
    emailExpectedWarringMessage = "E-Mail Address does not appear to be valid!"
    emailWarringXpath = "//input[@name='email']/following-sibling::div"
    enquiryExpectedWarringMessage = "Enquiry must be between 10 and 3000 characters!"
    enquiryWarringXpath = "//textarea[@name='enquiry']/following-sibling::div"

class ForgotPasswordFunctionality:

    forgotpasswordLINK_TEXT = "Forgotten Password"
    emailboxXPATH = "//input[@id='input-email']"
    continueButton = "//input[@value='Continue']"
    validWarring = "An email with a confirmation link has been sent your email address."
    validWarringXpath = "//div[@id='account-login']/div[1]"
    invalidWarring = "Warning: The E-Mail Address was not found in our records, please try again!"
    invalidWarringXpath = "//div[@id='account-forgotten']/div[1]"

class ModifyAddressBookFunctionality:

    modifyAddressBookXpath = "//a[text()='Modify your address book entries']"
    newAddressButtonXpath = "//a[text()='New Address']"
    firstNameXpath = "//input[@name='firstname']"
    lastNameXpath = "//input[@name='lastname']"
    companyXpath = "//input[@name='company']"
    address1Xpath = "//input[@name='address_1']"
    address2Xpath = "//input[@name='address_2']"
    cityXpath = "//input[@name='city']"
    postalCode = "//input[@name='postcode']"
    countryXpath = "//select[@name='country_id']"
    region_StateXpath = "//select[@name='zone_id']"
    defaultAddressYesXpath = "//label[1]/input[@type='radio' ]"
    defaultAddressNoXpath = "//label[2]/input[@type='radio' ]"
    continueButtonXpath = "//input[@value='Continue']"
    backButtonXpath = "//a[text()='Back']"
    deleteButtonXpath = "//table/tbody/tr[1]/td[2]/a[text()='Delete']"
    editButtonXpath = "//a[text()='Edit']"
    accountIconXpath = "//i[@class='fa fa-user']"
    logoutXpath = "//div/a[text()='Logout']"
    logoutContinueButtonXpath = "//a[text()='Continue']"
    successfullyAddedAddressOrDeletedWarringXpath = "//div[@class='alert alert-success alert-dismissible']"
    successfullyAddedAddressWarringExpected = "Your address has been successfully added"
    deletedSuccessfullyWarringExpected = "Your address has been successfully deleted"

class MyAccountEditInfoFunctionality:

    emailXpath = "//input[@id='input-email']"
    passwordXpath = "//input[@id='input-password']"
    loginButtonXpath = "//input[@value='Login']"
    editAccountInfoLinkText = "//a[text()='Edit your account information']"
    firstNameXpath = "//input[@name='firstname']"
    lastNameXpath = "//input[@name='lastname']"
    emailIdXpath = "//input[@name='email']"
    telNumXpath = "//input[@name='telephone']"
    continueButtonXpath = "//input[@value='Continue']"
    updateSuccessWarringText = "Success: Your account has been successfully updated."
    updateSuccessWarringXpath = "//div[@id='account-account']/div[1]"
    firstNameMissingWarringText = "First Name must be between 1 and 32 characters!"
    firstNameMissingWarringXpath = "//div[1]/div[@class='col-sm-10']/div[1]"
    lastNameMissingWarringText = "Last Name must be between 1 and 32 characters!"
    lastNameMissingWarringXpath = "//div[2]/div[@class='col-sm-10']/div[1]"
    emailIdMissingWarringText = "E-Mail Address does not appear to be valid!"
    emailIdMissingWarringXpath = "//div[3]/div[@class='col-sm-10']/div[1]"
    telNumMissingWarringText = "Telephone must be between 3 and 32 characters!"
    telNumMissingWarringXpath = "//div[4]/div[@class='col-sm-10']/div[1]"
    backButtonXpath = "//a[text()='Back']"

class MyWishListFunctionality:

    myWishListXpath = "//a[@id='wishlist-total']"
    outOfStockExpected = "Out Of Stock"
    continueButtonXpath = "//a[text()='Continue']"

class SearchProductFunctionality:

    searchBoxXpath = "//input[@name='search']"
    searchButtonXpath = "//div[@id='search']//button[@type='button']"
    invalidProductWarringTextMessage = "There is no product that matches the search criteria."
    invalidProductWarringMessageXpath = "//input[@id='button-search']/following-sibling::p"
