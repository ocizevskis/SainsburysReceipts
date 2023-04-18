
# Sainsbury's Receipt Scanner & Purchase History
Originally made as a project for HackTheBurgh 2023, this is a refactored version of the original app, which lets you scan your sainsbury's receipts and view spending stats. Receipts are processed using Veryfi optical character recognition (OCR) API, and results are matched to entries in sainsburys.co.uk. This enables you to automatically populate item information from the scraped website and e.g. see a detailed overview of your spending per product category etc. Matching items is done by searching the truncated item name on the receipt and item price using a google search API, and retrieving the first search result that matches from the Sainsbury's website.



## Usage

**main.py** contains the code for running the API used by the web interface. run main.py via uvicorn:

> uvicorn main:app

to start the server. 

Some basic **Integration Tests** can be found under /tests, and testing it done automatically on push via github actions.



The web interface can be used to access the main dashboard with spending stats, as well as the purchase history. A pre populated database has been provided, along with some test images of receipts.
