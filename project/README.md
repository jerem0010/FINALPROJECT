# USI Tennis Project - README

#### Video Demo: <https://youtu.be/gS5CVaVsxYE>

#### Description:

Hello everyone! I'm Jérémy LE NEZET,I'm 23-year-old and I'm from France. My CS50 final project focuses on optimizing the membership process for our tennis club, USI Tennis, and of my MySQL database.

## Project Structure

The project employs Flask to create a static website that meticulously showcases various facets of our club. HTML pages are carefully styled using CSS.

- **Home (index.html):** This central page provides general information about the club.

- **Form (formulaire.html):** This section facilitates easy sign-up for new members by capturing their details. The form uses the POST method to transmit this information to our MySQL database.

- **Court Reservation:** A built-in feature allows members to book tennis courts online, streamlining the process and updating the MySQL database accordingly.

- **Contact:** Users can also get in touch with the club via social media directly from the site.

## Data Management with MySQL

Data entered in the form is meticulously stored and managed in a MySQL database, providing significant flexibility for efficient data handling. Operations such as sorting, selection, and membership management are executed using secure SQL injections to ensure robust data security practices.

## Automated Invoicing

An innovative aspect of the project lies in the automated generation of invoices for the club. Using the convert.py script, member details stored in the MySQL database are extracted and utilized to create PDF invoices. I opted to implement this functionality using the reportlab library.

## Code Structure

The app.py file contains the essential code to run the site. In the "templates" folder, you'll find all HTML files, while the "static" folder houses static resources like images and CSS style sheets.

I encourage everyone to explore the project. Feel free to provide feedback and suggestions, as continuous improvement is a fundamental value for me. Thank you for your attention, and happy exploring! 🎾✨

JEJE

USI Tennis Project
Video Demo: Watch Demo
Description:
Hello there! I'm Jérémy LE NEZET, a 23-year-old student hailing from France. My CS50 final project is a dedicated effort to streamline the membership process for our esteemed tennis club, USI Tennis, using the dynamic duo of Flask and a MySQL database.

Project Overview
In the realm of web development, I've employed Flask to weave a dynamic yet static website. This creation meticulously showcases the essence of our tennis club through HTML pages that dance with the finesse of CSS.

Home (index.html): The nucleus of information, providing a centralized hub for all things related to the club.

Form (formulaire.html): A seamless sign-up experience for new members, elegantly utilizing the POST method to transmit data securely to our MySQL database.

Court Reservation: A frictionless online court booking feature, ensuring real-time updates to the MySQL database.

Contact: A direct line for users to engage with the club through various social media platforms.

Data Management with MySQL
The data entered through the form finds its home in our MySQL database, where it is stored securely and managed with the finesse of a maestro. Secure SQL injections stand guard, ensuring robust data security during operations such as sorting, selection, and membership management.

Automated Invoicing
A touch of innovation lies in the automated generation of invoices for the club. The convert.py script, a magician of sorts, extracts member details from the MySQL database and conjures up PDF invoices using the reportlab library.

Code Structure
The heartbeat of the site lies within app.py. The "templates" folder is a treasure trove of HTML files, while the "static" folder houses the visual elements - images and CSS style sheets.
