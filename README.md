# booking-scraper

## **Project Description: Web Scraper for Booking.com**

This web scraper is designed to extract comprehensive information about hotels listed on "https://www.booking.com/" for a specific city. The main goal is to gather detailed data on hotels, including rental prices for the current month, URLs, ratings, reviews, and remarks. 

**Key Features:**

1. **Target Website**: The web scraper focuses on "https://www.booking.com/" to ensure the data is reliable and up-to-date.
2. **City-Specific Data Collection**: Users can specify a city to collect hotel data, making the scraper versatile for different geographic locations.
3. **Rental Prices**: The scraper fetches rental prices for the current month, providing a snapshot of current accommodation costs.
4. **Hotel URLs**: Extracts the URLs of hotel listings for easy access to the original pages.
5. **Ratings and Reviews**: Gathers ratings and reviews, giving insights into customer satisfaction and hotel quality.
6. **Remarks**: Collects any additional remarks or descriptions provided in the hotel listings for a richer dataset.

**Technologies Used:**

- **Selenium**: Utilized for browser automation to handle dynamic content and navigate through the website.
- **Scrapy**: A robust web scraping framework used to extract the data efficiently.

**Implementation Overview:**

- **Selenium** is used to load the webpage, handle JavaScript execution, and manage interactions that require a real browser environment.
- **Scrapy** is employed to structure the scraping process, define data extraction rules, and save the gathered information into a structured format like JSON or CSV.

**Benefits:**

- **Automated Data Collection**: Saves time and effort by automating the data extraction process.
- **Up-to-Date Information**: Ensures that the data is current, reflecting the latest prices and reviews.
- **Comprehensive Dataset**: Provides a detailed overview of hotels, aiding in market analysis, travel planning, or competitive research.

This web scraper is a powerful tool for anyone needing detailed and current information about hotel accommodations in a specific city from Booking.com.

### How to run:

- **Download the repository**:  
    - use command "git clone https://github.com/HritikShukla02/booking-scraper.git".

- **Activate the virtual environment**:
    - Enter the folder *booking-scraper*.
    - run the command: "source venv/Scripts/activate".

-  **Enter the Location**: 
    - Open the middlewares.py
    - Scroll to SeleniumMiddleware class
    - Update the variable **DEST** to the desired location.
    - Save the file.

- **Run Spider**:
    - cd into the *spiders* folder.
    - run command: "scrapy crawl booking_spider"


- **Output**:
    - This spider genetares a json file as the output that you can find in booking folder after the script is successfully completed.
